import React from "react";
import { render, screen, fireEvent, within } from "@testing-library/react";
import SurveySubmissionList from "./SurveySubmissionList.jsx";

describe("SurveySubmissionList", () => {
  const submissions = [
    {
      submission_id: "s1",
      form_id: "intake",
      patient_id: "p1",
      submitted_at: 1714430000,
      id: undefined,
    },
    {
      submission_id: undefined,
      id: "s2",
      form_id: "followup",
      patient_id: "p2",
      submitted_at: 1714431111,
    },
  ];
  const forms = [
    { id: "intake", name: "Intake" },
    { id: "followup", name: "Follow Up" },
  ];

  it("renders all submission rows and columns correctly", () => {
    render(
      <SurveySubmissionList
        submissions={submissions}
        onView={() => {}}
        patient_id="pat-123"
        forms={forms}
        selectedFormId={"intake"}
        onSelect={() => {}}
      />
    );
    // Get all data rows (skip header rows)
    const allRows = screen.getAllByRole("row");
    const dataRows = allRows.slice(2);

    // First submission
    expect(within(dataRows[0]).getByText("s1")).toBeInTheDocument();
    expect(within(dataRows[0]).getByText("intake")).toBeInTheDocument();
    expect(within(dataRows[0]).getByText("p1")).toBeInTheDocument();
    expect(within(dataRows[0]).getByText("1714430000")).toBeInTheDocument();

    // Second submission
    expect(within(dataRows[1]).getByText("s2")).toBeInTheDocument();
    expect(within(dataRows[1]).getByText("followup")).toBeInTheDocument();
    expect(within(dataRows[1]).getByText("p2")).toBeInTheDocument();
    expect(within(dataRows[1]).getByText("1714431111")).toBeInTheDocument();

    // Check patient id in header
    expect(screen.getByText(/patient_id: pat-123/)).toBeInTheDocument();
  });

  it("calls onView with correct id when 'View' button is clicked", () => {
    const onView = jest.fn();
    render(
      <SurveySubmissionList
        submissions={submissions}
        onView={onView}
        patient_id="pat-123"
        forms={forms}
        selectedFormId={"intake"}
        onSelect={() => {}}
      />
    );
    // Click first "View" button
    const viewButtons = screen.getAllByRole("button", { name: /view/i });
    fireEvent.click(viewButtons[0]);
    expect(onView).toHaveBeenCalledWith("s1");
    fireEvent.click(viewButtons[1]);
    expect(onView).toHaveBeenCalledWith("s2");
  });
});
