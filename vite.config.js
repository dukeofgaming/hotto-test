import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import { resolve } from 'path';

export default defineConfig({
  root: 'assets/js/react',
  plugins: [react()],
  build: {
    outDir: '../../../static/react', // or another static dir for Flask
    emptyOutDir: true,
    manifest: true, // Enable manifest for hashed filenames
  },
  resolve: {
    alias: {
      '@': resolve(__dirname, 'assets/js/react'),
    },
  },
});
