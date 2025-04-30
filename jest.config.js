module.exports = {
  roots: ['<rootDir>/assets/js/react'],
  testMatch: ['**/*.test.jsx'],
  transform: {
    '^.+\\.[jt]sx?$': 'babel-jest',
  },
  setupFiles: [
    './setupJest.js',
  ],
  setupFilesAfterEnv: ['@testing-library/jest-dom'],
  moduleFileExtensions: ['js', 'jsx'],
  testEnvironment: 'jsdom',
};
