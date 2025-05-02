import React from "react";
import AnswerValue from "./AnswerValue";

function Answer({ question, answer }) {
  return (
    <tr role="row" aria-label="answer">
      <td>{question.question_text}</td>
      <td>{question.type}</td>
      <td>
        <AnswerValue value={answer.value} type={question.type} />
      </td>
    </tr>
  );
}

export default Answer;
