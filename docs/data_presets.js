// GoodNotes Pro - Presets, Templates, Covers, Stickers, Starter Library & Google Drive Script
window.GN_PRESETS = (function () {
  const COVERS = [
    { id: 'cobalt', name: 'Goodnotes Cobalt', bg: 'linear-gradient(145deg, #1d4ed8, #0284c7)', accent: '#38bdf8', textColor: '#ffffff', pattern: 'spine' },
    { id: 'minimal', name: 'Ivory Minimalist', bg: 'linear-gradient(145deg, #fafaf9, #e7e5e4)', accent: '#0f172a', textColor: '#0f172a', pattern: 'border' },
    { id: 'leather', name: 'Classic Navy Leather', bg: 'linear-gradient(145deg, #0f172a, #1e3a5f)', accent: '#f59e0b', textColor: '#f8fafc', pattern: 'stitch' },
    { id: 'pastel_sage', name: 'Pastel Sage', bg: 'linear-gradient(145deg, #d1fae5, #a7f3d0)', accent: '#065f46', textColor: '#064e3b', pattern: 'band' },
    { id: 'botanical', name: 'Botanical Emerald', bg: 'linear-gradient(145deg, #065f46, #047857)', accent: '#a7f3d0', textColor: '#ffffff', pattern: 'leaf' },
    { id: 'academic', name: 'Oxford Crimson', bg: 'linear-gradient(145deg, #881337, #be123c)', accent: '#fde68a', textColor: '#ffffff', pattern: 'spine' },
    { id: 'geometric', name: 'Bauhaus Grid', bg: 'linear-gradient(145deg, #312e81, #4f46e5)', accent: '#fbbf24', textColor: '#ffffff', pattern: 'grid' },
    { id: 'kraft', name: 'Warm Kraft Paper', bg: 'linear-gradient(145deg, #d6b88d, #b89263)', accent: '#451a03', textColor: '#291505', pattern: 'stitch' },
    { id: 'dark_pro', name: 'Midnight Obsidian', bg: 'linear-gradient(145deg, #111827, #1f2937)', accent: '#60a5fa', textColor: '#f9fafb', pattern: 'band' },
    { id: 'neon_cyber', name: 'Electric Violet', bg: 'linear-gradient(145deg, #581c87, #7c3aed)', accent: '#22d3ee', textColor: '#ffffff', pattern: 'grid' },
    { id: 'cornell_blue', name: 'Cornell Sky', bg: 'linear-gradient(145deg, #0ea5e9, #38bdf8)', accent: '#ffffff', textColor: '#ffffff', pattern: 'band' },
    { id: 'rose_gold', name: 'Blush Quartz', bg: 'linear-gradient(145deg, #fda4af, #fb7185)', accent: '#881337', textColor: '#4c0519', pattern: 'border' },
  ];

  const PAPER_COLORS = [
    { id: 'white', name: 'Pure White', bg: '#ffffff', line: '#dbe4f0', margin: '#fda4af', inkDefault: '#0f172a', muted: '#64748b' },
    { id: 'cream', name: 'Goodnotes Cream', bg: '#fdf8ee', line: '#e6d8be', margin: '#f4a29e', inkDefault: '#1e293b', muted: '#78716c' },
    { id: 'dark', name: 'Dark Charcoal', bg: '#181c24', line: '#2d3545', margin: '#be123c', inkDefault: '#f1f5f9', muted: '#94a3b8' },
    { id: 'sage', name: 'Sage Green', bg: '#eff6f0', line: '#c6dcc9', margin: '#86efac', inkDefault: '#143326', muted: '#4d7c64' },
    { id: 'rose', name: 'Rose Tint', bg: '#fdf2f4', line: '#eccdd4', margin: '#fb7185', inkDefault: '#3b1620', muted: '#9f465c' },
    { id: 'blueprint', name: 'Blueprint Blue', bg: '#0d2b52', line: '#1e4b85', margin: '#38bdf8', inkDefault: '#e0f2fe', muted: '#7dd3fc' },
  ];

  const PAGE_SIZES = [
    { id: 'goodnotes', name: 'Goodnotes Standard', w: 960, h: 1242 },
    { id: 'a4', name: 'A4 (210 × 297 mm)', w: 960, h: 1358 },
    { id: 'a5', name: 'A5 (148 × 210 mm)', w: 840, h: 1188 },
    { id: 'letter', name: 'US Letter', w: 960, h: 1242 },
  ];

  const TEMPLATES = [
    { id: 'blank', name: 'Blank Paper', cat: 'Essentials' },
    { id: 'ruled_narrow', name: 'Ruled Narrow', cat: 'Essentials' },
    { id: 'ruled_wide', name: 'Ruled Wide', cat: 'Essentials' },
    { id: 'cornell', name: 'Cornell Notes', cat: 'Essentials' },
    { id: 'grid_5mm', name: 'Squared Grid', cat: 'Essentials' },
    { id: 'dotted', name: 'Dotted Grid', cat: 'Essentials' },
    { id: 'isometric', name: 'Isometric Grid', cat: 'Essentials' },
    { id: 'legal', name: 'Legal Pad', cat: 'Essentials' },
    { id: 'monthly', name: 'Monthly Planner', cat: 'Planners' },
    { id: 'weekly', name: 'Weekly Planner', cat: 'Planners' },
    { id: 'daily', name: 'Daily Schedule', cat: 'Planners' },
    { id: 'todo', name: 'To-Do Checklist', cat: 'Planners' },
    { id: 'accounting', name: 'Accounting Ledger', cat: 'Planners' },
    { id: 'columnar', name: '3-Column Study', cat: 'Planners' },
    { id: 'music', name: 'Music Grand Staff', cat: 'Specialized' },
    { id: 'guitar', name: 'Guitar Tablature', cat: 'Specialized' },
    { id: 'hex', name: 'Hex Chemistry', cat: 'Specialized' },
    { id: 'axes', name: 'Coordinate x-y Axes', cat: 'Specialized' },
  ];

  const FOLDER_COLORS = [
    { id: 'blue', name: 'Goodnotes Blue', hex: '#0284c7', light: '#e0f2fe' },
    { id: 'indigo', name: 'Indigo', hex: '#4f46e5', light: '#e0e7ff' },
    { id: 'emerald', name: 'Emerald', hex: '#059669', light: '#d1fae5' },
    { id: 'amber', name: 'Amber', hex: '#d97706', light: '#fef3c7' },
    { id: 'rose', name: 'Rose', hex: '#e11d48', light: '#ffe4e6' },
    { id: 'purple', name: 'Violet', hex: '#7c3aed', light: '#ede9fe' },
    { id: 'teal', name: 'Teal', hex: '#0d9488', light: '#ccfbf1' },
    { id: 'coral', name: 'Coral', hex: '#ea580c', light: '#ffedd5' },
    { id: 'slate', name: 'Charcoal', hex: '#334155', light: '#f1f5f9' },
    { id: 'pink', name: 'Magenta', hex: '#db2777', light: '#fce7f3' },
  ];

  const PEN_PALETTE = [
    '#0f172a', '#1d4ed8', '#dc2626', '#059669',
    '#7c3aed', '#ea580c', '#0891b2', '#ffffff'
  ];

  const HIGHLIGHTER_PALETTE = [
    '#fde047', '#86efac', '#7dd3fc', '#f9a8d4', '#d8b4fe', '#fdba74'
  ];

  const TAPE_STYLES = [
    { id: 'amber_washi', name: 'Amber Washi', color: '#f59e0b', stripe: '#fbbf24' },
    { id: 'sky_dots', name: 'Sky Dots', color: '#0ea5e9', stripe: '#38bdf8' },
    { id: 'mint_recall', name: 'Mint Recall', color: '#10b981', stripe: '#34d399' },
    { id: 'rose_cover', name: 'Rose Cover', color: '#f43f5e', stripe: '#fb7185' },
    { id: 'dark_mask', name: 'Charcoal Mask', color: '#334155', stripe: '#475569' },
  ];

  function svgToDataUrl(svg) {
    return 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svg.trim());
  }

  const BUILT_IN_ELEMENTS = [
    // Sticky Notes
    {
      id: 'el_sticky_yellow',
      category: 'Sticky Notes',
      name: 'Yellow Sticky',
      w: 220,
      h: 220,
      src: svgToDataUrl(`<svg xmlns="http://www.w3.org/2000/svg" width="220" height="220" viewBox="0 0 220 220">
        <defs><filter id="s"><feDropShadow dx="0" dy="4" stdDeviation="4" flood-opacity="0.18"/></filter></defs>
        <path d="M8,6 H212 V186 L186,212 H8 Z" fill="#fef08a" stroke="#eab308" stroke-width="2" filter="url(#s)"/>
        <path d="M186,212 V186 H212 Z" fill="#fde047" stroke="#eab308" stroke-width="1.5"/>
        <rect x="8" y="6" width="204" height="24" fill="#fde047" opacity="0.7"/>
        <line x1="22" y1="62" x2="196" y2="62" stroke="#ca8a04" stroke-opacity="0.3" stroke-width="1.5"/>
        <line x1="22" y1="96" x2="196" y2="96" stroke="#ca8a04" stroke-opacity="0.3" stroke-width="1.5"/>
        <line x1="22" y1="130" x2="196" y2="130" stroke="#ca8a04" stroke-opacity="0.3" stroke-width="1.5"/>
        <line x1="22" y1="164" x2="196" y2="164" stroke="#ca8a04" stroke-opacity="0.3" stroke-width="1.5"/>
      </svg>`)
    },
    {
      id: 'el_sticky_pink',
      category: 'Sticky Notes',
      name: 'Rose Sticky',
      w: 220,
      h: 220,
      src: svgToDataUrl(`<svg xmlns="http://www.w3.org/2000/svg" width="220" height="220" viewBox="0 0 220 220">
        <path d="M8,6 H212 V186 L186,212 H8 Z" fill="#fbcfe8" stroke="#ec4899" stroke-width="2"/>
        <path d="M186,212 V186 H212 Z" fill="#f9a8d4" stroke="#ec4899" stroke-width="1.5"/>
        <rect x="8" y="6" width="204" height="24" fill="#f9a8d4" opacity="0.65"/>
        <line x1="22" y1="62" x2="196" y2="62" stroke="#db2777" stroke-opacity="0.25" stroke-width="1.5"/>
        <line x1="22" y1="96" x2="196" y2="96" stroke="#db2777" stroke-opacity="0.25" stroke-width="1.5"/>
        <line x1="22" y1="130" x2="196" y2="130" stroke="#db2777" stroke-opacity="0.25" stroke-width="1.5"/>
        <line x1="22" y1="164" x2="196" y2="164" stroke="#db2777" stroke-opacity="0.25" stroke-width="1.5"/>
      </svg>`)
    },
    {
      id: 'el_sticky_blue',
      category: 'Sticky Notes',
      name: 'Sky Grid Note',
      w: 220,
      h: 220,
      src: svgToDataUrl(`<svg xmlns="http://www.w3.org/2000/svg" width="220" height="220" viewBox="0 0 220 220">
        <rect x="8" y="8" width="204" height="204" rx="10" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>
        <g stroke="#0284c7" stroke-opacity="0.18" stroke-width="1">
          <line x1="40" y1="16" x2="40" y2="204"/><line x1="72" y1="16" x2="72" y2="204"/>
          <line x1="104" y1="16" x2="104" y2="204"/><line x1="136" y1="16" x2="136" y2="204"/>
          <line x1="168" y1="16" x2="168" y2="204"/>
          <line x1="16" y1="40" x2="204" y2="40"/><line x1="16" y1="72" x2="204" y2="72"/>
          <line x1="16" y1="104" x2="204" y2="104"/><line x1="16" y1="136" x2="204" y2="136"/>
          <line x1="16" y1="168" x2="204" y2="168"/>
        </g>
      </svg>`)
    },
    {
      id: 'el_sticky_mint',
      category: 'Sticky Notes',
      name: 'Mint Summary Box',
      w: 250,
      h: 160,
      src: svgToDataUrl(`<svg xmlns="http://www.w3.org/2000/svg" width="250" height="160" viewBox="0 0 250 160">
        <rect x="6" y="6" width="238" height="148" rx="14" fill="#d1fae5" stroke="#059669" stroke-width="2.5"/>
        <rect x="6" y="6" width="238" height="32" rx="12" fill="#10b981"/>
        <text x="20" y="27" font-family="-apple-system,sans-serif" font-size="14" font-weight="700" fill="#ffffff">KEY TAKEAWAY</text>
      </svg>`)
    },

    // Study Stamps
    {
      id: 'el_stamp_important',
      category: 'Study Stamps',
      name: 'IMPORTANT!',
      w: 190,
      h: 64,
      src: svgToDataUrl(`<svg xmlns="http://www.w3.org/2000/svg" width="190" height="64" viewBox="0 0 190 64">
        <rect x="4" y="4" width="182" height="56" rx="14" fill="#ffe4e6" stroke="#e11d48" stroke-width="3"/>
        <text x="95" y="39" text-anchor="middle" font-family="-apple-system,sans-serif" font-size="20" font-weight="800" fill="#be123c">IMPORTANT!</text>
      </svg>`)
    },
    {
      id: 'el_stamp_exam',
      category: 'Study Stamps',
      name: 'EXAM TIP',
      w: 180,
      h: 64,
      src: svgToDataUrl(`<svg xmlns="http://www.w3.org/2000/svg" width="180" height="64" viewBox="0 0 180 64">
        <rect x="4" y="4" width="172" height="56" rx="14" fill="#fef3c7" stroke="#d97706" stroke-width="3"/>
        <text x="90" y="39" text-anchor="middle" font-family="-apple-system,sans-serif" font-size="20" font-weight="800" fill="#b45309">EXAM TIP ★</text>
      </svg>`)
    },
    {
      id: 'el_stamp_definition',
      category: 'Study Stamps',
      name: 'DEFINITION',
      w: 190,
      h: 64,
      src: svgToDataUrl(`<svg xmlns="http://www.w3.org/2000/svg" width="190" height="64" viewBox="0 0 190 64">
        <rect x="4" y="4" width="182" height="56" rx="14" fill="#dbeafe" stroke="#2563eb" stroke-width="3"/>
        <text x="95" y="39" text-anchor="middle" font-family="-apple-system,sans-serif" font-size="19" font-weight="800" fill="#1d4ed8">DEFINITION</text>
      </svg>`)
    },
    {
      id: 'el_stamp_check',
      category: 'Study Stamps',
      name: 'Verified Check',
      w: 96,
      h: 96,
      src: svgToDataUrl(`<svg xmlns="http://www.w3.org/2000/svg" width="96" height="96" viewBox="0 0 96 96">
        <circle cx="48" cy="48" r="42" fill="#d1fae5" stroke="#059669" stroke-width="5"/>
        <polyline points="28,49 42,63 69,34" fill="none" stroke="#059669" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>`)
    },

    // STEM Diagrams
    {
      id: 'el_stem_unit_circle',
      category: 'STEM Diagrams',
      name: 'Unit Circle',
      w: 220,
      h: 220,
      src: svgToDataUrl(`<svg xmlns="http://www.w3.org/2000/svg" width="220" height="220" viewBox="0 0 220 220">
        <rect width="220" height="220" rx="12" fill="#ffffff" fill-opacity="0.88" stroke="#cbd5e1"/>
        <line x1="16" y1="110" x2="204" y2="110" stroke="#64748b" stroke-width="2"/>
        <line x1="110" y1="16" x2="110" y2="204" stroke="#64748b" stroke-width="2"/>
        <circle cx="110" cy="110" r="72" fill="none" stroke="#1d4ed8" stroke-width="3"/>
        <line x1="110" y1="110" x2="161" y2="59" stroke="#e11d48" stroke-width="2.5"/>
        <line x1="161" y1="59" x2="161" y2="110" stroke="#059669" stroke-dasharray="4 3" stroke-width="2"/>
        <circle cx="161" cy="59" r="4.5" fill="#e11d48"/>
        <text x="166" y="54" font-family="serif" font-size="13" fill="#0f172a">(cos θ, sin θ)</text>
        <text x="192" y="104" font-family="serif" font-size="13" fill="#475569">x</text>
        <text x="116" y="26" font-family="serif" font-size="13" fill="#475569">y</text>
      </svg>`)
    },
    {
      id: 'el_stem_bell',
      category: 'STEM Diagrams',
      name: 'Normal Curve',
      w: 260,
      h: 160,
      src: svgToDataUrl(`<svg xmlns="http://www.w3.org/2000/svg" width="260" height="160" viewBox="0 0 260 160">
        <rect width="260" height="160" rx="12" fill="#ffffff" fill-opacity="0.88" stroke="#cbd5e1"/>
        <line x1="18" y1="130" x2="242" y2="130" stroke="#475569" stroke-width="2"/>
        <path d="M22,128 C60,126 88,30 130,30 C172,30 200,126 238,128" fill="#bfdbfe" fill-opacity="0.55" stroke="#1d4ed8" stroke-width="3"/>
        <line x1="130" y1="24" x2="130" y2="135" stroke="#e11d48" stroke-dasharray="4 3" stroke-width="2"/>
        <text x="130" y="149" text-anchor="middle" font-family="serif" font-size="14" fill="#0f172a">μ</text>
      </svg>`)
    },
    {
      id: 'el_stem_benzene',
      category: 'STEM Diagrams',
      name: 'Benzene Ring',
      w: 170,
      h: 170,
      src: svgToDataUrl(`<svg xmlns="http://www.w3.org/2000/svg" width="170" height="170" viewBox="0 0 170 170">
        <polygon points="85,20 141,52 141,118 85,150 29,118 29,52" fill="none" stroke="#0f172a" stroke-width="4" stroke-linejoin="round"/>
        <circle cx="85" cy="85" r="34" fill="none" stroke="#0f172a" stroke-width="3" stroke-dasharray="10 6"/>
      </svg>`)
    },
    {
      id: 'el_stem_venn',
      category: 'STEM Diagrams',
      name: 'Venn Diagram',
      w: 240,
      h: 160,
      src: svgToDataUrl(`<svg xmlns="http://www.w3.org/2000/svg" width="240" height="160" viewBox="0 0 240 160">
        <circle cx="92" cy="80" r="56" fill="#3b82f6" fill-opacity="0.22" stroke="#2563eb" stroke-width="3"/>
        <circle cx="148" cy="80" r="56" fill="#ec4899" fill-opacity="0.22" stroke="#db2777" stroke-width="3"/>
        <text x="65" y="85" font-family="-apple-system,sans-serif" font-weight="700" font-size="16" fill="#1e3a8a">A</text>
        <text x="166" y="85" font-family="-apple-system,sans-serif" font-weight="700" font-size="16" fill="#831843">B</text>
      </svg>`)
    }
  ];

  function createStarterData() {
    const now = Date.now();
    return {
      folders: [
        { id: 'fld_stem', name: 'University & STEM', parentId: null, color: '#0284c7', icon: '📐', starred: true, createdAt: now - 86400000 },
        { id: 'fld_plan', name: 'Planners & Personal', parentId: null, color: '#ea580c', icon: '🗓️', starred: false, createdAt: now - 72000000 },
      ],
      notebooks: [
        {
          id: 'nb_welcome',
          title: 'Welcome to GoodNotes Pro',
          folderId: null,
          coverId: 'cobalt',
          paperColorId: 'white',
          sizeId: 'goodnotes',
          orientation: 'portrait',
          starred: true,
          trashed: false,
          createdAt: now - 3600000,
          updatedAt: now - 100000,
          outlines: [
            { id: 'out_1', title: '1. Zero-Delay Ink & Tools Overview', pageIndex: 0 },
            { id: 'out_2', title: '2. Cornell Study & Graph Axes', pageIndex: 1 },
          ],
          audioClips: [],
          pages: [
            {
              id: 'pg_w1',
              templateId: 'dotted',
              paperColorId: 'white',
              bookmarked: true,
              rotation: 0,
              pdfBg: null,
              strokes: [
                {
                  id: 'st_demo_hl',
                  tool: 'highlighter',
                  penType: 'highlighter',
                  color: '#fde047',
                  width: 24,
                  opacity: 0.42,
                  points: [
                    { x: 96, y: 150, p: 0.5 }, { x: 260, y: 150, p: 0.5 }, { x: 440, y: 150, p: 0.5 }, { x: 615, y: 150, p: 0.5 }
                  ]
                },
                {
                  id: 'st_demo_curve',
                  tool: 'pen',
                  penType: 'fountain',
                  color: '#1d4ed8',
                  width: 3.8,
                  opacity: 1,
                  points: [
                    { x: 110, y: 420, p: 0.4 }, { x: 170, y: 365, p: 0.65 }, { x: 245, y: 410, p: 0.78 },
                    { x: 325, y: 350, p: 0.85 }, { x: 410, y: 398, p: 0.72 }, { x: 495, y: 345, p: 0.55 }
                  ]
                }
              ],
              tapes: [
                {
                  id: 'tp_demo_1',
                  x: 115,
                  y: 590,
                  w: 390,
                  h: 42,
                  styleId: 'amber_washi',
                  revealed: false
                }
              ],
              texts: [
                {
                  id: 'tx_demo_1',
                  x: 92,
                  y: 118,
                  w: 620,
                  text: 'GoodNotes Pro — Zero-Delay Apple Pencil Studio',
                  fontSize: 28,
                  fontFamily: '-apple-system, BlinkMacSystemFont, sans-serif',
                  color: '#0f172a',
                  bg: 'transparent',
                  bold: true,
                  align: 'left'
                },
                {
                  id: 'tx_demo_2',
                  x: 96,
                  y: 196,
                  w: 760,
                  text: '• Fountain / Ball / Brush Pen with 240Hz coalesced input & Draw-and-Hold Shapes\n• Scribble to Erase & Circle to Lasso gestures\n• Study Tape below (tap the amber strip with Read Mode or Tape Tool to reveal!):\n\nEuler’s Identity:    e^(iπ) + 1 = 0',
                  fontSize: 19,
                  fontFamily: '-apple-system, BlinkMacSystemFont, sans-serif',
                  color: '#334155',
                  bg: 'transparent',
                  bold: false,
                  align: 'left'
                }
              ],
              elements: [
                {
                  id: 'el_inst_1',
                  x: 610,
                  y: 340,
                  w: 220,
                  h: 220,
                  rotation: -4,
                  src: BUILT_IN_ELEMENTS[0].src,
                  name: 'Yellow Sticky'
                }
              ]
            },
            {
              id: 'pg_w2',
              templateId: 'cornell',
              paperColorId: 'cream',
              bookmarked: false,
              rotation: 0,
              pdfBg: null,
              strokes: [],
              tapes: [],
              texts: [
                {
                  id: 'tx_demo_3',
                  x: 265,
                  y: 78,
                  w: 600,
                  text: 'Cornell Notes Template — Summary & Cues',
                  fontSize: 24,
                  fontFamily: '-apple-system, BlinkMacSystemFont, sans-serif',
                  color: '#1e293b',
                  bg: 'transparent',
                  bold: true,
                  align: 'left'
                }
              ],
              elements: []
            }
          ]
        },
        {
          id: 'nb_calc',
          title: 'Calculus & Linear Algebra',
          folderId: 'fld_stem',
          coverId: 'academic',
          paperColorId: 'white',
          sizeId: 'a4',
          orientation: 'portrait',
          starred: true,
          trashed: false,
          createdAt: now - 5400000,
          updatedAt: now - 500000,
          outlines: [
            { id: 'out_c1', title: 'Integration by Parts & Taylor Series', pageIndex: 0 }
          ],
          audioClips: [],
          pages: [
            {
              id: 'pg_c1',
              templateId: 'axes',
              paperColorId: 'white',
              bookmarked: true,
              rotation: 0,
              pdfBg: null,
              strokes: [],
              tapes: [],
              texts: [
                {
                  id: 'tx_c1',
                  x: 72,
                  y: 68,
                  w: 580,
                  text: 'Graph Sketching & Integration Workbench',
                  fontSize: 24,
                  fontFamily: '-apple-system, BlinkMacSystemFont, sans-serif',
                  color: '#0f172a',
                  bg: 'transparent',
                  bold: true,
                  align: 'left'
                }
              ],
              elements: []
            }
          ]
        },
        {
          id: 'nb_planner',
          title: '2026 Weekly Study Planner',
          folderId: 'fld_plan',
          coverId: 'pastel_sage',
          paperColorId: 'cream',
          sizeId: 'goodnotes',
          orientation: 'portrait',
          starred: false,
          trashed: false,
          createdAt: now - 7000000,
          updatedAt: now - 900000,
          outlines: [],
          audioClips: [],
          pages: [
            {
              id: 'pg_p1',
              templateId: 'weekly',
              paperColorId: 'cream',
              bookmarked: false,
              rotation: 0,
              pdfBg: null,
              strokes: [],
              tapes: [],
              texts: [],
              elements: []
            }
          ]
        }
      ],
      studySets: [
        {
          id: 'ss_calc',
          title: 'Calculus & Complex Analysis Deck',
          folderId: 'fld_stem',
          color: '#4f46e5',
          createdAt: now - 4000000,
          cards: [
            { id: 'fc_1', front: 'State Euler’s Formula for e^(iθ).', back: 'e^(iθ) = cos(θ) + i·sin(θ)', status: 'new', nextReview: now },
            { id: 'fc_2', front: 'Integration by Parts Formula', back: '∫ u dv = uv − ∫ v du', status: 'learning', nextReview: now },
            { id: 'fc_3', front: 'Taylor Series of e^x around x = 0', back: 'Σ (x^n / n!) for n = 0 to ∞', status: 'mastered', nextReview: now },
            { id: 'fc_4', front: 'Cauchy-Schwarz Inequality', back: '|⟨u, v⟩| ≤ ‖u‖ · ‖v‖', status: 'new', nextReview: now },
          ]
        }
      ],
      customElements: [],
      trash: []
    };
  }

  const GOOGLE_APPS_SCRIPT_TEMPLATE = `// Paste into https://script.google.com > New Project > Deploy as Web App (Anyone)
function doPost(e) {
  var folderName = "GoodNotesPro_Backups";
  var folders = DriveApp.getFoldersByName(folderName);
  var folder = folders.hasNext() ? folders.next() : DriveApp.createFolder(folderName);
  var data = JSON.parse(e.postData.contents);
  var filename = data.filename || "GoodNotesPro_Backup.goodnotes.json";
  var files = folder.getFilesByName(filename);
  if (files.hasNext() && data.overwrite !== false) {
    var existing = files.next();
    existing.setContent(data.content);
    return ContentService.createTextOutput(JSON.stringify({ ok: true, id: existing.getId(), name: filename, updatedAt: new Date().toISOString() })).setMimeType(ContentService.MimeType.JSON);
  }
  var file = folder.createFile(filename, data.content, MimeType.PLAIN_TEXT);
  return ContentService.createTextOutput(JSON.stringify({ ok: true, id: file.getId(), name: filename, updatedAt: new Date().toISOString() })).setMimeType(ContentService.MimeType.JSON);
}

function doGet(e) {
  var folderName = "GoodNotesPro_Backups";
  var folders = DriveApp.getFoldersByName(folderName);
  if (!folders.hasNext()) return ContentService.createTextOutput(JSON.stringify({ ok: true, files: [] })).setMimeType(ContentService.MimeType.JSON);
  var folder = folders.next();
  var action = (e && e.parameter && e.parameter.action) || "list";
  if (action === "get" && e.parameter.id) {
    var file = DriveApp.getFileById(e.parameter.id);
    return ContentService.createTextOutput(JSON.stringify({ ok: true, content: file.getBlob().getDataAsString() })).setMimeType(ContentService.MimeType.JSON);
  }
  var out = [];
  var files = folder.getFiles();
  while (files.hasNext()) {
    var f = files.next();
    out.push({ id: f.getId(), name: f.getName(), size: f.getSize(), modifiedTime: f.getLastUpdated().toISOString() });
  }
  return ContentService.createTextOutput(JSON.stringify({ ok: true, files: out })).setMimeType(ContentService.MimeType.JSON);
}`;

  return {
    COVERS,
    PAPER_COLORS,
    PAGE_SIZES,
    TEMPLATES,
    FOLDER_COLORS,
    PEN_PALETTE,
    HIGHLIGHTER_PALETTE,
    TAPE_STYLES,
    BUILT_IN_ELEMENTS,
    createStarterData,
    GOOGLE_APPS_SCRIPT_TEMPLATE
  };
})();
