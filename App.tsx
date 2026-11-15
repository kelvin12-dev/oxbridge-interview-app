import React from 'react';
import { KeyboardAvoidingView, Platform, SafeAreaView, StyleSheet } from 'react-native';
import { StatusBar } from 'expo-status-bar';
import { WebView } from 'react-native-webview';
import { GOODNOTES_PRO_HTML } from './src/htmlBundle';

/**
 * Root iPad/iOS component hosting GoodNotes Pro.
 */
export default function App() {
  return (
    <SafeAreaView style={styles.container}>
      <StatusBar style="auto" />
      <KeyboardAvoidingView
        style={styles.flex}
        behavior={Platform.OS === 'ios' ? 'padding' : undefined}
      >
        <WebView
          originWhitelist={['*']}
          source={{
            html: GOODNOTES_PRO_HTML,
            baseUrl: 'https://goodnotespro.local',
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
    backgroundColor: '#f5f7fb',
  },
  flex: {
    flex: 1,
  },
  webview: {
    flex: 1,
    backgroundColor: '#f5f7fb',
  },
});
