# CHANGELOG

## Architectural & Design Decisions

### 1. Clean Architecture & Screaming Architecture
- Adopted Clean Architecture principles, separating domain, adapters, and infrastructure layers.
- Directory structure makes business features and boundaries obvious (Screaming Architecture).

### 2. Domain Entities as Dataclasses
- Core business entities (`Submission`, `Answer`, `Question`, `Patient`, `Form`) are defined as Python dataclasses for immutability, type safety, and easy instantiation.
- Entities encapsulate their own logic (e.g., `Submission` handles ISO8601-to-unix timestamp conversion internally).

### 3. Database Schema & Type Validation
- Removed SQL-level type constraints on the `questions` table to allow dynamic question types.
- All type validation for questions is performed programmatically in Python, using a set of allowed types (`ALLOWED_QUESTION_TYPES`).

### 4. Gateways & Persistence
- All database access is encapsulated in Gateway interfaces (in `adapters/gateways/`) and MySQL implementations (in `infrastructure/gateways/`).
- Gateways use efficient bulk-insert operations where possible (e.g., `MySQLAnswerGateway.save` supports both single and bulk inserts).
- The application layer never accesses SQL directly.

### 5. Submission & Answer Loading
- Submissions and Answers are loaded from JSON using `from_dict` classmethods, which handle all necessary field mapping and type conversion.
- Question text is used as the unique identifier for answers in a submission, not the outer JSON keys (e.g., `q1`, `q2`).

### 6. Unique ID Generation
- Answer IDs are generated using a deterministic SHA-256 hash of `submission_id`, `question_id`, and value (no salt), making them unique and non-reversible.

### 7. Validation
- Question types are validated before any database operation to ensure only allowed types are processed.

### 8. Dependency Injection & Abstraction
- Gateways are instantiated with an active database connection and injected into the application layer, allowing for easy swapping of backends or mocking in tests.
- **SubmissionRepository** abstract class added at the domain layer, with a concrete MySQL implementation at the infrastructure layer.
- The repository now encapsulates the use of both submission and answer gateways, so the application layer only interacts with the repository for persistence (except for question validation).
- The application layer is now completely decoupled from SQL and gateway logic.

### 9. Feature Slices & Use Cases
- Introduced a `slices/save_submission` feature folder, organizing code by feature and Clean Architecture layer.
- Created a `SaveSubmissionUseCase` class in the usecase layer, encapsulating business logic for saving submissions and answers, including question type validation.
- The use case returns a tuple (response dict, status code) for the endpoint to handle HTTP response logic.

### 10. Strict Dependency Rule Enforcement
- Use cases and domain logic now depend only on domain-level interfaces (e.g., `SubmissionRepository`), never on infrastructure implementations.
- All infrastructure dependencies are injected at the application layer, ensuring the domain and use case layers are fully decoupled from technology choices and persistence details.
- Imports in the use case and domain layers reference only abstractions, not concrete classes.

### 11. Code Cleanup
- Removed obsolete helpers and unused constants from the application layer.
- Only methods that are actually used are defined in repositories and gateways, keeping the API minimal and focused.

## [2025-04-28] Refactor: Fractal Clean Architecture & Controller Placement

- Refactored the project to strictly follow fractal Clean Architecture principles at the feature slice level.
- Moved all controller abstractions and implementations for the `save_submission` feature into the slice's `adapters` and `infrastructure` folders, respectively.
- Removed all redundant or duplicate controllers and abstract classes outside the slice to ensure all abstractions are local and reusable within their feature.
- Updated all imports and infrastructure wiring to use the new controller locations.
- The application layer (Flask routes) now depends only on the infrastructure controller, which wires up repositories and use cases per Clean Architecture.
- Updated the codebase to be modular, testable, and ready for further feature slices or infrastructure implementations.

---

## Summary
- The codebase is now modular, testable, and scalable.
- All business logic is encapsulated in the domain and use case layers; persistence is handled by gateways and repositories; and the application layer is clean and focused.
- The design supports future extension (e.g., new storage backends, new validation rules, new feature slices) with minimal changes to the core logic.
