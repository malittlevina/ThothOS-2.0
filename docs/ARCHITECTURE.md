# ThothOS Master Document (Restart Baseline)

## 1. Core Vision & Principles
ThothOS is a modular, symbolic, emotionally intelligent operating system built around:
- Microkernel-style modularity
- Symbolic computing (glyphs, scrolls, ritual logic)
- Emotionally aware daemons
- Scalable integration (edge → XR)
- Ethical intelligence

Primary daemon: **Prometheus (Prom)** — evolving companion.

## 2. Architecture Overview
### Kernel Layer
- IPC Fabric v2 (IDL, zero-copy messaging, service registry)
- Energy-aware scheduler (DVFS, tickless)
- Runtime Power Management (device PM states, policy engine)
- Capability-based security
- Observability (tracing, lock-profiler, dashboards)

### Unimind
- Brain nodes, persona router
- Ethics modules: Contradiction Detector, Compassion-Logic Harmonizer, Recursive Ethical Simulator, Meta-Ethics Debater

### Codex
- Vector store, symbolic memory graph, timeline
- Web/PDF ingestion

### Daemon Layer
- Prom core & personas, Mirror Daemons, Oracle/Architect debate

### Scrolls & Rituals
- Registry, composer, triggers (voice, event, schedule)
- Optimize Self (daily) & Parting Rituals (safety)

### Symbolic UI / GlyphForge
- God UI overlays, glyph language
- Modeling suite, node editor, ritual timeline
- Tree of Life UI (22 Hermetic Scrolls, Sephirot glyphs)

### StoryRealms
- Realm editor, GhostEye, rating/featured realms

### Bridges
- realm_interface.py, memory_tree_interface.py, thoth_bridge.py, thirdparty_gateway.py

## 3. Active Modules & Status
(see docs/TRACKER.md)

## 4. Implementation Decisions
- Python orchestration; Rust for IPC/parsers/drivers; optional Prolog/Julia
- Capabilities, signed/versioned modules
- Codex snapshots, rollback/restore, cloud backup
- DVFS, tickless kernel, runtime PM

## 5. Roadmap (Restart)
Phase 1 — Core Foundations
1) IPC Fabric v2
2) Energy-aware scheduler (tickless)
3) Runtime PM
4) Capability security scaffold

Phase 2 — Intelligence Core
5) Codex + symbolic memory graph
6) Persona system + drift
7) Ethics subsystems

Phase 3 — Symbolic & Interactive
8) Scroll Engine + Optimize Self
9) GlyphForge
10) Tree of Life UI

Phase 4 — Immersive Expansion
11) StoryRealms + GhostEye
12) XR HUD + God UI
13) Multi-instance realm hosting

## 6. Next Actions
- Create scaffolds in /kernel, /unimind, /daemons, /codex, /scrolls
- Implement IDL and service registry stub
- Add observability hooks
