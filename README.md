# Architectural Overview & Design Patterns

This project is built with a strong emphasis on maintainability, scalability, and clarity, following modern software architecture and development best practices:

- **Clean Architecture**: The codebase is structured with clear separation of concerns:
  - **Domain Layer**: Core business logic and entities as Python dataclasses.
  - **Use Case/Application Layer**: Encapsulates business workflows.
  - **Adapters/Infrastructure Layer**: Handles persistence and external interactions.
- **Vertical Slicing**: Features are organized into self-contained slices (e.g., `save_submission`, `patient_analytics`), each with its own domain, use case, adapters, and infrastructure.
- **Screaming Architecture**: Directory and file structure make business features and boundaries obvious at a glance.
- **Domain-Driven Design (DDD)**: Uses entities, repositories, gateways, value objects, and bounded contexts. Each feature slice acts as its own bounded context, with dedicated models and logic.
- **Dependency Injection**: Use cases and controllers receive repositories/gateways via constructor injection, allowing for easy swapping, testing, and mocking. The application and domain layers never reference infrastructure details directly.
- **Thin Controllers & Pure Routing**: API controllers delegate all business logic to use cases and repositories. Flask routes act as pure HTTP routers, with all business and persistence logic encapsulated in controllers and use cases.
- **Centralized Validation & Type Safety**: Question types are validated against a central set before any persistence. Domain entities enforce types via dataclasses, reducing runtime errors.
- **TDD/BDD**: Test suite for React components and backend logic follows Given/When/Then structure, with descriptive describe/it blocks (e.g., “Then should ...”).
- **CDD**: Consistent naming conventions and code organization, making intent and structure clear.
- **Minimal APIs & Cleanup**: Only necessary methods are exposed in repositories/gateways. Unused helpers and constants are removed for clarity. Imports are alphabetized for readability and to minimize merge conflicts.

---

# Project Summary
- The codebase exemplifies Clean Architecture, DDD, vertical slicing, and best practices for maintainability and testability.
- All business logic is encapsulated in the domain and use case layers; persistence is handled by gateways and repositories; and the application layer is clean and focused.
- The design supports future extension (e.g., new storage backends, new validation rules, new feature slices) with minimal changes to the core logic.

---

# System Overview

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
