import React from 'react';
import { createRoot } from 'react-dom/client';
import PatientSurveys from './survey/PatientSurveys';

// Accept patient_id from window.REACT_PROPS or fallback
const patient_id = window.REACT_PROPS || 'p1';
const root = createRoot(document.getElementById('react-root'));
root.render(<PatientSurveys patient_id={patient_id} />);
