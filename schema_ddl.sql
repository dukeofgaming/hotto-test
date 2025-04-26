CREATE TABLE questions (
    id VARCHAR(255) UNIQUE PRIMARY KEY,
    question_text VARCHAR(255) NOT NULL,
    type VARCHAR(50) NOT NULL
);

CREATE TABLE submissions (
    id VARCHAR(255) UNIQUE PRIMARY KEY,
    form_id VARCHAR(255) NOT NULL,
    patient_id VARCHAR(255) NOT NULL,

    FOREIGN KEY (form_id) REFERENCES forms(id),
    FOREIGN KEY (patient_id) REFERENCES patients(id)
);

CREATE TABLE forms (
    id VARCHAR(255) UNIQUE PRIMARY KEY
);

CREATE TABLE patients (
    id VARCHAR(255) UNIQUE PRIMARY KEY
);

CREATE TABLE answers (
    id VARCHAR(255) UNIQUE PRIMARY KEY,
    submission_id VARCHAR(255) NOT NULL,
    question_id VARCHAR(255) NOT NULL,
    answer_text TEXT NULL
);

CREATE TABLE form_questions (
    form_id VARCHAR(255) NOT NULL,
    question_id VARCHAR(255) NOT NULL,
    PRIMARY KEY (form_id, question_id),
    FOREIGN KEY (form_id) REFERENCES forms(id),
    FOREIGN KEY (question_id) REFERENCES questions(id)
);