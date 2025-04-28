module.exports = {
  roots: ['<rootDir>/assets/js/react'],
  testMatch: ['**/*.test.jsx'],
  transform: {
    '^.+\\.[jt]sx?$': 'babel-jest',
  },
  setupFilesAfterEnv: ['@testing-library/jest-dom'],
  moduleFileExtensions: ['js', 'jsx'],
  testEnvironment: 'jsdom',
};
