import React, { useState } from "react";
import FormSelector from "./FormSelector/FormSelector";
import SurveySubmissionList from "./SurveySubmissionList/SurveySubmissionList";
import AnswerList from "./AnswerList/AnswerList";

// Mock data based on data/submissions_preexisting.json
const MOCK_SUBMISSIONS = [
  { id: "ghi123", form_id: "basic_check", patient_id: "abc321", submitted_at: "2025-04-11T16:30:45Z" },
  { id: "ghi124", form_id: "mental_health_followup", patient_id: "abc321", submitted_at: "2025-04-08T16:30:45Z" },
  { id: "ghi125", form_id: "basic_check", patient_id: "abc432", submitted_at: "2025-02-10T16:30:45Z" },
];

const MOCK_FORMS = [
  { id: "basic_check" },
  { id: "mental_health_followup" },
];

const MOCK_ANSWERS = [
  // Submission ghi123
  { id: "a1", submission_id: "ghi123", question_id: "q1", value: "Mario López" },
  { id: "a2", submission_id: "ghi123", question_id: "q2", value: "1950-02-18" },
  { id: "a3", submission_id: "ghi123", question_id: "q3", value: "No" },
  { id: "a4", submission_id: "ghi123", question_id: "q4", value: { name: "", policy_number: "" } },
  { id: "a5", submission_id: "ghi123", question_id: "q5", value: ["Hospitalization in 2020", "Started physical therapy", "Diagnosed with insomnia"] },
  // Submission ghi124
  { id: "a6", submission_id: "ghi124", question_id: "q1", value: "Mario López" },
  { id: "a7", submission_id: "ghi124", question_id: "q2", value: "1950-02-18" },
  { id: "a8", submission_id: "ghi124", question_id: "q3", value: "Depressed, occasionally anxious" },
  { id: "a9", submission_id: "ghi124", question_id: "q4", value: "8" },
  // Submission ghi125
  { id: "a10", submission_id: "ghi125", question_id: "q1", value: "Luisa Jhonson" },
  { id: "a11", submission_id: "ghi125", question_id: "q2", value: "1955-04-01" },
  { id: "a12", submission_id: "ghi125", question_id: "q3", value: "Yes" },
  { id: "a13", submission_id: "ghi125", question_id: "q4", value: { name: "Aetna", policy_number: "AH-100-2988" } },
  { id: "a14", submission_id: "ghi125", question_id: "q5", value: ["Fractured foot in 2022", "Diagnosed with type 1 diabetes"] },
];

const MOCK_QUESTIONS = [
  { id: "q1", question_text: "Patient Name", type: "text", is_clinical: false },
  { id: "q2", question_text: "Date of Birth", type: "date", is_clinical: false },
  { id: "q3", question_text: "Has Insurance?", type: "boolean", is_clinical: false },
  { id: "q4", question_text: "Insurance Provider", type: "object", is_clinical: false },
  { id: "q5", question_text: "Recent Health Events", type: "array", is_clinical: false },
  // For mental_health_followup
  { id: "q6", question_text: "Describe your mood over the past week", type: "text", is_clinical: false },
  { id: "q7", question_text: "How many hours of sleep did you get last night?", type: "text", is_clinical: false },
];

function PatientSurveys({ patient_id }) {
  const [modalOpen, setModalOpen] = useState(false);
  const [selectedSubmissionId, setSelectedSubmissionId] = useState(null);
  const [selectedFormId, setSelectedFormId] = useState("");

  // Filter submissions by selected form (if any)
  const filteredSubmissions = selectedFormId
    ? MOCK_SUBMISSIONS.filter(s => s.form_id === selectedFormId)
    : MOCK_SUBMISSIONS;

  // Find answers and questions for selected submission (mock logic)
  const answers = MOCK_ANSWERS.filter(a => a.submission_id === selectedSubmissionId);
  // Only include questions present in the selected submission's answers
  const answerQIds = new Set(answers.map(a => a.question_id));
  const questions = MOCK_QUESTIONS.filter(q => answerQIds.has(q.id));

  const handleView = (submissionId) => {
    setSelectedSubmissionId(submissionId);
    setModalOpen(true);
  };

  const handleClose = () => {
    setModalOpen(false);
    setSelectedSubmissionId(null);
  };

  return (
    <div data-testid="patient-surveys-root">
      Patient Surveys for patient_id: {patient_id}
      <FormSelector forms={MOCK_FORMS} selectedFormId={selectedFormId} onSelect={setSelectedFormId} />
      <SurveySubmissionList submissions={filteredSubmissions} onView={handleView} />
      {modalOpen && (
        <AnswerList answers={answers} questions={questions} onClose={handleClose} />
      )}
    </div>
  );
}

export default PatientSurveys;
