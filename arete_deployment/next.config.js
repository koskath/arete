/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  // Allow cross-origin requests from network devices in development only
  ...(process.env.NODE_ENV === 'development' && {
    experimental: {
      allowedDevOrigins: ['172.18.0.191'], // Add your network IP(s) here for dev
    },
  }),
  async rewrites() {
    return [
      // /api/chat/stream is handled by the Next.js API route
    ];
  },
};

module.exports = nextConfig;

