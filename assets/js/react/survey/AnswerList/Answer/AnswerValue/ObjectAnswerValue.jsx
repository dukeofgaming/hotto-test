import React from "react";

function ObjectAnswerValue({ value }) {
  let obj = value;
  if (typeof value === "string") {
    try {
      obj = JSON.parse(value);
    } catch (e) {
      return <span data-testid="object-answer-value">Invalid object</span>;
    }
  }
  if (!obj || typeof obj !== "object" || Array.isArray(obj)) {
    return <span data-testid="object-answer-value">Invalid object</span>;
  }
  return (
    <table data-testid="object-answer-value" style={{ border: "1px solid #ccc", fontSize: 12 }}>
      <tbody>
        {Object.entries(obj).map(([k, v]) => (
          <tr key={k}>
            <td><strong>{k}</strong></td>
            <td>{String(v)}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default ObjectAnswerValue;
