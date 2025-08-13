# kernel/sched/scheduler.py
"""
Tickless scheduler simulation:
- No periodic tick
- Wakes only for the next due timer
- Coalesces timers within 'slack' window
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Callable, List, Tuple
import heapq, time

# --- DVFS hint (kept from stub)
def apply_dvfs_hint(load: float) -> str:
    if load < 0.2:
        return "low_power"
    if load < 0.7:
        return "balanced"
    return "performance"

@dataclass(order=True)
class _Timer:
    due_ms: int
    id: int
    slack_ms: int
    tag: str

class TicklessScheduler:
    def __init__(self):
        self._q: List[_Timer] = []
        self._next_id = 1

    def _now_ms(self) -> int:
        return int(time.time() * 1000)

    def add_timer_abs(self, when_ms: int, slack_ms: int = 0, tag: str = "") -> int:
        tid = self._next_id; self._next_id += 1
        heapq.heappush(self._q, _Timer(due_ms=when_ms, id=tid, slack_ms=slack_ms, tag=tag))
        return tid

    def cancel(self, tid: int) -> bool:
        # lazy cancel: mark by removing when popped (simple demo)
        for i, t in enumerate(self._q):
            if t.id == tid:
                self._q[i] = self._q[-1]
                self._q.pop()
                heapq.heapify(self._q)
                return True
        return False

    def run_once(self, on_fire: Callable[[str, int], None]) -> bool:
        """Run until next batch fires (single wake). Returns False if idle."""
        if not self._q:
            return False

        # Peek next timer
        nxt = self._q[0]
        now = self._now_ms()
        sleep_ms = max(0, nxt.due_ms - now)
        if sleep_ms > 0:
            time.sleep(sleep_ms / 1000.0)

        # Wake: fire all timers due within coalescing window
        now = self._now_ms()
        fired: List[_Timer] = []
        while self._q and (self._q[0].due_ms - now) <= max(0, self._q[0].slack_ms):
            fired.append(heapq.heappop(self._q))

        for t in fired:
            on_fire(t.tag or "timer", t.id)

        return True

    def run_until_idle(self, on_fire: Callable[[str, int], None]):
        while self.run_once(on_fire):
            pass

# Convenience coalescer for simple lists (kept from stub API)
def coalesce_timers(timers: List[int]) -> List[int]:
    return sorted(timers)
