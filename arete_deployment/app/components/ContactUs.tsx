'use client';

import { useState, useRef, useEffect } from 'react';

export default function ContactUs() {
  const [isOpen, setIsOpen] = useState(false);
  const menuRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const handleClickOutside = (event: MouseEvent) => {
      if (menuRef.current && !menuRef.current.contains(event.target as Node)) {
        setIsOpen(false);
      }
    };

    if (isOpen) {
      document.addEventListener('mousedown', handleClickOutside);
    }

    return () => {
      document.removeEventListener('mousedown', handleClickOutside);
    };
  }, [isOpen]);

  const contactLinks = [
    {
      label: 'kok.digi@cbs.dk',
      href: 'mailto:kok.digi@cbs.dk',
      icon: (
        <svg
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          strokeWidth="1.8"
          className="h-4 w-4 text-gray-600"
        >
          <rect x="3" y="5" width="18" height="14" rx="2" ry="2" />
          <polyline points="4 6 12 12 20 6" />
        </svg>
      ),
    },
    {
      label: 'GitHub',
      href: 'https://github.com/your-username',
      icon: (
        <svg
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 24 24"
          fill="currentColor"
          className="h-4 w-4 text-gray-600"
        >
          <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
        </svg>
      ),
    },
  ];

  return (
    <div className="absolute bottom-0 left-0 p-6">
      <div className="relative" ref={menuRef}>
        <button
          onClick={() => setIsOpen(!isOpen)}
          className="flex items-center justify-center h-10 w-10 rounded-full bg-white border-2 border-gray-300 hover:border-black transition-colors duration-200"
          title="Feedback & Contact"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2"
            className="h-5 w-5 text-gray-600"
          >
            <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" />
          </svg>
        </button>
        
        {isOpen && (
          <div className="absolute bottom-full left-0 mb-2 w-52 bg-white border border-gray-300 rounded-lg shadow-lg z-50" style={{ maxWidth: 'calc(100vw - 3rem)' }}>
            <div className="p-4 space-y-3">
              <a
                href="https://docs.google.com/forms/d/e/1FAIpQLSdHIDmSth0DYO5t-UzWWVfupGbnApevJYuk1Xp0JSGvk7yeug/viewform?usp=dialog"
                target="_blank"
                rel="noopener noreferrer"
                className="flex items-center gap-3 text-gray-700 hover:text-blue-700 transition-colors duration-200 text-sm"
              >
                <div className="flex items-center justify-center h-7 w-7 rounded-full bg-gray-100 border border-gray-300 flex-shrink-0">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    strokeWidth="2"
                    className="h-4 w-4 text-gray-600"
                  >
                    <path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                </div>
                <span>Help us Improve</span>
              </a>
              {contactLinks.map((link, index) => (
                <a
                  key={index}
                  href={link.href}
                  target={link.href.startsWith('mailto:') ? undefined : '_blank'}
                  rel={link.href.startsWith('mailto:') ? undefined : 'noopener noreferrer'}
                  className="flex items-center gap-3 text-gray-700 hover:text-blue-700 transition-colors duration-200 text-sm pt-2 border-t border-gray-200"
                >
                  <div className="flex items-center justify-center h-7 w-7 rounded-full bg-gray-100 border border-gray-300 flex-shrink-0">
                    {link.icon}
                  </div>
                  <span>{link.label}</span>
                </a>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

