# ThothOS (Restart Baseline)

This repository is the clean restart of **ThothOS** based exclusively on prior ChatGPT architecture work.

- **docs/ARCHITECTURE.md** — master reference for the system
- **docs/TRACKER.md** — milestones & tasks mapped to subsystems
- **docs/DECISIONS.md** — decision log (ADR-lite)
- **kernel/** — microkernel-style services: IPC, scheduler, PM, security, observability
- **unimind/** — brain-node architecture, ethics, memory
- **daemons/** — Prom (primary daemon), Mirrors, Oracle/Architect
- **codex/** — vector store, symbolic memory graph, timeline
- **scrolls/** — engine, registry, rituals (incl. optimize_self)
- **storyrealms/** — realm editor, GhostEye, rating
- **glyphforge/** — symbolic modeling suite
- **bridges/** — external integrations & app connectors
- **xr/** — HUD & overlays

## Quickstart
1. Read `docs/ARCHITECTURE.md`.
2. Open `docs/TRACKER.md` and start with Milestone 1 (IPC Fabric v2).
3. Run `tools/scripts/dev_env_check.sh` to verify local tooling (edit as needed).
