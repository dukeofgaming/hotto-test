import React from "react";

function BooleanAnswerValue({ value }) {
  // Accepts various representations of true/false
  const checked =
    value === true ||
    value === "true" ||
    (typeof value === "string" && value.trim().toLowerCase() === "yes");
  return <input type="checkbox" checked={checked} readOnly data-testid="boolean-answer-value" />;
}

export default BooleanAnswerValue;
