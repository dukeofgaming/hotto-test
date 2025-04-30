# ADR-7: Docs as Code

## Status
Accepted

## Context
Up-to-date documentation is essential for project success. Documentation must be clear, thorough, and evolve alongside the codebase. Traditional approaches (wikis, external tools) often fall out of sync with code. Treating documentation as code ensures it is always versioned, reviewed, and improved as part of the development process.

## Decision
Adopt the "Docs as Code" methodology: all technical documentation, ADRs, and guides are written in Markdown and stored in the same repository as the codebase. Documentation is updated via pull requests and reviewed as part of normal development. Developers are encouraged to use text-based tools (e.g., Mermaid, D2, Draw.io) for diagrams and visual aids, also stored as code artifacts.

```d2
...
answers : {
    shape: sql_table
    id: "VARCHAR(255) PRIMARY KEY"
    submission_id: "VARCHAR(255) NOT NULL"
    question_id: "VARCHAR(255) NOT NULL"
    value: "TEXT NOT NULL"
}

form_questions : {
    shape: sql_table
    form_id: "VARCHAR(255) NOT NULL"
    question_id: "VARCHAR(255) NOT NULL"
    position: "INTEGER NOT NULL"
}

# Relationships
submissions -> forms : "form_id"
submissions -> patients : "patient_id"
answers -> submissions : "submission_id"
answers -> questions : "question_id"
form_questions -> forms : "form_id"
form_questions -> questions : "question_id"

```

![alt text](../../erd.svg)

## Consequences
1. Documentation is in version control, making it easier to keep up to date and auditable.
2. Developers can update documentation as they work, improving context for code reviews and reducing knowledge silos.
3. Markdown can be used for note-taking and easily converted into project documentation.
4. All design/diagramming tools are available as part of the development environment, reducing the need for proprietary tools and silos.
5. Enables automated documentation generation, publishing, and static site creation if needed.
6. Promotes a culture of continuous documentation and shared ownership.
7. Using Obsidian or Foam enables developers to create a Knowledge Base over time.