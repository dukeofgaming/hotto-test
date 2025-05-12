import React from "react";
import { render, screen } from "@testing-library/react";
import BooleanAnswerValue from "./BooleanAnswerValue";

describe("Given BooleanAnswerValue is rendered", () => {
  describe("When type is boolean", () => {
    it("Then should render a readonly checkbox (checked, ARIA)", () => {
      // Arrange
      const value = true;
      // Act
      render(<BooleanAnswerValue value={value} />);
      // Assert
      const checkbox = screen.getByRole("checkbox", { name: /answer value/i });
      expect(checkbox).toBeInTheDocument();
      expect(checkbox.checked).toBe(true);
    });
    it("Then should render a readonly checkbox (unchecked, ARIA)", () => {
      // Arrange
      const value = false;
      // Act
      render(<BooleanAnswerValue value={value} />);
      // Assert
      const checkbox = screen.getByRole("checkbox", { name: /answer value/i });
      expect(checkbox).toBeInTheDocument();
      expect(checkbox.checked).toBe(false);
    });
  });
});
