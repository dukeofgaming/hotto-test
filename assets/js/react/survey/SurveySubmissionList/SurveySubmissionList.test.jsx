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
      // Get all rows, including header and info rows
      const allRows = screen.getAllByRole("row");
      // Data rows are after the two header rows
      const dataRows = allRows.slice(2);
      expect(dataRows.length).toBe(2);

      expect(dataRows[0]).toHaveTextContent("s1");
      expect(dataRows[1]).toHaveTextContent("s2");
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
