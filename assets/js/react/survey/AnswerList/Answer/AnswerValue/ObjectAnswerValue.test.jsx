import React from "react";
import { render, screen } from "@testing-library/react";
import ObjectAnswerValue from "./ObjectAnswerValue";

describe("Given a valid object", () => {
  describe("When rendering the component", () => {
    it("Then should render a table with key-value pairs", () => {
      // Arrange
      const value = { foo: "bar", baz: 1 };
      // Act
      render(<ObjectAnswerValue value={value} />);
      // Assert
      const table = screen.getByTestId("object-answer-value");
      expect(table).toBeInTheDocument();
      expect(table).toHaveTextContent("foo");
      expect(table).toHaveTextContent("bar");
      expect(table).toHaveTextContent("baz");
      expect(table).toHaveTextContent("1");
    });
  });
});

describe("Given a non-object value", () => {
  describe("When rendering the component", () => {
    it("Then should render Invalid object", () => {
      // Arrange
      const value = "not-an-object";
      // Act
      render(<ObjectAnswerValue value={value} />);
      // Assert
      expect(screen.getByTestId("object-answer-value")).toHaveTextContent("Invalid object");
    });
  });
});
