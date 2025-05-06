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
    <div role="dialog" aria-label="answers" className="bg-white rounded-lg shadow-md border border-gray-200 p-8 max-w-3xl w-full mx-auto">
      <button type="button" aria-label="close" onClick={onClose}>Close</button>
      <table className="w-full table-auto mx-auto align-middle">
        <thead>
          <tr>
            <th className="hotto-th px-6 py-3 font-semibold text-left whitespace-nowrap !text-white rounded-tl-lg">Question</th>
            <th className="hotto-th px-6 py-3 font-semibold text-left whitespace-nowrap !text-white">Type</th>
            <th className="hotto-th px-6 py-3 font-semibold text-left whitespace-nowrap !text-white rounded-tr-lg">Answer</th>
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
