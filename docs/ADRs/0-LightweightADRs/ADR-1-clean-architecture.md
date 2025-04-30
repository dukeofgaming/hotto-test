# ADR-1: Clean Architecture

**Status:** Accepted  
**Context:**  
We need a maintainable, testable, and decoupled backend structure.

**Decision:**  
Adopt Clean Architecture: separate domain, use case, and adapter layers.

**Consequences:**  
- Business logic is isolated from infrastructure.
- Easier testing and future refactoring.
