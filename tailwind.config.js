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
  // Best practice: Use literal Tailwind class names in your React code.
  // Avoid dynamic class name generation (e.g., `shadow-${level}`) unless you add all possible values to the safelist.
  // The content array below covers all .js, .jsx, .ts, .tsx, and .html files in your project where Tailwind classes may appear.
  // The safelist is now empty, as all classes should be detected by the content scan.
  safelist: [],
  plugins: [],
}
