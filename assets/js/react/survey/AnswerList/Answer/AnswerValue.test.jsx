import React from "react";
import { render, screen } from "@testing-library/react";
import AnswerValue from "./AnswerValue";

describe("Given AnswerValue is rendered", () => {
  describe("When type is text", () => {
    it("Then should render a readonly text input", () => {
      // Arrange
      const type = "text";
      const value = "hello";
      // Act
      render(<AnswerValue value={value} type={type} />);
      // Assert
      const input = screen.getByTestId("text-answer-value");
      expect(input).toBeInTheDocument();
      expect(input).toHaveAttribute("readonly");
      expect(input.value).toBe(value);
    });
  });

  describe("When type is date", () => {
    it("Then should render a readonly date input", () => {
      // Arrange
      const type = "date";
      const value = "2023-01-01";
      // Act
      render(<AnswerValue value={value} type={type} />);
      // Assert
      const input = screen.getByTestId("date-answer-value");
      expect(input).toBeInTheDocument();
      expect(input).toHaveAttribute("readonly");
      expect(input.value).toBe(value);
    });
  });

  describe("When type is boolean", () => {
    it("Then should render a readonly checkbox (checked)", () => {
      // Arrange
      const type = "boolean";
      const value = "Yes";
      // Act
      render(<AnswerValue value={value} type={type} />);
      // Assert
      const checkbox = screen.getByTestId("boolean-answer-value");
      expect(checkbox).toBeInTheDocument();
      expect(checkbox.checked).toBe(true);
    });
    it("Then should render a readonly checkbox (unchecked)", () => {
      // Arrange
      const type = "boolean";
      const value = "No";
      // Act
      render(<AnswerValue value={value} type={type} />);
      // Assert
      const checkbox = screen.getByTestId("boolean-answer-value");
      expect(checkbox).toBeInTheDocument();
      expect(checkbox.checked).toBe(false);
    });
  });

  describe("When type is object", () => {
    it("Then should render a table with key-value pairs", () => {
      // Arrange
      const type = "object";
      const value = { foo: "bar", baz: 1 };
      // Act
      render(<AnswerValue value={value} type={type} />);
      // Assert
      const table = screen.getByTestId("object-answer-value");
      expect(table).toBeInTheDocument();
      expect(table).toHaveTextContent("foo");
      expect(table).toHaveTextContent("bar");
      expect(table).toHaveTextContent("baz");
      expect(table).toHaveTextContent("1");
    });
    it("Then should render Invalid object for non-object", () => {
      // Arrange
      const type = "object";
      const value = "not-an-object";
      // Act
      render(<AnswerValue value={value} type={type} />);
      // Assert
      expect(screen.getByTestId("object-answer-value")).toHaveTextContent("Invalid object");
    });
  });

  describe("When type is array", () => {
    it("Then should render an unordered list of items", () => {
      // Arrange
      const type = "array";
      const value = [1, 2, 3];
      // Act
      render(<AnswerValue value={value} type={type} />);
      // Assert
      const ul = screen.getByTestId("array-answer-value");
      expect(ul).toBeInTheDocument();
      expect(ul).toHaveTextContent("1");
      expect(ul).toHaveTextContent("2");
      expect(ul).toHaveTextContent("3");
    });
    it("Then should render Invalid array for non-array", () => {
      // Arrange
      const type = "array";
      const value = "not-an-array";
      // Act
      render(<AnswerValue value={value} type={type} />);
      // Assert
      expect(screen.getByTestId("array-answer-value")).toHaveTextContent("Invalid array");
    });
  });

  describe("When given an unknown type", () => {
    it("Then should render the value as a string and log a warning", () => {
      // Arrange
      const type = "unknown";
      const value = 42;
      const consoleSpy = jest.spyOn(console, "log").mockImplementation(() => {});
      // Act
      render(<AnswerValue type={type} value={value} />);
      // Assert
      expect(screen.getByText(String(value))).toBeInTheDocument();
      expect(consoleSpy).toHaveBeenCalledWith(
        expect.stringContaining("Unknown answer type"),
        type,
        value
      );
      consoleSpy.mockRestore();
    });
  });
});
