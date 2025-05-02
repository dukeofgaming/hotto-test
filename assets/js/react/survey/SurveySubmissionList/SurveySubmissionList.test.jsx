import React from "react";
import { render, screen, fireEvent } from "@testing-library/react";
import SurveySubmissionList from "./SurveySubmissionList";

describe("Given SurveySubmissionList is rendered", () => {
  describe("When a list of submissions is provided", () => {
    it("Then it renders each submission as a row", () => {
      // Arrange
      const submissions = [
        { submission_id: "s1", form_id: "intake", patient_id: "p1", submitted_at: 1714430000 },
        { submission_id: "s2", form_id: "followup", patient_id: "p1", submitted_at: 1714431000 }
      ];

      // Act
      render(
        <SurveySubmissionList submissions={submissions} onView={() => {}} />
      );

      // Assert
      const rows = screen.getAllByRole("row", { name: /submission/i });
      expect(rows.length).toBe(2);

      expect(rows[0]).toHaveTextContent("s1");
      expect(rows[1]).toHaveTextContent("s2");
    });
  });

  describe("When the 'View' button is clicked", () => {
    it("Then it calls onView with the correct id", () => {
      // Arrange
      const submissions = [
        { submission_id: "s1", form_id: "intake", patient_id: "p1", submitted_at: 1714430000 },
        { submission_id: "s2", form_id: "followup", patient_id: "p1", submitted_at: 1714431000 }
      ];
      const onView = jest.fn();

      // Act
      render(
        <SurveySubmissionList submissions={submissions} onView={onView} />
      );
      const viewBtns = screen.getAllByRole("button", { name: /view/i });
      fireEvent.click(viewBtns[0]);

      // Assert
      expect(onView).toHaveBeenCalledWith("s1");
    });
  });
});
