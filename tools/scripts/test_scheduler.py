# tools/scripts/test_scheduler.py
from kernel.sched.scheduler import TicklessScheduler, apply_dvfs_hint
import time

def main():
    s = TicklessScheduler()
    now_ms = lambda: int(time.time() * 1000)

    # Schedule three timers ~500ms apart, coalescing the last two by 200ms
    base = now_ms() + 400
    s.add_timer_abs(base, slack_ms=0,   tag="t1")
    s.add_timer_abs(base + 500, slack_ms=200, tag="t2")
    s.add_timer_abs(base + 650, slack_ms=200, tag="t3")  # within t2 slack ⇒ coalesced

    fired = []
    s.run_until_idle(lambda tag, tid: fired.append((tag, tid)))

    print("fired:", fired)
    print("dvfs(0.1) =", apply_dvfs_hint(0.1))
    print("dvfs(0.5) =", apply_dvfs_hint(0.5))
    print("dvfs(0.9) =", apply_dvfs_hint(0.9))

if __name__ == "__main__":
    main()
