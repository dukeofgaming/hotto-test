import React from "react";

function TextAnswerValue({ value }) {
  return <input type="text" value={value} readOnly data-testid="text-answer-value" />;
}

export default TextAnswerValue;
