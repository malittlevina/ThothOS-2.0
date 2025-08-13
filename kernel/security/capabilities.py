# kernel/security/capabilities.py (stub)
"""Capability objects and checks."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Capability:
    subject: str
    action: str
    resource: str
    ttl_s: int = 300

def check(cap: Capability, action: str, resource: str) -> bool:
    return cap.action == action and cap.resource == resource
