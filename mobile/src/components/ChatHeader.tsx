import React from 'react';
import { StyleSheet, View, Text } from 'react-native';
import MaterialIcons from 'react-native-vector-icons/MaterialIcons';

export default function ChatHeader(): React.JSX.Element {
  return (
    <View style={styles.container}>
      <View style={styles.content}>
        <MaterialIcons name="smart-toy" size={24} color="#007AFF" />
        <View style={styles.textContainer}>
          <Text style={styles.title}>Claude Code</Text>
          <Text style={styles.subtitle}>AI Assistant</Text>
        </View>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    paddingHorizontal: 16,
    paddingVertical: 12,
    backgroundColor: '#f5f5f5',
    borderBottomWidth: 1,
    borderBottomColor: '#e0e0e0',
  },
  content: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  textContainer: {
    marginLeft: 12,
  },
  title: {
    fontSize: 18,
    fontWeight: '600',
    color: '#000',
  },
  subtitle: {
    fontSize: 12,
    color: '#666',
    marginTop: 2,
  },
});
