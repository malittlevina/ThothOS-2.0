# Decisions (ADR-lite)

- Language strategy: Python orchestration; Rust for IPC/parsers/drivers; optional Prolog/Julia where beneficial.
- Security model: Capability-based permissions per IPC endpoint; signed/versioned modules.
- Persistence: Codex snapshots + rollback/restore; optional cloud backup.
- Energy conservation: DVFS, tickless kernel, runtime PM.
- Repo: Private GitHub under `malittlevina` initially; monorepo with clear component boundaries.
