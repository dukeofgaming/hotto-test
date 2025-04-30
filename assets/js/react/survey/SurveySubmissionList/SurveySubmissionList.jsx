import React from "react";
import SurveySubmission from "./SurveySubmission";

function SurveySubmissionList({ submissions, onView }) {
  return (
    <table data-testid="survey-submission-list">
      <thead>
        <tr>
          <th>ID</th>
          <th>Form</th>
          <th>Patient</th>
          <th>Submitted At</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        {submissions.map(sub => (
          <SurveySubmission key={sub.id} submission={sub} onView={onView} />
        ))}
      </tbody>
    </table>
  );
}

export default SurveySubmissionList;
