CREATE TABLE questions (
    id VARCHAR(255) NOT NULL PRIMARY KEY,
    question_text VARCHAR(1000) NOT NULL,
    type VARCHAR(20) NOT NULL
);

CREATE TABLE forms (
    id VARCHAR(255) NOT NULL PRIMARY KEY
);

CREATE TABLE patients (
    id VARCHAR(255) NOT NULL PRIMARY KEY
);

CREATE TABLE submissions (
    id VARCHAR(255) NOT NULL PRIMARY KEY,
    form_id VARCHAR(255) NOT NULL,
    patient_id VARCHAR(255) NOT NULL,
    submitted_at BIGINT NOT NULL,
    CONSTRAINT fk_submission_form FOREIGN KEY (form_id) REFERENCES forms(id),
    CONSTRAINT fk_submission_patient FOREIGN KEY (patient_id) REFERENCES patients(id)
);

CREATE TABLE answers (
    id VARCHAR(255) NOT NULL PRIMARY KEY,
    submission_id VARCHAR(255) NOT NULL,
    question_id VARCHAR(255) NOT NULL,
    value TEXT NOT NULL,
    CONSTRAINT fk_answer_submission FOREIGN KEY (submission_id) REFERENCES submissions(id),
    CONSTRAINT fk_answer_question FOREIGN KEY (question_id) REFERENCES questions(id)
);

CREATE TABLE form_questions (
    form_id VARCHAR(255) NOT NULL,
    question_id VARCHAR(255) NOT NULL,
    position INTEGER NOT NULL,
    PRIMARY KEY (form_id, question_id),
    CONSTRAINT fk_form_question_form FOREIGN KEY (form_id) REFERENCES forms(id),
    CONSTRAINT fk_form_question_question FOREIGN KEY (question_id) REFERENCES questions(id)
);