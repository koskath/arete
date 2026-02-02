export interface ChatMessage {
  message: string;
  session_id?: string | null;
  course?: string;
}

export interface StreamChunk {
  type: 'session_id' | 'chunk' | 'done' | 'error';
  session_id?: string;
  content?: string;
  error?: string;
  record_id?: number;
}

// Use Next.js API proxy to avoid CORS issues
const API_BASE_URL = '/api';

export async function sendChatMessageStream(
  message: string,
  sessionId: string | null,
  course: string,
  onChunk: (chunk: string) => void,
  onSessionId: (sessionId: string) => void,
  onError: (error: string) => void,
  onRecordId?: (recordId: number) => void
): Promise<string> {
  const response = await fetch(`${API_BASE_URL}/chat/stream`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      message,
      session_id: sessionId,
      course: course,
    }),
  });

  if (!response.ok) {
    let errorMessage = 'Failed to get response';
    try {
      const errorData = await response.json();
      errorMessage = errorData.detail || errorData.message || errorMessage;
    } catch {
      errorMessage = response.statusText || errorMessage;
    }
    throw new Error(errorMessage);
  }

  const reader = response.body?.getReader();
  const decoder = new TextDecoder();
  let buffer = '';
  let fullResponse = '';

  if (!reader) {
    throw new Error('Response body is not readable');
  }

  while (true) {
    const { done, value } = await reader.read();
    if (done) break;

    buffer += decoder.decode(value, { stream: true });
    
    // SSE format: "data: {json}\n\n"
    // Split by double newline to get complete events
    const events = buffer.split('\n\n');
    // Keep the last incomplete event in buffer
    buffer = events.pop() || '';

    for (const event of events) {
      if (!event.trim()) continue;
      
      // Find the data line
      const lines = event.split('\n');
      for (const line of lines) {
        if (line.startsWith('data: ')) {
          try {
            const jsonStr = line.slice(6); // Remove "data: " prefix
            const data: StreamChunk = JSON.parse(jsonStr);
            
            if (data.type === 'session_id' && data.session_id) {
              onSessionId(data.session_id);
            } else if (data.type === 'chunk' && data.content !== undefined) {
              fullResponse += data.content;
              onChunk(data.content);
            } else if (data.type === 'done') {
              if (data.record_id !== undefined && onRecordId) {
                onRecordId(data.record_id);
              }
              return fullResponse;
            } else if (data.type === 'error' && data.error) {
              onError(data.error);
              throw new Error(data.error);
            }
          } catch (e) {
            // Skip invalid JSON
            console.warn('Failed to parse SSE data:', line, e);
          }
        }
      }
    }
  }
  
  // Handle any remaining buffer
  if (buffer.trim()) {
    const lines = buffer.split('\n');
    for (const line of lines) {
      if (line.startsWith('data: ')) {
        try {
          const jsonStr = line.slice(6);
          const data: StreamChunk = JSON.parse(jsonStr);
          if (data.type === 'chunk' && data.content !== undefined) {
            fullResponse += data.content;
            onChunk(data.content);
          }
        } catch (e) {
          // Ignore parse errors
        }
      }
    }
  }

  return fullResponse;
}

export async function sendFeedback(recordId: number, feedback: 'Chosen' | 'Rejected'): Promise<void> {
  const response = await fetch(`${API_BASE_URL}/chat/feedback`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      record_id: recordId,
      feedback: feedback,
    }),
  });

  if (!response.ok) {
    let errorMessage = 'Failed to update feedback';
    try {
      const errorData = await response.json();
      errorMessage = errorData.detail || errorData.message || errorMessage;
    } catch {
      errorMessage = response.statusText || errorMessage;
    }
    throw new Error(errorMessage);
  }
}

