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
          DEFAULT: "#f45b5b",
          dark: "#3d364a",
        }
      },
      fontFamily: {
        serif: ["Georgia", "serif"],
        sans: ["Inter", "Helvetica", "Arial", "sans-serif"],
      }
    },
  },
  plugins: [],
}
