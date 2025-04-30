import React from "react";
import { render, screen, fireEvent } from "@testing-library/react";
import AnswerList from "./AnswerList";

describe("Given AnswerList is rendered", () => {
  describe("When answers and questions are provided", () => {
    it("Then it displays a table of answers with question text and type, and calls onClose when close is clicked", () => {
      // Arrange
      const answers = [
        { id: "a1", submission_id: "s1", question_id: "q1", value: "42" },
        { id: "a2", submission_id: "s1", question_id: "q2", value: "yes" }
      ];
      const questions = [
        { id: "q1", question_text: "How old are you?", type: "text", is_clinical: false },
        { id: "q2", question_text: "Do you smoke?", type: "boolean", is_clinical: true }
      ];
      const onClose = jest.fn();
      // Act
      render(<AnswerList answers={answers} questions={questions} onClose={onClose} />);
      // Assert
      const modal = screen.getByTestId("answer-list-modal");
      expect(modal).toBeInTheDocument();
      const rows = screen.getAllByTestId("answer-row");
      expect(rows.length).toBe(2);
      expect(rows[0]).toHaveTextContent("How old are you?");
      expect(rows[0]).toHaveTextContent("text");
      // Check input value for text answer
      const textInput = screen.getByTestId("text-answer-value");
      expect(textInput).toBeInTheDocument();
      expect(textInput.value).toBe("42");
      expect(rows[1]).toHaveTextContent("Do you smoke?");
      expect(rows[1]).toHaveTextContent("boolean");
      // Check input value for boolean answer
      const boolInput = screen.getByTestId("boolean-answer-value");
      expect(boolInput).toBeInTheDocument();
      expect(boolInput.checked).toBe(true);
      // Act
      fireEvent.click(screen.getByTestId("close-btn"));
      // Assert
      expect(onClose).toHaveBeenCalled();
    });
  });
});
