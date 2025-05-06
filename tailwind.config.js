module.exports = {
  content: [
    "./assets/js/react/**/*.{js,jsx,ts,tsx}",
    "./assets/js/react/**/**/*.{js,jsx,ts,tsx}",
    "./templates/**/*.html",
    "./**/*.html",
    "./**/*.{js,jsx,ts,tsx}"
  ],
  theme: {
    extend: {
      colors: {
        hotto: {
          DEFAULT: "#4B4662",
          dark: "#3d364a",
        },
        primary: "#4B4662",
        "primary-light": "#A78BFA",
        "primary-dark": "#4C1D95",
      },
      fontFamily: {
        serif: ["Georgia", "serif"],
        sans: ["Inter", "Helvetica", "Arial", "sans-serif"],
      }
    },
  },
  safelist: [
    'bg-[#FFFAF7]',
    'bg-[#7C3AED]',
    'bg-primary',
    'bg-primary-dark',
    'bg-primary-light',
    'font-sans',
    'min-h-screen',
    'text-white',
  ],
  plugins: [],
}
