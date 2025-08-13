# Optimize Self (Scroll)

**Purpose:** Daily self-optimization routine.

**Triggers:** Scheduled daily at 03:00 (local).  
**Actions:** 
- Run tests, static analysis, and lint.
- Snapshot Codex state.
- Suggest refactors; open issues for risky changes.
- If safe: rebuild modules; if risky: queue for review.

**Guardrails:**
- No destructive action without snapshot.
- Respect capability checks & power policies.
