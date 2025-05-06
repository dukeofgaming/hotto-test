module.exports = {
  content: [
    "./assets/js/react/**/*.{js,jsx,ts,tsx}",
    "./assets/js/react/**/**/*.{js,jsx,ts,tsx}",
    "./templates/**/*.html",
    "./**/*.html",
    "./**/*.{js,jsx,ts,tsx}"
  ],
  theme: {
    colors: {
      primary: {
        DEFAULT: "#4B4662",
        500: "#4B4662"
      },
      secondary: {
        DEFAULT: "#FF6F4C",
        500: "#FF6F4C"
      },
      white: { DEFAULT: "#fff", 500: "#fff" },
      black: { DEFAULT: "#000", 500: "#000" },
    },
    extend: {
      fontFamily: {
        serif: ["Georgia", "serif"],
        sans: ["Inter", "Helvetica", "Arial", "sans-serif"],
      }
    },
  },
  safelist: [
    'bg-primary',
    'bg-primary-500',
    'bg-secondary',
    'bg-secondary-500',
    'text-white',
    '!text-white',
    'font-sans',
    'min-h-screen',
    'table-auto',
    'mx-auto',
    'align-middle',
    'whitespace-nowrap',
  ],
  plugins: [],
}
