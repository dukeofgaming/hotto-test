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
- [x] Build a simple react component to show surveys for a patient with all the questions and answers.
    - Include a selector to select by form type

# Running this project


1. Copy .env.dist to .env
2. Build and run with docker compose:
```bash
docker compose up --build
```
3. Access the application at http://localhost:80


# Architectural Decision Records (ADRs)

This project follows a set of architectural patterns for maintainability, modularity, and clarity. For details on architecture and design decisions, see the following ADRs:

- Clean Architecture (see [[ADR-1]])
- Vertical Slicing (see [[ADR-2]])
- Screaming Architecture (see [[ADR-3]])
- Component Driven Development (see [[ADR-4]])
- Domain Driven Design (see [[ADR-5]])
- Fractal File Structure (see [[ADR-6]])
- Docs as Code (see [[ADR-7]])

For implementation details and rationale, refer to the ADRs directory.

# Architectural Overview & Design Patterns

This project is designed for maintainability, scalability, and clarity using modern architecture patterns:

- **Clean Architecture**: Clear separation of concerns—domain logic, use cases, and infrastructure are isolated. All business logic lives in the domain and use case layers; persistence is handled by gateways and repositories.
- **Vertical Slicing**: Features are organized into self-contained slices (e.g., `save_submission`, `patient_analytics`), each with its own domain, use case, adapters, and infrastructure.
- **Screaming Architecture**: The directory structure makes business features and boundaries obvious.
- **Domain-Driven Design (DDD)**: Uses entities, repositories, gateways, and value objects. Each slice is a bounded context with dedicated models and logic.
- **Dependency Injection**: Use cases and controllers receive repositories/gateways via constructor injection for easy testing and swapping. The core never references infrastructure directly.
- **Thin Controllers & Pure Routing**: API controllers only route requests; all business and persistence logic is in use cases and controllers.
- **Centralized Validation & Type Safety**: Question types are validated centrally before persistence. Domain entities use dataclasses for type safety.
- **Testing**: Test suites for React and backend logic use clear Given/When/Then structure. Naming and organization are consistent and descriptive.
- **Minimal APIs & Cleanup**: Only necessary methods are exposed. Unused code is removed and imports are alphabetized for clarity.

The design supports easy extension (e.g., new storage backends, validation rules, or feature slices) with minimal changes to core logic.

---

# Assumptions

- Assuming patient IDs are created beforehand by an administrator
