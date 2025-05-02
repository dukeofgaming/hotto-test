import React from "react";

function TextAnswerValue({ value }) {
  return <input type="text" value={value} readOnly role="textbox" aria-label="answer value" />;
}

export default TextAnswerValue;
