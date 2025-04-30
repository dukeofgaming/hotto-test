import React from "react";

function ArrayAnswerValue({ value }) {
  let arr = value;
  if (typeof value === "string") {
    try {
      arr = JSON.parse(value);
    } catch (e) {
      return <span data-testid="array-answer-value">Invalid array</span>;
    }
  }
  if (!Array.isArray(arr)) {
    return <span data-testid="array-answer-value">Invalid array</span>;
  }
  return (
    <ul data-testid="array-answer-value">
      {arr.map((item, idx) => (
        <li key={idx}>{String(item)}</li>
      ))}
    </ul>
  );
}

export default ArrayAnswerValue;
