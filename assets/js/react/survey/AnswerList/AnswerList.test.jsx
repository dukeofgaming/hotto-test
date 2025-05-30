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
      const modal = screen.getByRole("dialog", { name: /answers/i });
      expect(modal).toBeInTheDocument();

      // Only count answer rows (not header)
      const allRows = screen.getAllByRole("row");
      const answerRows = allRows.filter(row => row.getAttribute("aria-label") === "answer");
      expect(answerRows.length).toBe(2);

      expect(answerRows[0]).toHaveTextContent("How old are you?");
      expect(answerRows[0]).toHaveTextContent("text");

      const textInput = screen.getByRole("textbox", { name: /answer value/i });
      expect(textInput).toBeInTheDocument();
      expect(textInput.value).toBe("42");

      expect(answerRows[1]).toHaveTextContent("Do you smoke?");
      expect(answerRows[1]).toHaveTextContent("boolean");

      const boolInput = screen.getByRole("checkbox", { name: /answer value/i });
      expect(boolInput).toBeInTheDocument();
      expect(boolInput.checked).toBe(true);

      // Act
      fireEvent.click(screen.getByRole("button", { name: /close/i }));

      // Assert
      expect(onClose).toHaveBeenCalled();
    });
  });
});
