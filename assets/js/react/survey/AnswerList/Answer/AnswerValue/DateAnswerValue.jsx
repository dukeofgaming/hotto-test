import React from "react";

function DateAnswerValue({ value }) {
  return <input type="date" value={value} readOnly data-testid="date-answer-value" />;
}

export default DateAnswerValue;
