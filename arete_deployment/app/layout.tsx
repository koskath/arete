import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'Areté',
  description: 'AI Chat Bot Interface',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}

