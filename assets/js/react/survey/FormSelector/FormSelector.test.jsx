import React from "react";
import { render, screen, fireEvent } from "@testing-library/react";
import FormSelector from "./FormSelector";

describe("Given FormSelector is rendered", () => {
  describe("When forms and a selected value are provided", () => {
    it("Then it renders the options and sets the selected value", () => {
      // Arrange
      const forms = [{ id: "intake" }, { id: "followup" }];
      // Act
      render(
        <FormSelector forms={forms} selectedFormId="intake" onSelect={() => {}} />
      );
      // Assert
      const select = screen.getByTestId("form-selector");
      expect(select).toBeInTheDocument();
      expect(select.value).toBe("intake");
      expect(screen.getByText("intake")).toBeInTheDocument();
      expect(screen.getByText("followup")).toBeInTheDocument();
    });
  });

  describe("When the value is changed", () => {
    it("Then it calls onSelect when changed", () => {
      // Arrange
      const forms = [{ id: "intake" }, { id: "followup" }];
      const onSelect = jest.fn();
      render(
        <FormSelector forms={forms} selectedFormId="intake" onSelect={onSelect} />
      );
      const select = screen.getByTestId("form-selector");
      // Act
      fireEvent.change(select, { target: { value: "followup" } });
      // Assert
      expect(onSelect).toHaveBeenCalledWith("followup");
    });
  });
});
