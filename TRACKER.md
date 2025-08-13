# ThothOS Upgrade Tracker (Restart)

## Milestone 1 — IPC Fabric v2
| Task ID | Task | Description | Dependency Modules | Owner | % | Notes |
|---|---|---|---|---|---|---|
| IPC-1 | Define IDL format | Versioned schema + feature flags | kernel/ipc | malittlevina | 0 |  |
| IPC-2 | Shared-memory rings | Zero-copy transport for large payloads | kernel/ipc, kernel/observability |  | 0 |  |
| IPC-3 | Inline fast path | Optimize small control messages | kernel/ipc |  | 0 |  |
| IPC-4 | Service registry | Discovery, health, locality routing | kernel/ipc | malittlevina | 0 |  |
| IPC-5 | Contract tests | Wire protocol tests pre-activation | kernel/ipc, tools |  | 0 |  |

## Milestone 2 — Energy-Aware Scheduling
| Task ID | Task | Description | Dependency Modules | Owner | % | Notes |
|---|---|---|---|---|---|---|
| SCHED-1 | DVFS hints | Adjust P/C states by load | kernel/sched, kernel/pm |  | 0 |  |
| SCHED-2 | Tickless kernel | Remove periodic timer interrupts | kernel/sched | malittlevina | 0 |  |
| SCHED-3 | Timer batching | Batch timers & I/O completions | kernel/sched, kernel/ipc |  | 0 |  |
| SCHED-4 | I/O-aware scheduling | Align threads with I/O events | kernel/sched, kernel/ipc |  | 0 |  |

## Milestone 3 — Runtime Power Mgmt
| Task ID | Task | Description | Dependency Modules | Owner | % | Notes |
|---|---|---|---|---|---|---|
| PM-1 | Driver PM states | Wake latencies + power states | kernel/pm |  | 0 |  |
| PM-2 | PM policy engine | Select device states per workload | kernel/pm |  | 0 |  |
| PM-3 | Interrupt moderation | Adaptive NIC/storage batching | kernel/pm |  | 0 |  |
| PM-4 | FS writeback alignment | Delay writes to low-power windows | kernel/pm, codex |  | 0 |  |

## Milestone 4 — Observability & Contention
| Task ID | Task | Description | Dependency Modules | Owner | % | Notes |
|---|---|---|---|---|---|---|
| OBS-1 | Tracing integration | Service IDs, timestamps, sizes | kernel/observability |  | 0 |  |
| OBS-2 | eBPF-like probes | Event hooks (kernel/user) | kernel/observability |  | 0 |  |
| OBS-3 | Power/latency dashboards | Correlate CPU states & IPC latency | kernel/observability |  | 0 |  |
| OBS-4 | Lock contention profiler | Identify & refactor hotspots | kernel/observability |  | 0 |  |

## Milestone 5 — SMP/NUMA Scaling & Sharding
| Task ID | Task | Description | Dependency Modules | Owner | % | Notes |
|---|---|---|---|---|---|---|
| SCALE-1 | NUMA placement | Local allocations per CPU domain | kernel/sched, unimind |  | 0 |  |
| SCALE-2 | Per-CPU locks | Reduce global lock contention | kernel |  | 0 |  |
| SCALE-3 | Multi-instance services | Registry load-balances | kernel/ipc |  | 0 |  |
| SCALE-4 | Service affinity | Route requests to local shard | kernel/ipc |  | 0 |  |
