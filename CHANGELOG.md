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

### 8. Dependency Injection
- Gateways are instantiated with an active database connection and injected into the application layer, allowing for easy swapping of backends or mocking in tests.

---

## Summary
- The codebase is now modular, testable, and scalable.
- All business logic is encapsulated in the domain layer; persistence is handled by gateways; and the application layer is clean and focused.
- The design supports future extension (e.g., new storage backends, new validation rules) with minimal changes to the core logic.
