'use client';

import { useState, useRef, useEffect } from 'react';
import Link from 'next/link';
import Info from './info';
import AreteLogo from './AreteLogo';
import { sendChatMessageStream, sendFeedback } from '../lib/api';
import ReactMarkdown from 'react-markdown';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

// Preprocess LaTeX delimiters to markdown math delimiters
function preprocessMathDelimiters(text: string): string {
  // Replace block math delimiters: \[ ... \] -> $$ ... $$
  let processed = text.replace(/\\\[/g, '$$').replace(/\\\]/g, '$$');
  // Replace inline math delimiters: \( ... \) -> $ ... $
  processed = processed.replace(/\\\(/g, '$').replace(/\\\)/g, '$');
  return processed;
}

interface Message {
  text: string;
  sender: 'user' | 'assistant';
  messageId?: number;
  feedback?: 'Chosen' | 'Rejected' | null;
}

interface ChatInterfaceProps {
  course: string;
}

export default function ChatInterface({ course }: ChatInterfaceProps) {
  // Course name mapping: course code -> display name
  const courseNameMap: Record<string, string> = {
    'ml': 'Machine Learning',
    'sc': 'Supply Chain Management',
    'iot': 'Internet of Things',
  };

  // Get the display name for the course, fallback to original course if not found
  const courseDisplayName = courseNameMap[course] || course;

  const [messages, setMessages] = useState<Message[]>([
    {
      text: `Hi there! I'm Areté, how can I help you with ${courseDisplayName} today?`,
      sender: 'assistant',
      messageId: undefined,
      feedback: null,
    },
  ]);
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [isThinking, setIsThinking] = useState(false);
  const [sessionId, setSessionId] = useState<string | null>(null);
  const chatAreaRef = useRef<HTMLDivElement>(null);
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  useEffect(() => {
    // Scroll to bottom when messages change
    if (chatAreaRef.current) {
      chatAreaRef.current.scrollTop = chatAreaRef.current.scrollHeight;
    }
  }, [messages]);

  useEffect(() => {
    // Auto-resize textarea based on content
    if (textareaRef.current) {
      textareaRef.current.style.height = 'auto';
      const scrollHeight = textareaRef.current.scrollHeight;
      // Set max height to prevent it from growing too large (e.g., 6 lines)
      const maxHeight = 150; // approximately 6 lines
      textareaRef.current.style.height = `${Math.min(scrollHeight, maxHeight)}px`;
    }
  }, [inputValue]);

  useEffect(() => {
    // Auto-focus textarea when component mounts or when loading finishes
    if (!isLoading && textareaRef.current) {
      textareaRef.current.focus();
    }
  }, [isLoading]);

  const handleSendMessage = async () => {
    const message = inputValue.trim();
    if (!message || isLoading) return;

    // Add user message to chat
    const userMessage: Message = { text: message, sender: 'user' };
    setMessages((prev) => [...prev, userMessage]);
    setInputValue('');
    // Reset textarea height
    if (textareaRef.current) {
      textareaRef.current.style.height = 'auto';
    }
    setIsLoading(true);
    setIsThinking(true);
    
    let hasReceivedChunk = false;
    let accumulatedText = '';

    try {
      await sendChatMessageStream(
        message,
        sessionId,
        course,
        (chunk: string) => {
          // Add the assistant message on first chunk if it doesn't exist
          if (!hasReceivedChunk) {
            hasReceivedChunk = true;
            setIsThinking(false);
            accumulatedText = chunk;
            // Add the assistant message with the first chunk
            setMessages((prev) => [...prev, { 
              text: accumulatedText, 
              sender: 'assistant',
              messageId: undefined,
              feedback: null
            }]);
          } else {
            // Update the last message (assistant message) with accumulated chunks
            accumulatedText += chunk;
            setMessages((prev) => {
              const newMessages = [...prev];
              const lastMessage = newMessages[newMessages.length - 1];
              if (lastMessage && lastMessage.sender === 'assistant') {
                // Create a new message object to ensure React detects the change
                newMessages[newMessages.length - 1] = {
                  ...lastMessage,
                  text: accumulatedText,
                };
              }
              return newMessages;
            });
          }
        },
        (newSessionId: string) => {
          setSessionId(newSessionId);
        },
        (error: string) => {
          console.error('Streaming error:', error);
          setIsLoading(false);
          setIsThinking(false);
          // Add error message if we haven't received any chunks yet
          if (!hasReceivedChunk) {
            setMessages((prev) => [...prev, { 
              text: error || 'Sorry, an error occurred. Please try again.', 
              sender: 'assistant',
              messageId: undefined,
              feedback: null
            }]);
          } else {
            // Update existing message with error
            setMessages((prev) => {
              const newMessages = [...prev];
              const lastMessage = newMessages[newMessages.length - 1];
              if (lastMessage && lastMessage.sender === 'assistant') {
                lastMessage.text = error || 'Sorry, an error occurred. Please try again.';
              }
              return newMessages;
            });
          }
        },
        (recordId: number) => {
          // Update the last assistant message with the record ID
          setMessages((prev) => {
            const newMessages = [...prev];
            const lastMessage = newMessages[newMessages.length - 1];
            if (lastMessage && lastMessage.sender === 'assistant') {
              newMessages[newMessages.length - 1] = {
                ...lastMessage,
                messageId: recordId,
              };
            }
            return newMessages;
          });
        }
      );
    } catch (error) {
      console.error('Error:', error);
      setIsLoading(false);
      const errorText = error instanceof Error ? error.message : 'Sorry, an error occurred. Please try again.';
      // Only add error message if we haven't received any chunks
      if (!hasReceivedChunk) {
        setMessages((prev) => [...prev, { 
          text: errorText, 
          sender: 'assistant',
          messageId: undefined,
          feedback: null
        }]);
      } else {
        // Update existing message with error
        setMessages((prev) => {
          const newMessages = [...prev];
          const lastMessage = newMessages[newMessages.length - 1];
          if (lastMessage && lastMessage.sender === 'assistant') {
            lastMessage.text = errorText;
          }
          return newMessages;
        });
      }
    } finally {
      setIsLoading(false);
      setIsThinking(false);
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSendMessage();
    }
  };

  const handleFeedback = async (messageIndex: number, feedback: 'Chosen' | 'Rejected') => {
    const message = messages[messageIndex];
    if (!message || message.sender !== 'assistant' || !message.messageId) {
      return;
    }

    try {
      await sendFeedback(message.messageId, feedback);
      // Update the message with the feedback
      setMessages((prev) => {
        const newMessages = [...prev];
        newMessages[messageIndex] = {
          ...newMessages[messageIndex],
          feedback: feedback,
        };
        return newMessages;
      });
    } catch (error) {
      console.error('Failed to send feedback:', error);
    }
  };

  return (
    <div className="relative flex h-screen items-center justify-center bg-white">
      {/* Logo - Top Left */}
      <div className="absolute top-5 left-5 flex flex-col">
        <Link 
          href="/" 
          className="flex items-center gap-2 hover:opacity-70 transition-opacity cursor-pointer"
        >
          <AreteLogo className="w-12 h-12" />
          <span className="text-xl font-light tracking-wide text-black">Areté</span>
        </Link>
        <span className="text-xs font-bold text-gray-600 ml-14 font-serif tracking-tight -mt-2">
          {courseDisplayName}
        </span>
      </div>
      {/* CBS Logo - Top Right */}
      <div className="absolute top-5 right-5 flex items-center">
        <a 
          href="https://www.cbs.dk/en/research/departments/department-digitalisation" 
          target="_blank" 
          rel="noopener noreferrer"
          className="hover:opacity-70 transition-opacity"
        >
          <img 
            src="/cbs_logo.png" 
            alt="Copenhagen Business School" 
            className="h-8"
          />
        </a>
      </div>
      <div className="flex h-[98vh] w-[90%] max-w-4xl flex-col overflow-hidden bg-white border border-gray-300 shadow-[4px_4px_8px_rgba(0,0,0,0.15),-2px_-2px_4px_rgba(255,255,255,0.8)]">
        {/* Chat Area */}
        <div
          ref={chatAreaRef}
          className="flex-1 overflow-y-auto bg-white p-5"
        >
          <div className="space-y-4">
            {messages.map((message, index) => (
              <div
                key={index}
                className={`flex flex-col ${
                  message.sender === 'user' ? 'items-end' : 'items-start'
                }`}
              >
                <div
                  className={`px-4 py-3 ${
                    message.sender === 'user'
                      ? 'max-w-[70%] rounded-2xl bg-white border-2 border-blue-700 text-gray-800'
                      : 'max-w-full text-gray-800'
                  }`}
                >
                  {message.sender === 'assistant' ? (
                    <div className="prose prose-sm max-w-none break-words">
                      <ReactMarkdown
                        remarkPlugins={[remarkMath]}
                        rehypePlugins={[rehypeKatex]}
                        components={{
                          // Style code blocks
                          code: ({ node, className, children, ...props }: any) => {
                            const isInline = !className || !className.includes('language-');
                            return isInline ? (
                              <code className="bg-gray-100 px-1.5 py-0.5 rounded text-sm font-mono text-gray-800" {...props}>
                                {children}
                              </code>
                            ) : (
                              <code className="block bg-gray-100 p-3 rounded-lg text-sm font-mono text-gray-800 overflow-x-auto" {...props}>
                                {children}
                              </code>
                            );
                          },
                          // Style pre blocks
                          pre: ({ node, children, ...props }) => {
                            return (
                              <pre className="bg-gray-100 p-3 rounded-lg overflow-x-auto my-2" {...props}>
                                {children}
                              </pre>
                            );
                          },
                          // Style headings
                          h1: ({ node, children, ...props }) => (
                            <h1 className="text-2xl font-bold mt-4 mb-2 text-gray-900" {...props}>
                              {children}
                            </h1>
                          ),
                          h2: ({ node, children, ...props }) => (
                            <h2 className="text-xl font-bold mt-3 mb-2 text-gray-900" {...props}>
                              {children}
                            </h2>
                          ),
                          h3: ({ node, children, ...props }) => (
                            <h3 className="text-lg font-semibold mt-3 mb-2 text-gray-900" {...props}>
                              {children}
                            </h3>
                          ),
                          // Style lists
                          ul: ({ node, children, ...props }) => (
                            <ul className="list-disc list-inside my-2 space-y-1" {...props}>
                              {children}
                            </ul>
                          ),
                          ol: ({ node, children, ...props }) => (
                            <ol className="list-decimal list-outside my-2 space-y-1 pl-6" {...props}>
                              {children}
                            </ol>
                          ),
                          li: ({ node, children, ...props }) => (
                            <li className="my-1" {...props}>
                              {children}
                            </li>
                          ),
                          // Style links
                          a: ({ node, children, ...props }) => (
                            <a className="text-blue-600 hover:text-blue-800 underline" {...props}>
                              {children}
                            </a>
                          ),
                          // Style blockquotes
                          blockquote: ({ node, children, ...props }) => (
                            <blockquote className="border-l-4 border-gray-300 pl-4 my-2 italic text-gray-700" {...props}>
                              {children}
                            </blockquote>
                          ),
                          // Style paragraphs
                          p: ({ node, children, ...props }) => (
                            <p className="my-2" {...props}>
                              {children}
                            </p>
                          ),
                          // Style strong/bold
                          strong: ({ node, children, ...props }) => (
                            <strong className="font-bold text-gray-900" {...props}>
                              {children}
                            </strong>
                          ),
                          // Style emphasis/italic
                          em: ({ node, children, ...props }) => (
                            <em className="italic" {...props}>
                              {children}
                            </em>
                          ),
                        }}
                      >
                        {preprocessMathDelimiters(message.text)}
                      </ReactMarkdown>
                    </div>
                  ) : (
                    <p className="break-words whitespace-pre-wrap">
                      {message.text}
                    </p>
                  )}
                </div>
                {message.sender === 'assistant' && message.messageId && (
                  <div className="flex gap-1 mt-1 ml-4">
                    <button
                      onClick={() => handleFeedback(index, 'Chosen')}
                      disabled={message.feedback === 'Chosen'}
                      className={`p-1 rounded transition-colors ${
                        message.feedback === 'Chosen'
                          ? 'text-green-600'
                          : 'text-gray-400 hover:text-green-600'
                      }`}
                      title="Like"
                    >
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        viewBox="0 0 24 24"
                        fill="none"
                        stroke="currentColor"
                        strokeWidth="2.5"
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        className="w-4 h-4"
                      >
                        <path d="M20 6L9 17l-5-5" />
                      </svg>
                    </button>
                    <button
                      onClick={() => handleFeedback(index, 'Rejected')}
                      disabled={message.feedback === 'Rejected'}
                      className={`p-1 rounded transition-colors ${
                        message.feedback === 'Rejected'
                          ? 'text-red-600'
                          : 'text-gray-400 hover:text-red-600'
                      }`}
                      title="Dislike"
                    >
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        viewBox="0 0 24 24"
                        fill="none"
                        stroke="currentColor"
                        strokeWidth="2.5"
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        className="w-4 h-4"
                      >
                        <path d="M18 6L6 18" />
                        <path d="M6 6l12 12" />
                      </svg>
                    </button>
                  </div>
                )}
              </div>
            ))}
            {isThinking && (
              <div className="flex justify-start">
                <div className="bg-white rounded-2xl px-4 py-3 shadow-md">
                  <div className="flex items-center space-x-2">
                    <div className="h-5 w-5 animate-spin rounded-full border-4 border-primary-500 border-t-transparent"></div>
                    <span className="text-gray-500">Thinking...</span>
                  </div>
                </div>
              </div>
            )}
          </div>
        </div>

        {/* Input Area */}
        <div className="border-t border-white bg-white p-5 overflow-visible">
          <div className="flex gap-3 items-end overflow-visible">
            <textarea
              ref={textareaRef}
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
              onKeyDown={handleKeyPress}
              placeholder="Type your message here..."
              rows={1}
              className="flex-1 rounded-2xl border-2 border-gray-200 px-4 py-3 text-[15px] leading-[1.5] outline-none transition-colors focus:border-blue-700 resize-none overflow-hidden"
              style={{ minHeight: '48px', maxHeight: '150px' }}
              autoComplete="off"
            />
            <button
              onClick={handleSendMessage}
              disabled={isLoading || !inputValue.trim()}
              className="rounded-full bg-transparent px-4 py-3 transition-all hover:-translate-y-0.5 hover:shadow-lg active:translate-y-0 disabled:cursor-not-allowed disabled:opacity-60 disabled:transform-none flex-shrink-0 flex items-center justify-center group"
              style={{ height: 'fit-content', minWidth: '56px' }}
            >
              {isLoading ? (
                <div className="h-5 w-5 animate-spin rounded-full border-2 border-blue-700 border-t-transparent"></div>
              ) : (
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="2.5"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  className="w-6 h-6 text-blue-700 group-hover:text-pink-500 transition-colors"
                >
                  <line x1="12" y1="19" x2="12" y2="5"></line>
                  <polyline points="5 12 12 5 19 12"></polyline>
                </svg>
              )}
            </button>
          </div>
          {/* Disclaimer */}
          <div className="mt-2 text-xs text-gray-500 opacity-70 text-center" style={{ marginLeft: 'clamp(-70px, calc(-3.5vw - 25px), -30px)' }}>
          This tool supports learning, not final answers. Review, evaluate and verify the responses critically.
          </div>
        </div>
      </div>

      <Info />
    </div>
  );
}

