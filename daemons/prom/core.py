# daemons/prom/core.py (stub)
from ..oracle_architect.debate import debate_once

def respond(prompt: str) -> str:
    # TODO: route by persona & context
    pro, con = debate_once(prompt)
    return f"PROM> {pro} | {con}"
