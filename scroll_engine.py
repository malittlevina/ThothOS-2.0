# scrolls/engine/scroll_engine.py (stub)
from typing import Callable, Dict

_HANDLERS: Dict[str, Callable] = {}

def register(name: str, fn: Callable):
    _HANDLERS[name] = fn

def invoke(name: str, **kwargs):
    fn = _HANDLERS.get(name)
    if not fn:
        raise KeyError(f"Unknown scroll: {name}")
    return fn(**kwargs)
