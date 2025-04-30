# ADR-2: Vertical Slicing

**Status:** Accepted  
**Context:**  
Feature work should be modular and independently deployable.

**Decision:**  
Organize code into vertical feature slices (e.g., save_submission, patient_analytics), each with its own models, use cases, and adapters.

**Consequences:**  
- Features are self-contained and scalable.
- Teams can work in parallel with minimal conflicts.
