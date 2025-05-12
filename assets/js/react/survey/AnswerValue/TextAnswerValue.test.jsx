import React from "react";
import { render, screen } from "@testing-library/react";
import TextAnswerValue from "./TextAnswerValue";

describe("Given TextAnswerValue is rendered", () => {
  describe("When given a valid text value", () => {
    it("Then should render a readonly text input with the correct value (ARIA)", () => {
      // Arrange
      const value = "hello";
      // Act
      render(<TextAnswerValue value={value} />);
      // Assert
      const input = screen.getByRole("textbox", { name: /answer value/i });
      expect(input).toBeInTheDocument();
      expect(input).toHaveAttribute("readonly");
      expect(input.value).toBe("hello");
    });
  });
});
