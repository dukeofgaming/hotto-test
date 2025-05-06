import React from "react";
import SurveySubmission from "./SurveySubmission";

function SurveySubmissionList({ submissions, onView }) {
  return (
    <div className="flex items-center justify-center min-h-screen w-full">
      <table role="table" aria-label="survey submissions" className="bg-white rounded-lg shadow-md border border-gray-200 table-auto mx-auto align-middle">
        <thead>
          <tr>
            <th className="hotto-th px-6 py-3 font-semibold text-left whitespace-nowrap !text-white rounded-tl-lg">ID</th>
            <th className="hotto-th px-6 py-3 font-semibold text-left whitespace-nowrap !text-white">Form</th>
            <th className="hotto-th px-6 py-3 font-semibold text-left whitespace-nowrap !text-white">Patient</th>
            <th className="hotto-th px-6 py-3 font-semibold text-left whitespace-nowrap !text-white">Submitted At</th>
            <th className="hotto-th px-6 py-3 font-semibold text-left whitespace-nowrap !text-white rounded-tr-lg">Action</th>
          </tr>
        </thead>
        <tbody>
          {submissions.map(sub => (
            <SurveySubmission key={sub.submission_id || sub.id} submission={sub} onView={onView} />
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default SurveySubmissionList;
