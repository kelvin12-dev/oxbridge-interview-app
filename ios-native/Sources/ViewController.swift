import UIKit
import WebKit
import PDFKit

final class ViewController: UIViewController, WKUIDelegate, WKNavigationDelegate, WKScriptMessageHandler {
    private var webView: WKWebView!
    private var darkStatusBar = false

    override var preferredStatusBarStyle: UIStatusBarStyle {
        return darkStatusBar ? .lightContent : .darkContent
    }

    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = UIColor(red: 245/255, green: 247/255, blue: 251/255, alpha: 1)

        let userContentController = WKUserContentController()
        userContentController.add(self, name: "nativeShare")
        userContentController.add(self, name: "nativeHaptic")
        userContentController.add(self, name: "nativeOpenUrl")
        userContentController.add(self, name: "nativeRenderPdf")
        userContentController.add(self, name: "nativeTheme")

        let config = WKWebViewConfiguration()
        config.userContentController = userContentController
        config.allowsInlineMediaPlayback = true
        config.mediaTypesRequiringUserActionForPlayback = []
        config.websiteDataStore = .default()

        let wv = WKWebView(frame: .zero, configuration: config)
        wv.translatesAutoresizingMaskIntoConstraints = false
        wv.uiDelegate = self
        wv.navigationDelegate = self
        wv.isOpaque = false
        wv.backgroundColor = .clear
        wv.allowsBackForwardNavigationGestures = false
        wv.scrollView.isScrollEnabled = false
        wv.scrollView.bounces = false
        wv.scrollView.delaysContentTouches = false
        wv.scrollView.canCancelContentTouches = false
        wv.scrollView.contentInsetAdjustmentBehavior = .never
        wv.scrollView.showsVerticalScrollIndicator = false
        wv.scrollView.showsHorizontalScrollIndicator = false
        self.webView = wv

        view.addSubview(wv)
        NSLayoutConstraint.activate([
            wv.topAnchor.constraint(equalTo: view.topAnchor),
            wv.bottomAnchor.constraint(equalTo: view.bottomAnchor),
            wv.leadingAnchor.constraint(equalTo: view.leadingAnchor),
            wv.trailingAnchor.constraint(equalTo: view.trailingAnchor),
        ])

