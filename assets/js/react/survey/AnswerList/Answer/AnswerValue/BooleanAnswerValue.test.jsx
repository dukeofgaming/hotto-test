import React from "react";
import { render, screen } from "@testing-library/react";
import BooleanAnswerValue from "./BooleanAnswerValue";

describe("Given a true-like value", () => {
  describe("When rendering the component", () => {
    it("Then should render a checked checkbox", () => {
      // Arrange
      const value = "yes";
      // Act
      render(<BooleanAnswerValue value={value} />);
      // Assert
      const checkbox = screen.getByTestId("boolean-answer-value");
      expect(checkbox).toBeInTheDocument();
      expect(checkbox.checked).toBe(true);
    });
  });
});

describe("Given a false-like value", () => {
  describe("When rendering the component", () => {
    it("Then should render an unchecked checkbox", () => {
      // Arrange
      const value = "no";
      // Act
      render(<BooleanAnswerValue value={value} />);
      // Assert
      const checkbox = screen.getByTestId("boolean-answer-value");
      expect(checkbox).toBeInTheDocument();
      expect(checkbox.checked).toBe(false);
    });
  });
});
