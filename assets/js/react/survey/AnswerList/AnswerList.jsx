import React from "react";
import Answer from "./Answer/Answer";

function AnswerList({ answers, questions, onClose }) {
  // Map questions by id for easy lookup
  const questionMap = React.useMemo(() => {
    const map = {};
    questions.forEach(q => { map[q.id] = q; });
    return map;
  }, [questions]);

  // Order answers by question order in questions array
  const orderedAnswers = questions
    .map(q => answers.find(a => a.question_id === q.id))
    .filter(Boolean);

  return (
    <div data-testid="answer-list-modal" style={{ background: "#fff", border: "1px solid #ccc", padding: 24 }}>
      <button data-testid="close-btn" onClick={onClose}>Close</button>
      <table data-testid="answer-list-table">
        <thead>
          <tr>
            <th>Question</th>
            <th>Type</th>
            <th>Answer</th>
          </tr>
        </thead>
        <tbody>
          {orderedAnswers.map(ans => (
            <Answer key={ans.id} question={questionMap[ans.question_id]} answer={ans} />
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default AnswerList;
