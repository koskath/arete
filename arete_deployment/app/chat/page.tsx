'use client';

import { useSearchParams } from 'next/navigation';
import { Suspense } from 'react';
import ChatInterface from '../components/ChatInterface';

function ChatPageContent() {
  const searchParams = useSearchParams();
  const course = searchParams.get('course') || 'ml';

  return <ChatInterface course={course} />;
}

export default function ChatPage() {
  return (
    <Suspense fallback={<div className="flex h-screen items-center justify-center">Loading...</div>}>
      <ChatPageContent />
    </Suspense>
  );
}

