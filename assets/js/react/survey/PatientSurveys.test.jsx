import React from "react";
import { render, screen } from "@testing-library/react";
import PatientSurveys from "./PatientSurveys";

describe("Given PatientSurveys is rendered", () => {
  describe("When patient_id is provided", () => {
    it("Then it renders the PatientSurveys root with the patient_id", () => {
      // Arrange
      const patientId = "123";
      // Act
      render(<PatientSurveys patient_id={patientId} />);
      // Assert
      const root = screen.getByTestId("patient-surveys-root");
      expect(root).toBeInTheDocument();
      expect(root).toHaveTextContent("patient_id: 123");
    });
  });
});
