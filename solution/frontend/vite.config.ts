import { defineConfig } from 'vite'
import tailwindcss from '@tailwindcss/vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [ tailwindcss(), react()],
  // test: {
  //   globals: true,
  //   environment: "jsdom",  // Simula un navegador para pruebas de React
  //   setupFiles: "./setupTests.ts",
  // },
})
