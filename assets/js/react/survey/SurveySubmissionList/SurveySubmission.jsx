import React from "react";

function SurveySubmission({ submission, onView }) {
  return (
    <tr role="row" aria-label="submission">
      <td>{submission.submission_id}</td>
      <td>{submission.form_id}</td>
      <td>{submission.patient_id}</td>
      <td>{submission.submitted_at}</td>
      <td>
        <button onClick={() => onView && onView(submission.submission_id)} aria-label="view">
          View
        </button>
      </td>
    </tr>
  );
}

export default SurveySubmission;
