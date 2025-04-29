-- Preload fixture data for forms
INSERT INTO forms (id) VALUES ('basic_check');
INSERT INTO forms (id) VALUES ('mental_health_followup');
-- Add more forms as needed

-- Preload fixture data for patients
INSERT INTO patients (id) VALUES ('abc123');
INSERT INTO patients (id) VALUES ('abc234');
INSERT INTO patients (id) VALUES ('abc321');
INSERT INTO patients (id) VALUES ('abc432');

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


-- Preexisting submissions

INSERT INTO `submissions` (`id`, `form_id`, `patient_id`, `submitted_at`) VALUES ('ghi123', 'basic_check', 'abc321', 1744389045);
INSERT INTO `submissions` (`id`, `form_id`, `patient_id`, `submitted_at`) VALUES ('ghi124', 'mental_health_followup', 'abc321', 1744129845);
INSERT INTO `submissions` (`id`, `form_id`, `patient_id`, `submitted_at`) VALUES ('ghi125', 'basic_check', 'abc432', 1739205045);

INSERT INTO `answers` (`id`, `submission_id`, `question_id`, `value`) VALUES ('165f7b40f1b7a3cd59638dd6563795b758a8235376a241db2ff7b7b6c1474297', 'ghi123', 'Patient Name', 'Mario López');
INSERT INTO `answers` (`id`, `submission_id`, `question_id`, `value`) VALUES ('37412e2a6c5fc27311d12ecd4abd9a475cc902a14a24f73f14109079ba876d9f', 'ghi125', 'Date of Birth', '1955-04-01');
INSERT INTO `answers` (`id`, `submission_id`, `question_id`, `value`) VALUES ('5d2ee4e3d249c55e4870fd6e7dc076c7421655727f6e463184bd89c8228a2986', 'ghi124', 'Patient Name', 'Mario López');
INSERT INTO `answers` (`id`, `submission_id`, `question_id`, `value`) VALUES ('603839f55a6742bd9a4b7f9f3bec0101bdd6f4fc549d6745d3a97409865c898d', 'ghi123', 'Insurance Provider', '{\'name\': \'\', \'policy_number\': \'\'}');
INSERT INTO `answers` (`id`, `submission_id`, `question_id`, `value`) VALUES ('6ae12f0eb211fa72d8166825bcb9d19778ebeb480b6c4c099ac7a33930453e14', 'ghi124', 'Date of Birth', '1950-02-18');
INSERT INTO `answers` (`id`, `submission_id`, `question_id`, `value`) VALUES ('6bb3132ab0ecd82811e84cfb842f72acbdf771b55e9530818a1f8e1ced09da9f', 'ghi125', 'Has Insurance?', 'Yes');
INSERT INTO `answers` (`id`, `submission_id`, `question_id`, `value`) VALUES ('a9afbd2825a959430675ae801c0c49b22a5e21000cc3f3a05b66fb7eb52aed29', 'ghi125', 'Insurance Provider', '{\'name\': \'Aetna\', \'policy_number\': \'AH-100-2988\'}');
INSERT INTO `answers` (`id`, `submission_id`, `question_id`, `value`) VALUES ('ac4d0c2b9a08edcc2f7927d6076f9229a988577ea1d51b772d89a8fb95654267', 'ghi125', 'Recent Health Events', '[\'Fractured foot in 2022\', \'Diagnosed with type 1 diabetes\']');
INSERT INTO `answers` (`id`, `submission_id`, `question_id`, `value`) VALUES ('b096414e2cbab138aa41c812ad5ad892a703e57d629497ca44d6ebb7bf7832db', 'ghi123', 'Date of Birth', '1950-02-18');
INSERT INTO `answers` (`id`, `submission_id`, `question_id`, `value`) VALUES ('ba199a4af81d6461240e41fd7cc09687db13ccab1adfb15ec3221f0e9c48f678', 'ghi123', 'Has Insurance?', 'No');
INSERT INTO `answers` (`id`, `submission_id`, `question_id`, `value`) VALUES ('cf55598f5cca717687bd3c4643c1ff5fad16bcb600b14037414481ddca6d9dd9', 'ghi125', 'Patient Name', 'Luisa Jhonson');
INSERT INTO `answers` (`id`, `submission_id`, `question_id`, `value`) VALUES ('d42840a51cb8c33c26f10fe5ff4baaac01585170fd3aebfe7c08c21c67221353', 'ghi124', 'How many hours of sleep did you get last night?', '8');
INSERT INTO `answers` (`id`, `submission_id`, `question_id`, `value`) VALUES ('df1e07c9e9b40498840308b2de737ade1b5ea28f8e3fb0d3ca70bef31ad234da', 'ghi123', 'Recent Health Events', '[\'Hospitalization in 2020\', \'Started physical therapy\', \'Diagnosed with insomnia\']');
INSERT INTO `answers` (`id`, `submission_id`, `question_id`, `value`) VALUES ('e3749bb687bfb5b23ccabdfc1391314aedb56b7c6be65a1a7fd8ff3bd3b10414', 'ghi124', 'Describe your mood over the past week', 'Depressed, occasionally anxious');