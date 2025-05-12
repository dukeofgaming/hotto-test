import React from "react";
import AnswerValue from "./AnswerValue";

function AnswerList({ answers, questions, onClose, hideClose = false }) {
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
    <div role="dialog" aria-label="answers" className="bg-[#F6E7D8] p-8 max-w-3xl w-full mx-auto">
      {!hideClose && (
        <button type="button" aria-label="close" onClick={onClose} className="mb-4 px-4 py-2 rounded bg-gray-200 hover:bg-gray-300 focus:outline-none focus:ring-2 focus:ring-orange-400">Close</button>
      )}
      <div className="rounded-lg overflow-hidden border border-gray-200 shadow-md bg-white w-full">
        <table className="w-full table-auto mx-auto align-middle">
          <thead>
            <tr>
              <th className="hotto-th px-6 py-3 font-semibold text-left whitespace-nowrap text-black rounded-tl-lg">Question</th>
              <th className="hotto-th px-6 py-3 font-semibold text-left whitespace-nowrap text-black">Type</th>
              <th className="hotto-th px-6 py-3 font-semibold text-left whitespace-nowrap text-black rounded-tr-lg">Answer</th>
            </tr>
          </thead>
        <tbody>
          {orderedAnswers.map(ans => {
            const question = questionMap[ans.question_id];
            return (
              <tr key={ans.id} role="row" aria-label="answer">
                <td className="px-6 py-3 text-black">{question.question_text}</td>
                <td className="px-6 py-3 text-black">{question.type}</td>
                <td className="px-6 py-3 text-black">
                  <AnswerValue value={ans.value} type={question.type} />
                </td>
              </tr>
            );
          })}
        </tbody>
      </table>
      </div>
    </div>
  );
}

export default AnswerList;
