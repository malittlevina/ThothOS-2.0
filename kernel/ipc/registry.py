# kernel/ipc/registry.py
"""
In-memory service registry with TTL + heartbeat.
Matches the Cap’n Proto shapes in kernel/ipc/idl.capnp.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List, Optional
import time
import threading

@dataclass
class ServiceId:
    name: str               # e.g. "thoth.registry"
    version: str            # e.g. "0.1.0"

@dataclass
class Endpoint:
    addr: str               # e.g. "unix:///run/thoth/registry.sock"
    locality: str = "local" # "local", "numa0", "remote"

@dataclass
class ServiceRecord:
    id: ServiceId
    endpoint: Endpoint
    features: int
    expires_at_ms: int

class Registry:
    def __init__(self):
        self._lock = threading.RLock()
        self._services: Dict[str, ServiceRecord] = {}  # key = ServiceId.name

    # internal
    def _now_ms(self) -> int:
        return int(time.time() * 1000)

    def _gc_expired(self) -> None:
        now = self._now_ms()
        expired = [k for k, v in self._services.items() if v.expires_at_ms <= now]
        for k in expired:
            self._services.pop(k, None)

    # API
    def register(self, name: str, version: str, addr: str, ttl_sec: int, features: int = 0, locality: str = "local") -> bool:
        with self._lock:
            self._gc_expired()
            exp = self._now_ms() + ttl_sec * 1000
            rec = ServiceRecord(
                id=ServiceId(name=name, version=version),
                endpoint=Endpoint(addr=addr, locality=locality),
                features=features,
                expires_at_ms=exp,
            )
            self._services[name] = rec
            return True

    def heartbeat(self, name: str, ttl_sec: int) -> bool:
        with self._lock:
            rec = self._services.get(name)
            if not rec:
                return False
            rec.expires_at_ms = self._now_ms() + ttl_sec * 1000
            return True

    def resolve(self, name: str, min_version: str = "", locality: str = "") -> Optional[ServiceRecord]:
        with self._lock:
            self._gc_expired()
            rec = self._services.get(name)
            if not rec:
                return None
            if min_version and rec.id.version < min_version:
                return None
            if locality and rec.endpoint.locality != locality:
                return None
            return rec

    def list(self, prefix: str = "", locality: str = "") -> List[ServiceRecord]:
        with self._lock:
            self._gc_expired()
            out: List[ServiceRecord] = []
            for rec in self._services.values():
                if prefix and not rec.id.name.startswith(prefix):
                    continue
                if locality and rec.endpoint.locality != locality:
                    continue
                out.append(rec)
            return out

# Singleton
REGISTRY = Registry()
