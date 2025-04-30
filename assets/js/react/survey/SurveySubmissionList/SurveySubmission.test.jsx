import React from "react";
import { render, screen, fireEvent } from "@testing-library/react";
import SurveySubmission from "./SurveySubmission";

describe("Given SurveySubmission is rendered", () => {
  describe("When a submission is provided", () => {
    it("Then it renders the submission data", () => {
      // Arrange
      const submission = {
        submission_id: "s1",
        form_id: "intake",
        patient_id: "p1",
        submitted_at: 1714430000
      };
      // Act
      render(<table><tbody><SurveySubmission submission={submission} onView={() => {}} /></tbody></table>);
      // Assert
      const row = screen.getByTestId("survey-submission-row");
      expect(row).toBeInTheDocument();
      expect(row).toHaveTextContent("s1");
      expect(row).toHaveTextContent("intake");
      expect(row).toHaveTextContent("p1");
      expect(row).toHaveTextContent("1714430000");
    });
  });

  describe("When the 'View' button is clicked", () => {
    it("Then it calls onView with the correct id", () => {
      // Arrange
      const submission = {
        submission_id: "s1",
        form_id: "intake",
        patient_id: "p1",
        submitted_at: 1714430000
      };
      const onView = jest.fn();
      render(<table><tbody><SurveySubmission submission={submission} onView={onView} /></tbody></table>);
      const viewBtn = screen.getByTestId("view-btn");
      // Act
      fireEvent.click(viewBtn);
      // Assert
      expect(onView).toHaveBeenCalledWith("s1");
    });
  });
});
