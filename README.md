
Your system receives structured JSON submissions from external forms filled out by users.
Each form has a unique ID and a list of questions.

The structure of each submission is consistent within a form, but can vary significantly across forms.
    - Different sets of questions.
    - Varying formats (strings, dicts, arrays, matrices, etc.)
    - Optional or missing fields.
Some of the known structures are defined on the sample data, but there could be new structures, so your program should be flexible enough to handle them and avoid errors.

Your solution should be able to:

- [x] Parse a single survey submission and extract the relevant data.
- [x] Normalize the output into a consistent internal representation.
- [x] Store the internal representation in a database of your choice (relational or NoSQL).
- [x] Support querying the database for analytics, such as:
    - "Patients without insurance"
    - "Clinical data for patient X"
- [x] Be able to extend to new forms.
- [ ] Build a simple react component to show surveys for a patient with all the questions and answers.
    - Include a selector to select by form type


# Assumptions

- Assuming patient IDs are created beforehand by an administrator
