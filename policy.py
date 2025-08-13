# kernel/pm/policy.py (stub)
"""Runtime power policy engine."""
from dataclasses import dataclass

@dataclass
class DeviceState:
    name: str
    power_state: str  # D0..D3hot/D3cold
    wake_latency_ms: int

def choose_state(latency_budget_ms: int) -> str:
    if latency_budget_ms < 1:
        return "D0"
    if latency_budget_ms < 10:
        return "D1"
    if latency_budget_ms < 50:
        return "D2"
    return "D3hot"
