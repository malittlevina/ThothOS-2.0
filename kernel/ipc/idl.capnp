@0xbf5147d580e2ec4a;  # ThothOS IPC v0.1 (restart baseline)

using Cxx = import "/capnp/c++.capnp";  # optional for generators

# ──────────────────────────────────────────────────────────────────────────────
# Versioning notes
# - Add fields only at the end of structs (append-only).
# - Never reuse or reorder field IDs.
# - Prefer optional/union arms for extensibility.
# - Use featureFlags for capability negotiation at connect time.
# ──────────────────────────────────────────────────────────────────────────────

struct MessageHeader {
  serviceName  @0 :Text;     # logical service (e.g., "registry", "scheduler", "codex")
  version      @1 :UInt16;   # semantic minor only here (major in serviceName if needed)
  messageType  @2 :Text;     # "PingRequest", "Registry.RegisterRequest", etc.
  featureFlags @3 :UInt32;   # bitset negotiated per-connection
  traceId      @4 :UInt64;   # optional tracing id (0 = none)
}

struct Error {
  code    @0 :UInt32;        # 0 = OK
  message @1 :Text;
}

# Generic envelope so transports can route without knowing concrete types.
struct Envelope {
  header @0 :MessageHeader;
  body   @1 :Data;           # serialized payload of the concrete message
}

# ──────────────────────────────────────────────────────────────────────────────
# Ping (smoke test)
# ──────────────────────────────────────────────────────────────────────────────
struct PingRequest { header @0 :MessageHeader; }
struct PingResponse {
  header @0 :MessageHeader;
  pong   @1 :Text;           # "pong"
  err    @2 :Error;          # code=0 when OK
}

# ──────────────────────────────────────────────────────────────────────────────
# Registry API (IPC-4)
# ──────────────────────────────────────────────────────────────────────────────
struct ServiceId {
  name     @0 :Text;         # unique logical name, e.g. "thoth.registry"
  version  @1 :Text;         # semver string, e.g. "0.1.0"
}

struct Endpoint {
  # Examples: "unix:///run/thoth/registry.sock", "tcp://127.0.0.1:7011"
  addr     @0 :Text;
  locality @1 :Text;         # "local", "numa0", "remote", etc.
}

struct RegisterRequest {
  header    @0 :MessageHeader;
  id        @1 :ServiceId;
  endpoint  @2 :Endpoint;
  ttlSec    @3 :UInt32;      # heartbeat interval requirement
  features  @4 :UInt32;      # advertised feature bits for negotiation
}

struct RegisterResponse {
  header @0 :MessageHeader;
  ok     @1 :Bool;
  err    @2 :Error;          # code != 0 on failure
}

struct HeartbeatRequest {
  header @0 :MessageHeader;
  id     @1 :ServiceId;
}
struct HeartbeatResponse {
  header @0 :MessageHeader;
  ok     @1 :Bool;
  err    @2 :Error;
}

struct ResolveRequest {
  header   @0 :MessageHeader;
  name     @1 :Text;         # service logical name
  minVers  @2 :Text;         # minimum compatible version (semver), "" = any
  locality @3 :Text;         # "" = any; "local" preferred; future: list
}
struct ResolveResponse {
  header   @0 :MessageHeader;
  found    @1 :Bool;
  id       @2 :ServiceId;
  endpoint @3 :Endpoint;
  features @4 :UInt32;
  err      @5 :Error;
}

struct ListRequest {
  header   @0 :MessageHeader;
  prefix   @1 :Text;         # filter by name prefix; "" = all
  locality @2 :Text;         # optional filter
}
struct ListResponse {
  header   @0 :MessageHeader;
  services @1 :List(ServiceRecord);
  err      @2 :Error;

  struct ServiceRecord {
    id       @0 :ServiceId;
    endpoint @1 :Endpoint;
    features @2 :UInt32;
    expiresAtEpochMs @3 :UInt64;  # for TTL visibility
  }
}

# Optional Cap’n Proto interfaces (nice for RPC codegen; you can also use raw messages).
interface Registry {
  register  @0 (req :RegisterRequest) -> (res :RegisterResponse);
  heartbeat @1 (req :HeartbeatRequest) -> (res :HeartbeatResponse);
  resolve   @2 (req :ResolveRequest)   -> (res :ResolveResponse);
  list      @3 (req :ListRequest)      -> (res :ListResponse);
}

# ──────────────────────────────────────────────────────────────────────────────
# Scheduler surface (SCHED-2 bring-up)
# ──────────────────────────────────────────────────────────────────────────────
enum TaskClass {
  idle      @0;
  background@1;
  latency   @2;    # interactive, low-latency
  batch     @3;
}

struct AddTimerRequest {
  header    @0 :MessageHeader;
  whenMs    @1 :UInt64;    # absolute epoch ms
  slackMs   @2 :UInt32;    # coalescing window (0 = exact)
  class     @3 :TaskClass; # helps DVFS/timer policy
  tag       @4 :Text;      # user label
}
struct AddTimerResponse {
  header @0 :MessageHeader;
  ok     @1 :Bool;
  id     @2 :UInt64;       # timer id
  err    @3 :Error;
}

struct CancelTimerRequest {
  header @0 :MessageHeader;
  id     @1 :UInt64;
}
struct CancelTimerResponse {
  header @0 :MessageHeader;
  ok     @1 :Bool;
  err    @2 :Error;
}

interface Scheduler {
  addTimer    @0 (req :AddTimerRequest)    -> (res :AddTimerResponse);
  cancelTimer @1 (req :CancelTimerRequest) -> (res :CancelTimerResponse);
}
