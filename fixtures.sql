-- Preload fixture data for forms
INSERT INTO forms (id) VALUES ('basic_check');
INSERT INTO forms (id) VALUES ('mental_health_followup');
-- Add more forms as needed

-- Preload fixture data for patients
INSERT INTO patients (id) VALUES ('abc123');
INSERT INTO patients (id) VALUES ('abc234');
-- Add more forms and patients as needed

-- Preload fixture data for questions
INSERT INTO questions (id, question_text, type) VALUES ('Patient Name', 'Patient Name', 'text');
INSERT INTO questions (id, question_text, type) VALUES ('Date of Birth', 'Date of Birth', 'date');
INSERT INTO questions (id, question_text, type) VALUES ('Has Insurance?', 'Has Insurance?', 'boolean');
INSERT INTO questions (id, question_text, type) VALUES ('Insurance Provider', 'Insurance Provider', 'object');
INSERT INTO questions (id, question_text, type) VALUES ('Recent Health Events', 'Recent Health Events', 'array');
INSERT INTO questions (id, question_text, type) VALUES ('Describe your mood over the past week', 'Describe your mood over the past week', 'text');
INSERT INTO questions (id, question_text, type) VALUES ('How many hours of sleep did you get last night?', 'How many hours of sleep did you get last night?', 'number');

-- Preload fixture data for form_questions
-- basic_check form
INSERT INTO form_questions (form_id, question_id, position) VALUES ('basic_check', 'Patient Name', 1);
INSERT INTO form_questions (form_id, question_id, position) VALUES ('basic_check', 'Date of Birth', 2);
INSERT INTO form_questions (form_id, question_id, position) VALUES ('basic_check', 'Has Insurance?', 3);
INSERT INTO form_questions (form_id, question_id, position) VALUES ('basic_check', 'Insurance Provider', 4);
INSERT INTO form_questions (form_id, question_id, position) VALUES ('basic_check', 'Recent Health Events', 5);
-- mental_health_followup form
INSERT INTO form_questions (form_id, question_id, position) VALUES ('mental_health_followup', 'Patient Name', 1);
INSERT INTO form_questions (form_id, question_id, position) VALUES ('mental_health_followup', 'Date of Birth', 2);
INSERT INTO form_questions (form_id, question_id, position) VALUES ('mental_health_followup', 'Describe your mood over the past week', 3);
INSERT INTO form_questions (form_id, question_id, position) VALUES ('mental_health_followup', 'How many hours of sleep did you get last night?', 4);
