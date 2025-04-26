<?php

$data = json_decode(file_get_contents('./data.json'), true);



class Question {
    public array $answers = [];

    public function __construct(
        public string $question,

        public int $correctAnswer
    ) {
    }
}

class Answer {
    public function __construct(
        public string $submission_id,
        public Question $question,
        public ?string $answer_text
    ){}
}

class Submission {
    public array $answers = [];

    public function __construct(
        public string $submission_id,
        public string $form_id,
        public string $patient_id,
        public string $submitted_at,
        Answer ...$answers
    ) {
        $this->answers = $answers;
    }
}

$submissions = [];

foreach ($data as $submission) {



    $submissions[] = new Submission(
        $submission['submission_id'],
        
        $submission['form_id'],
        $submission['patient_id'],
        $submission['submitted_at'],

        $submission['answers'] //TODO: Delegate parsing to Answer class
    );
}


