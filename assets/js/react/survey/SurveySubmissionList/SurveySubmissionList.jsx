import React from "react";
import SurveySubmission from "./SurveySubmission";
import FormSelector from "../FormSelector/FormSelector";

function SurveySubmissionList({ submissions, onView, patient_id, forms, selectedFormId, onSelect }) {
  // Number of columns in the table
  const columnCount = 5;
  return (
    <div className="flex items-center justify-center h-full">
      <table role="table" aria-label="survey submissions" className="bg-white rounded-lg shadow-md border border-gray-200 table-auto align-middle">
        <thead>
          {/* Patient Info Row */}
          <tr>
            <th colSpan={columnCount} className="text-center py-3 text-xl font-semibold text-gray-800 bg-white border-b border-gray-200">
              Patient Surveys for <span className="font-mono">patient_id: {patient_id}</span>
            </th>
          </tr>
          {/* Table Header Row with FormSelector in last cell */}
          <tr>
            <th className="px-6 py-3 text-left whitespace-nowrap rounded-tl-lg text-white bg-[#FF8159]">ID</th>
            <th className="px-6 py-3 text-left whitespace-nowrap text-white bg-[#FF8159]">
              Form
              <div className="mt-2">
                <FormSelector forms={forms} selectedFormId={selectedFormId} onSelect={onSelect} />
              </div>
            </th>
            <th className="px-6 py-3 text-left whitespace-nowrap text-white bg-[#FF8159]">Patient</th>
            <th className="px-6 py-3 text-left whitespace-nowrap text-white bg-[#FF8159]">Submitted At</th>
            <th className="px-6 py-3 text-right whitespace-nowrap rounded-tr-lg text-white bg-[#FF8159]">Action</th>
          </tr>
        </thead>
        <tbody>
          {submissions.map(sub => (
            <tr
              key={sub.submission_id || sub.id}
              className="bg-white"
              aria-label={`survey submission ${sub.submission_id || sub.id}`}
              role="row"
            >
              <td className="px-6 py-3 text-black">{sub.id || sub.submission_id}</td>
              <td className="px-6 py-3 text-black">{sub.form_id}</td>
              <td className="px-6 py-3 text-black">{sub.patient_id}</td>
              <td className="px-6 py-3 text-black">{sub.submitted_at}</td>
              <td className="px-6 py-3 text-right text-black">
                <button className="hotto-btn" onClick={() => onView(sub.id || sub.submission_id)} aria-label={`View submission ${sub.id || sub.submission_id}`}>View</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default SurveySubmissionList;
