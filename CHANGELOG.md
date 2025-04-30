# CHANGELOG

## [2025-04-28] Clean Architecture & Modular Design
- **Clean Architecture** (see [[ADR-1]]): The codebase is structured with clear separation of concerns:
  - **Domain Layer**: Contains core business logic and entities as Python dataclasses (Submission, Answer, Question, Patient, Form).
  - **Use Case/Application Layer**: Encapsulates business workflows (e.g., SaveSubmissionUseCase).
  - **Adapters/Infrastructure Layer**: Handles persistence (MySQL gateways/repositories) and external interactions.
- **Vertical Slicing** (see [[ADR-2]]): Features are organized into self-contained slices (e.g., save_submission, patient_analytics), each with its own domain, use case, adapters, and infrastructure, promoting modularity and scalability.
- **Screaming Architecture** (see [[ADR-3]]): Directory and file structure make business features and boundaries obvious at a glance.

## [2025-04-28] Domain-Driven Design (DDD) Patterns
- **Entities**: Core models are Python dataclasses, enforcing immutability and encapsulating business rules.
- **Repositories**: Abstract interfaces (e.g., SubmissionRepository) decouple domain logic from persistence.
- **Gateways**: Infrastructure gateways (e.g., MySQLAnswerGateway, MySQLSubmissionGateway) implement persistence logic, supporting both single and bulk inserts.
- **Value Objects & Aggregates**: Entity IDs (e.g., Answer.id) are deterministically generated from business data, ensuring uniqueness and integrity.
- **Bounded Contexts**: Each feature slice acts as its own bounded context, with dedicated models and logic. (see [[ADR-5]])

## [2025-04-28] Dependency Injection & Decoupling
- **Dependency Injection**: Use cases and controllers receive repositories/gateways via constructor injection, allowing for easy swapping, testing, and mocking.
- **Decoupling**: The application and domain layers never reference infrastructure details directly; all dependencies are injected. (see [[ADR-1]])

## [2025-04-28] Controller & Routing Patterns
- **Thin Controllers**: API controllers (e.g., SaveSubmissionApiController) delegate all business logic to use cases and repositories.
- **Pure Routing**: Flask routes act as pure HTTP routers, with all business and persistence logic encapsulated in controllers and use cases.

## [2025-04-28] Validation & Type Safety
- **Centralized Validation**: Question types are validated against a central set (ALLOWED_QUESTION_TYPES) in the use case layer before any persistence.
- **Type Safety**: Domain entities enforce types via dataclasses, reducing runtime errors. (see [[ADR-1]])

## [2025-04-28] Test-Driven & Convention-Driven Development
- **TDD/BDD**: Test suite for React components and backend logic follows Given/When/Then structure, with descriptive describe/it blocks (e.g., “Then should ...”).
- **CDD** (see [[ADR-4]]): Consistent naming conventions and code organization, making intent and structure clear.

## [2025-04-28] Code Cleanup & Maintainability
- **Minimal APIs**: Only necessary methods are exposed in repositories/gateways.
- **Removed Obsolete Code**: Unused helpers and constants removed for clarity.
- **Alphabetized Imports**: All imports are alphabetized for readability and to minimize merge conflicts.
- **Fractal File Structure** (see [[ADR-6]]): Project organization supports modularity and scalability.

## [2025-04-29] Refactor & Test Suite Improvements
- Refactored all React test files to strictly follow the Given/When/Then structure.
- Updated all it block descriptions to “Then should ...” for clarity and consistency.
- Ensured all test logic and assertions remain unchanged; only structure and naming improved.
- Ran the full test suite and verified all tests pass after changes.
- Built the project successfully after refactor.

## [2025-04-28] Fractal Feature Slices & Controller Placement
- Controllers and abstractions are colocated within their feature slice (slices/save_submission), ensuring all abstractions are local and reusable.
- The application layer depends only on infrastructure controllers, which wire up repositories and use cases per Clean Architecture.
