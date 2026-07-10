'use client';

import { useRouter } from 'next/navigation';
import AreteLogo from './components/AreteLogo';
import Info from './components/info';

export default function Home() {
  const router = useRouter();

  const handleCourseSelection = (course: string) => {
    router.push(`/chat?course=${course}`);
  };

  return (
    <div className="relative flex h-screen items-center justify-center bg-white">
      <Info />

      <div className="flex flex-col items-center justify-center w-full max-w-2xl px-6">
        {/* Header */}
        <header className="mb-16 text-center">
          <a
            href="https://github.com/koskath/arete"
            target="_blank"
            rel="noopener noreferrer"
            className="inline-block hover:opacity-70 transition-opacity cursor-pointer"
          >
            <div className="flex justify-center mb-2 -mt-8">
              <AreteLogo className="w-44 h-44" />
            </div>
            <h1 className="text-3xl font-light tracking-wide text-black">
              AI Research Ecosystem for Teaching Experiment 
            </h1>
          </a>
        </header>

        {/* Course Selection Options */}
        <div className="flex flex-col gap-6 w-full mb-16">
          <button
            onClick={() => handleCourseSelection('ml')}
            className="px-8 py-6 rounded-lg border-2 border-gray-300 bg-white text-black hover:bg-white hover:border-black transition-all duration-200 text-xl font-medium shadow-md hover:shadow-lg"
          >
            Machine Learning
          </button>
          <button
            onClick={() => handleCourseSelection('sc')}
            className="px-8 py-6 rounded-lg border-2 border-gray-300 bg-white text-black hover:bg-white hover:border-black transition-all duration-200 text-xl font-medium shadow-md hover:shadow-lg"
          >
            Supply Chain Management
          </button>
          <button
            onClick={() => handleCourseSelection('iot')}
            className="px-8 py-6 rounded-lg border-2 border-gray-300 bg-white text-black hover:bg-white hover:border-black transition-all duration-200 text-xl font-medium shadow-md hover:shadow-lg"
          >
            Internet of Things
          </button>
        </div>

        {/* Footer */}
        <footer className="mt-auto text-center -mt-8">
          <a 
            href="https://www.cbs.dk/en/research/departments/department-digitalisation" 
            target="_blank" 
            rel="noopener noreferrer"
            className="hover:opacity-70 transition-opacity"
          >
            <img 
              src="/cbs_logo.png" 
              alt="Copenhagen Business School" 
              className="h-7 mx-auto"
            />
          </a>
        </footer>
      </div>
    </div>
  );
}
