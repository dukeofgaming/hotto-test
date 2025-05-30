import React from "react";

function TextAnswerValue({ value }) {
  return (
    <input
      type="text"
      value={value}
      readOnly
      role="textbox"
      aria-label="answer value"
      className="border border-gray-300 rounded-md px-3 py-2 text-gray-900 bg-white w-full focus:outline-none focus:ring-2 focus:ring-orange-400"
    />
  );
}

export default TextAnswerValue;
