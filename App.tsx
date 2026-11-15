import React from 'react';
import { KeyboardAvoidingView, Platform, SafeAreaView, StyleSheet } from 'react-native';
import { StatusBar } from 'expo-status-bar';
import { WebView } from 'react-native-webview';
import { INTERVIEW_APP_HTML } from './src/htmlBundle';

/**
 * Root iPad/Tablet component hosting the self-contained
 * Oxbridge Mathematics Whiteboard & Gemini Live Auto-Hint Interviewer.
 */
export default function App() {
  return (
    <SafeAreaView style={styles.container}>
      <StatusBar style="light" />
      <KeyboardAvoidingView
        style={styles.flex}
        behavior={Platform.OS === 'ios' ? 'padding' : undefined}
      >
        <WebView
          originWhitelist={['*']}
          source={{
            html: INTERVIEW_APP_HTML,
            baseUrl: 'https://oxbridge.local',
          }}
          style={styles.webview}
          javaScriptEnabled
          domStorageEnabled
          allowsInlineMediaPlayback
          bounces={false}
          scrollEnabled={false}
          overScrollMode="never"
          contentInsetAdjustmentBehavior="never"
          allowsBackForwardNavigationGestures={false}
          sharedCookiesEnabled
        />
      </KeyboardAvoidingView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#0d1321',
  },
  flex: {
    flex: 1,
  },
  webview: {
    flex: 1,
    backgroundColor: '#0d1321',
  },
});
