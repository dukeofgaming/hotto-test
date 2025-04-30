import React from "react";
import { render, screen } from "@testing-library/react";
import Answer from "./Answer";

describe("Given a question and answer", () => {
  describe("When rendering the component", () => {
    it("Then should render a table row with question text, type, and delegate to AnswerValue", () => {
      // Arrange
      const question = { id: "q1", question_text: "How old are you?", type: "text", is_clinical: false };
      const answer = { id: "a1", question_id: "q1", value: "42" };
      // Act
      render(
        <table><tbody><Answer question={question} answer={answer} /></tbody></table>
      );
      // Assert
      const row = screen.getByTestId("answer-row");
      expect(row).toBeInTheDocument();
      expect(row).toHaveTextContent("How old are you?");
      expect(row).toHaveTextContent("text");
      const input = screen.getByTestId("text-answer-value");
      expect(input.value).toBe("42");
    });
  });
});