        loadAppHTML()
    }

    private func loadAppHTML() {
        let htmlUrl = Bundle.main.url(forResource: "index", withExtension: "html")
            ?? Bundle.main.url(forResource: "index", withExtension: "html", subdirectory: "Resources")
        if let url = htmlUrl,
           let html = try? String(contentsOf: url, encoding: .utf8) {
            // Load with HTTPS baseURL so IndexedDB, localStorage, getUserMedia, and Google Drive APIs have a secure origin.
            webView.loadHTMLString(html, baseURL: URL(string: "https://goodnotespro.local"))
        } else {
            let fallback = "<html><body style='font-family:-apple-system;padding:40px;'><h2>GoodNotes Pro</h2><p>Unable to locate bundled index.html resource.</p></body></html>"
            webView.loadHTMLString(fallback, baseURL: nil)
        }
    }

    // MARK: - WKScriptMessageHandler

    func userContentController(_ userContentController: WKUserContentController, didReceive message: WKScriptMessage) {
        switch message.name {
        case "nativeShare":
            handleNativeShare(message.body)
        case "nativeHaptic":
            handleNativeHaptic(message.body)
        case "nativeOpenUrl":
            if let str = message.body as? String, let url = URL(string: str) {
                UIApplication.shared.open(url, options: [:], completionHandler: nil)
            }
        case "nativeRenderPdf":
            handleNativeRenderPdf(message.body)
        case "nativeTheme":
            if let dict = message.body as? [String: Any], let isDark = dict["dark"] as? Bool {
                darkStatusBar = isDark
                view.backgroundColor = isDark
                    ? UIColor(red: 15/255, green: 23/255, blue: 42/255, alpha: 1)
                    : UIColor(red: 245/255, green: 247/255, blue: 251/255, alpha: 1)
                setNeedsStatusBarAppearanceUpdate()
            }
        default:
            break
        }
    }

    private func handleNativeHaptic(_ body: Any) {
        let styleStr = (body as? String) ?? "light"
        if styleStr == "selection" {
            UISelectionFeedbackGenerator().selectionChanged()
        } else {
            let style: UIImpactFeedbackGenerator.FeedbackStyle = styleStr == "medium" ? .medium : .light
            let gen = UIImpactFeedbackGenerator(style: style)
            gen.impactOccurred()
        }
    }

    private func handleNativeShare(_ body: Any) {
        guard let dict = body as? [String: Any] else { return }
        let rawName = (dict["filename"] as? String) ?? "GoodNotesPro_Backup.goodnotes.json"
        let safeName = URL(fileURLWithPath: rawName).lastPathComponent
        let targetUrl = FileManager.default.temporaryDirectory.appendingPathComponent(safeName)

        var fileData: Data?
        if let base64 = dict["base64"] as? String, !base64.isEmpty {
            let cleaned = base64.components(separatedBy: ",").last ?? base64
            fileData = Data(base64Encoded: cleaned, options: .ignoreUnknownCharacters)
        } else if let text = dict["text"] as? String {
            fileData = text.data(using: .utf8)
        }

        guard let data = fileData else { return }
        do {
            try data.write(to: targetUrl, options: .atomic)
        } catch {
            return
        }

        let activityVC = UIActivityViewController(activityItems: [targetUrl], applicationActivities: nil)
        if let pop = activityVC.popoverPresentationController {
            pop.sourceView = self.view
            pop.sourceRect = CGRect(x: self.view.bounds.midX, y: 80, width: 1, height: 1)
            pop.permittedArrowDirections = [.up, .any]
        }
        present(activityVC, animated: true, completion: nil)
    }

    private func handleNativeRenderPdf(_ body: Any) {
        guard let dict = body as? [String: Any],
              let reqId = dict["requestId"] as? String,
              let base64 = dict["base64"] as? String else { return }
        let maxPages = (dict["maxPages"] as? Int) ?? 60

        DispatchQueue.global(qos: .userInitiated).async { [weak self] in
            let cleaned = base64.components(separatedBy: ",").last ?? base64
            guard let pdfData = Data(base64Encoded: cleaned, options: .ignoreUnknownCharacters),
                  let pdfDoc = PDFDocument(data: pdfData) else {
                self?.sendPdfCallback(reqId: reqId, payload: ["error": "Invalid or encrypted PDF data."])
                return
            }

            let count = min(pdfDoc.pageCount, maxPages)
            var pagesOut: [[String: Any]] = []
            pagesOut.reserveCapacity(count)

            for i in 0..<count {
                guard let page = pdfDoc.page(at: i) else { continue }
                let bounds = page.bounds(for: .mediaBox)
                let targetWidth: CGFloat = 1400.0
                let scale = max(1.0, min(2.5, targetWidth / max(1.0, bounds.width)))
                let renderSize = CGSize(width: bounds.width * scale, height: bounds.height * scale)

                let renderer = UIGraphicsImageRenderer(size: renderSize)
                let image = renderer.image { ctx in
                    UIColor.white.setFill()
                    ctx.fill(CGRect(origin: .zero, size: renderSize))
                    ctx.cgContext.translateBy(x: 0, y: renderSize.height)
                    ctx.cgContext.scaleBy(x: scale, y: -scale)
                    ctx.cgContext.translateBy(x: -bounds.origin.x, y: -bounds.origin.y)
                    page.draw(with: .mediaBox, to: ctx.cgContext)
                }

                if let jpegData = image.jpegData(compressionQuality: 0.84) {
                    let dataUrl = "data:image/jpeg;base64," + jpegData.base64EncodedString()
                    pagesOut.append([
                        "width": Int(bounds.width),
                        "height": Int(bounds.height),
                        "dataUrl": dataUrl
                    ])
                }
            }

            self?.sendPdfCallback(reqId: reqId, payload: [
                "totalPages": pdfDoc.pageCount,
                "renderedPages": pagesOut.count,
                "pages": pagesOut
            ])
        }
    }

    private func sendPdfCallback(reqId: String, payload: [String: Any]) {
        guard let jsonData = try? JSONSerialization.data(withJSONObject: payload, options: []),
              let jsonStr = String(data: jsonData, encoding: .utf8),
              let idData = try? JSONSerialization.data(withJSONObject: reqId, options: []),
              let idStr = String(data: idData, encoding: .utf8) else { return }

        DispatchQueue.main.async { [weak self] in
            let js = "window.__onNativePdfResult && window.__onNativePdfResult(\(idStr), \(jsonStr));"
            self?.webView.evaluateJavaScript(js, completionHandler: nil)
        }
    }

    // MARK: - WKUIDelegate

    @available(iOS 15.0, *)
    func webView(
        _ webView: WKWebView,
        requestMediaCapturePermissionFor origin: WKSecurityOrigin,
        initiatedByFrame frame: WKFrameInfo,
        type: WKMediaCaptureType,
        decisionHandler: @escaping (WKPermissionDecision) -> Void
    ) {
        decisionHandler(.grant)
    }

    func webView(
        _ webView: WKWebView,
        runJavaScriptAlertPanelWithMessage message: String,
        initiatedByFrame frame: WKFrameInfo,
        completionHandler: @escaping () -> Void
    ) {
        let alert = UIAlertController(title: "GoodNotes Pro", message: message, preferredStyle: .alert)
        alert.addAction(UIAlertAction(title: "OK", style: .default) { _ in completionHandler() })
        present(alert, animated: true)
    }

    func webView(
        _ webView: WKWebView,
        runJavaScriptConfirmPanelWithMessage message: String,
        initiatedByFrame frame: WKFrameInfo,
        completionHandler: @escaping (Bool) -> Void
    ) {
        let alert = UIAlertController(title: "GoodNotes Pro", message: message, preferredStyle: .alert)
        alert.addAction(UIAlertAction(title: "Cancel", style: .cancel) { _ in completionHandler(false) })
        alert.addAction(UIAlertAction(title: "OK", style: .default) { _ in completionHandler(true) })
        present(alert, animated: true)
    }

    func webView(
        _ webView: WKWebView,
        runJavaScriptTextInputPanelWithPrompt prompt: String,
        defaultText: String?,
        initiatedByFrame frame: WKFrameInfo,
        completionHandler: @escaping (String?) -> Void
    ) {
        let alert = UIAlertController(title: "GoodNotes Pro", message: prompt, preferredStyle: .alert)
        alert.addTextField { tf in tf.text = defaultText }
        alert.addAction(UIAlertAction(title: "Cancel", style: .cancel) { _ in completionHandler(nil) })
        alert.addAction(UIAlertAction(title: "OK", style: .default) { _ in
            completionHandler(alert.textFields?.first?.text)
        })
        present(alert, animated: true)
    }
}
