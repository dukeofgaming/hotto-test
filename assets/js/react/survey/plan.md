1. Create a top level React component that is called PatientSurveys, it has a prop for patient_id

2. It should have two subcomponents: FormSelector (combo box) and SurveySubmissionList (table)

3. SurveySubmissionList (renders as a table) has a collection of subcomponents called SurveySubmission 

4. SurveySubmission renders as a row, showing the form type, submission date, and a link to view the survey AnswerList, each SurveySubmission represents a submission (see submission.py)

5. SurveySubmission has a link, which opens a modal to present an AnswerList component as a modal

6. The AnswerList component includes a table which it populates with the general survey submission data for convenience, but below has a table in which multiple Answer subcomponents

7. Answer subcomponents present the answer to a single question, in the order specified for the form (see form_questions pivot table)

8. Answer subcomponents have a label, which is the question text, a value, which is the answer value, and a type, which is used to render the answer in the correct way.

9. Answer will have a single subcomponent called AnswerValue, which has two props: value and type

10. AnswerValue is like an abstract component, it will decide dynamically which component to render based on the type prop. THere should be the following concrete components:
    
    - TextAnswerValue: Renders a readonly text input
    - DateAnswerValue: Renders a readonly date input
    - BooleanAnswerValue: Renders a readonly checkbox
    - ObjectAnswerValue: Renders as a small table with key-value pairs
    - ArrayAnswerValue: Renders an unordered list of items

Prompt:

I need to create a React component  called PatientSurveys, as defined by my plan.md in assets/js/react/survey

but we will take this step by step, so that we can implement things end to end alongside the required API and data structures in python

we will use CDD and design the component and expected props first, then come up with the relevant API endpoint

as we create the react component we will create a corresponding test, we will follow TDD, and keep things as simple as possible


Changelog:

- 4/29/2025 22:34: Started work with agent, agent will summarize significant functional increments below:
- 4/29/2025 22:41: PatientSurveys component and test created in plain JSX, passing test. Confirmed that all data structures for forms are 1:1 with backend (single id field).
- 4/29/2025 22:42: Designed FormSelector subcomponent (dropdown) to use [{ id }] as per schema_ddl.sql and Form dataclass. Implemented in its own subfolder as per Screaming Architecture. Test covers rendering and selection.