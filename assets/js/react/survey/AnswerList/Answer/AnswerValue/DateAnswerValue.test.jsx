import React from "react";
import { render, screen } from "@testing-library/react";
import DateAnswerValue from "./DateAnswerValue";

describe("Given DateAnswerValue is rendered", () => {
  describe("When given a valid date string", () => {
    it("Then should render a readonly date input with the correct value", () => {
      // Arrange
      const value = "2023-01-01";
      // Act
      render(<DateAnswerValue value={value} />);
      // Assert
      const input = screen.getByTestId("date-answer-value");
      expect(input).toBeInTheDocument();
      expect(input).toHaveAttribute("readonly");
      expect(input.value).toBe("2023-01-01");
    });
  });
});
