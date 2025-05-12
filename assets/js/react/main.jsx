import React from 'react';
import { createRoot } from 'react-dom/client';
import './index.css';
import PatientSurveys from './survey/PatientSurveys';

const patient_id = window.REACT_PROPS;
const root = createRoot(document.getElementById('react-root'));
root.render(<PatientSurveys patient_id={patient_id} />);
