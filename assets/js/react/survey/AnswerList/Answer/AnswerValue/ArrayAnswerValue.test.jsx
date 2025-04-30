import React from "react";
import { render, screen } from "@testing-library/react";
import ArrayAnswerValue from "./ArrayAnswerValue";

describe("Given a valid array", () => {
  describe("When rendering the component", () => {
    it("Then should render an unordered list of items", () => {
      // Arrange
      const value = [1, 2, 3];
      // Act
      render(<ArrayAnswerValue value={value} />);
      // Assert
      const ul = screen.getByTestId("array-answer-value");
      expect(ul).toBeInTheDocument();
      expect(ul).toHaveTextContent("1");
      expect(ul).toHaveTextContent("2");
      expect(ul).toHaveTextContent("3");
    });
  });
});

describe("Given a non-array value", () => {
  describe("When rendering the component", () => {
    it("Then should render Invalid array", () => {
      // Arrange
      const value = "not-an-array";
      // Act
      render(<ArrayAnswerValue value={value} />);
      // Assert
      expect(screen.getByTestId("array-answer-value")).toHaveTextContent("Invalid array");
    });
  });
});
