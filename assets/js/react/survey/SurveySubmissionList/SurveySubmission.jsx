import React from "react";

function SurveySubmission({ submission, onView }) {
  return (
    <tr role="row" aria-label="submission">
      <td className="px-6 py-3">{submission.submission_id}</td>
      <td className="px-6 py-3">{submission.form_id}</td>
      <td className="px-6 py-3">{submission.patient_id}</td>
      <td className="px-6 py-3">{submission.submitted_at}</td>
      <td className="px-6 py-3">
        <button onClick={() => onView && onView(submission.submission_id)} aria-label="view">
          View
        </button>
      </td>
    </tr>
  );
}

export default SurveySubmission;
