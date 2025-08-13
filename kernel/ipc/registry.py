# kernel/ipc/registry.py (stub)
"""Service discovery & health registry (local-only to start)."""

from dataclasses import dataclass
from typing import Dict, Optional, List
import time

@dataclass
class Service:
    name: str
    version: str
    addr: str
    last_heartbeat: float
    locality: str = "local"

class Registry:
    def __init__(self):
        self._services: Dict[str, Service] = {}

    def register(self, name: str, version: str, addr: str, locality: str = "local"):
        self._services[name] = Service(name, version, addr, time.time(), locality)

    def heartbeat(self, name: str):
        if name in self._services:
            self._services[name].last_heartbeat = time.time()

    def resolve(self, name: str) -> Optional[Service]:
        return self._services.get(name)

    def list(self) -> List[Service]:
        return list(self._services.values())

REGISTRY = Registry()
