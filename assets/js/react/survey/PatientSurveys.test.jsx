import React from "react";
import { render, screen } from "@testing-library/react";
import PatientSurveys from "./PatientSurveys";
import FormSelector from "./FormSelector.jsx";
import SurveySubmissionList from "./SurveySubmissionList.jsx";
import AnswerList from "./AnswerList.jsx";

describe("Given PatientSurveys is rendered", () => {
  beforeEach(() => {
    global.fetch = jest.fn(() =>
      Promise.resolve({
        ok: true,
        json: () => Promise.resolve({
          forms: [
            { id: "basic_check" },
            { id: "mental_health_followup" }
          ],
          questions: [
            { id: "Patient Name", question_text: "Patient Name", type: "text", is_clinical: false },
            { id: "Date of Birth", question_text: "Date of Birth", type: "date", is_clinical: false }
          ],
          submissions: [
            {
              answers: [
                { question_id: "Patient Name", value: "Mario López" },
                { question_id: "Date of Birth", value: "1950-02-18" }
              ],
              form_id: "basic_check",
              patient_id: "abc321",
              submission_id: "ghi123",
              submitted_at: 1744389045
            }
          ]
        })
      })
    );
  });

  afterEach(() => {
    global.fetch.mockClear();
  });

  describe("When patient_id is provided", () => {
    it("Then it renders the PatientSurveys root with the patient_id", async () => {
      // Arrange
      const patientId = "123";

      // Act
      render(<PatientSurveys patient_id={patientId} />);

      // Assert: wait for the patient-surveys-root to appear
      const root = await screen.findByRole("region", { name: /patient surveys root/i });
      expect(root).toBeInTheDocument();
      expect(root).toHaveTextContent("patient_id: 123");
    });
  });
});
