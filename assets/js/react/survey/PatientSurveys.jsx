import React, { useState, useEffect } from "react";
import FormSelector from "./FormSelector/FormSelector";
import SurveySubmissionList from "./SurveySubmissionList/SurveySubmissionList";
import AnswerList from "./AnswerList/AnswerList";

// --- Begin: Use improved API response as const ---
/*
const API_RESPONSE = {
  forms: [
    { id: "basic_check", name: "Basic Check" },
    { id: "mental_health_followup", name: "Mental Health Followup" }
  ],
  questions: [
    { id: "Patient Name", question_text: "Patient Name", type: "text", is_clinical: false },
    { id: "Date of Birth", question_text: "Date of Birth", type: "date", is_clinical: false },
    { id: "Has Insurance?", question_text: "Has Insurance?", type: "boolean", is_clinical: false },
    { id: "Insurance Provider", question_text: "Insurance Provider", type: "object", is_clinical: false },
    { id: "Recent Health Events", question_text: "Recent Health Events", type: "array", is_clinical: true },
    { id: "Describe your mood over the past week", question_text: "Describe your mood over the past week", type: "text", is_clinical: true },
    { id: "How many hours of sleep did you get last night?", question_text: "How many hours of sleep did you get last night?", type: "number", is_clinical: true }
  ],
  submissions: [
    {
      answers: [
        { question_id: "Date of Birth", value: "1950-02-18" },
        { question_id: "Has Insurance?", value: "No" },
        { question_id: "Insurance Provider", value: { name: "", policy_number: "" } },
        { question_id: "Patient Name", value: "Mario López" },
        { question_id: "Recent Health Events", value: ["Hospitalization in 2020", "Started physical therapy", "Diagnosed with insomnia"] }
      ],
      form_id: "basic_check",
      patient_id: "abc321",
      submission_id: "ghi123",
      submitted_at: 1744389045
    },
    {
      answers: [
        { question_id: "Date of Birth", value: "1950-02-18" },
        { question_id: "Describe your mood over the past week", value: "Depressed, occasionally anxious" },
        { question_id: "How many hours of sleep did you get last night?", value: "8" },
        { question_id: "Patient Name", value: "Mario López" }
      ],
      form_id: "mental_health_followup",
      patient_id: "abc321",
      submission_id: "ghi124",
      submitted_at: 1744129845
    }
  ]
};
*/
// --- End: Use improved API response as const ---

function PatientSurveys({ patient_id }) {
  if (!patient_id) {
    return (
      <div style={{ color: 'red', padding: '1em', background: '#fff3cd', border: '1px solid #ffeeba', borderRadius: '4px', margin: '2em 0' }}>
        <h2 style={{marginTop: 0}}>Patient not found or not provided</h2>
        <div>
          <strong>Warning:</strong> No <code>patient_id</code> provided.<br />
          Please use a URL like <code>localhost/?patient_id=abc321</code> to view patient surveys.
        </div>
      </div>
    );
  }

  const [modalOpen, setModalOpen] = useState(false);
  const [selectedSubmissionId, setSelectedSubmissionId] = useState(null);
  const [selectedFormId, setSelectedFormId] = useState("");
  const [apiResponse, setApiResponse] = useState({ forms: [], questions: [], submissions: [] });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    setLoading(true);
    setError(null);
    fetch(`/api/surveys/show?patient_id=${patient_id}`)
      .then(res => {
        if (!res.ok) throw new Error("Failed to fetch surveys");
        return res.json();
      })
      .then(data => {
        setApiResponse(data);
        setLoading(false);
      })
      .catch(e => {
        setError(e.message);
        setLoading(false);
      });
  }, [patient_id]);

  const forms = apiResponse.forms;
  const questions = apiResponse.questions;
  const submissions = apiResponse.submissions;

  // Filter submissions by selected form (if any)
  const filteredSubmissions = selectedFormId
    ? submissions.filter(s => s.form_id === selectedFormId)
    : submissions;

  // Find answers for selected submission
  const answers = submissions
    .find(s => s.submission_id === selectedSubmissionId)?.answers || [];

  // Only include questions present in the selected submission's answers
  const answerQIds = new Set(answers.map(a => a.question_id));
  const shownQuestions = questions.filter(q => answerQIds.has(q.id));

  const handleView = (submissionId) => {
    setSelectedSubmissionId(submissionId);
    setModalOpen(true);
  };

  const handleClose = () => {
    setModalOpen(false);
    setSelectedSubmissionId(null);
  };

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div role="region" aria-label="patient surveys root">
      Patient Surveys for patient_id: {patient_id}
      <FormSelector forms={forms} selectedFormId={selectedFormId} onSelect={setSelectedFormId} />
      <SurveySubmissionList submissions={filteredSubmissions} onView={handleView} />
      {modalOpen && (
        <>
          <div style={{
            position: 'fixed',
            top: 0,
            left: 0,
            width: '100vw',
            height: '100vh',
            background: 'rgba(0,0,0,0.5)',
            zIndex: 1000
          }} />
          <div className="bg-[#4B4662] rounded-lg shadow-lg p-8 max-w-3xl w-full mx-auto" style={{
            position: 'fixed',
            top: '50%',
            left: '50%',
            transform: 'translate(-50%, -50%)',
            zIndex: 1001,
            minWidth: 600,
            maxWidth: '90vw',
            maxHeight: '90vh',
            overflowY: 'auto',
          }}>
            <AnswerList answers={answers} questions={shownQuestions} onClose={handleClose} />
          </div>
        </>
      )}
    </div>
  );
}

export default PatientSurveys;
