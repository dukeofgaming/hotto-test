import React from "react";
import AnswerValue from "./AnswerValue";

function Answer({ question, answer }) {
  return (
    <tr role="row" aria-label="answer">
      <td className="px-6 py-3">{question.question_text}</td>
      <td className="px-6 py-3">{question.type}</td>
      <td className="px-6 py-3">
        <AnswerValue value={answer.value} type={question.type} />
      </td>
    </tr>
  );
}

export default Answer;
