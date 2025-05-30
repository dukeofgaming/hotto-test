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
    <div className="min-h-screen flex items-center justify-center bg-[#554F6C]">
      <div role="region" aria-label="patient surveys root" className="flex flex-col items-center justify-center gap-y-6 bg-[#F6E7D8] rounded-xl shadow-lg px-2 md:px-8 py-4 md:py-10 max-w-4xl overflow-auto">
        <div className="w-full overflow-x-auto">
          <SurveySubmissionList
            submissions={filteredSubmissions}
            onView={handleView}
            patient_id={patient_id}
            forms={forms}
            selectedFormId={selectedFormId}
            onSelect={setSelectedFormId}
          />
        </div>
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
            <div className="fixed inset-0 flex items-center justify-center z-[1001] bg-[#4B4662]" style={{ pointerEvents: 'auto' }}>
              <div
                className="relative pt-12 md:pt-16 p-8 max-w-3xl w-full mx-auto flex flex-col rounded-xl"
                style={{
                  minWidth: 600,
                  maxWidth: '90vw',
                  maxHeight: '90vh',
                  overflowY: 'auto',
                  pointerEvents: 'auto',
                }}
                role="dialog"
                aria-label="answers"
              >
                <div className="bg-[#F6E7D8] rounded-xl w-full relative">
                  <button
                    type="button"
                    aria-label="Close modal"
                    onClick={handleClose}
                    className="absolute top-[-20px] right-[-20px] bg-white text-[#4B4662] rounded-full w-10 h-10 flex items-center justify-center shadow-md hover:bg-gray-200 focus:outline-none focus:ring-2 focus:ring-orange-400 z-10 border border-[#F6E7D8]"
                  >
                    <span className="sr-only">Close</span>
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="2">
                      <path strokeLinecap="round" strokeLinejoin="round" d="M6 18L18 6M6 6l12 12" />
                    </svg>
                  </button>
                  <AnswerList answers={answers} questions={shownQuestions} hideClose className="bg-white rounded-lg shadow-md" />
                </div>
              </div>
            </div>
          </>
        )}
      </div>
    </div>
  );
}

export default PatientSurveys;
