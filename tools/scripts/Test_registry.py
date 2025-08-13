# tools/scripts/test_registry.py
from kernel.ipc.registry import REGISTRY

def main():
    print("register…")
    ok = REGISTRY.register(
        name="thoth.registry",
        version="0.1.0",
        addr="unix:///tmp/thoth-reg.sock",
        ttl_sec=5,
        features=0b0001,
        locality="local",
    )
    print("register ok:", ok)

    print("list all:")
    for rec in REGISTRY.list():
        print(" -", rec)

    print("resolve thoth.registry:")
    rec = REGISTRY.resolve("thoth.registry")
    print(" ->", rec)

    print("heartbeat (extend TTL)…")
    print("hb ok:", REGISTRY.heartbeat("thoth.registry", ttl_sec=10))

if __name__ == "__main__":
    main()
