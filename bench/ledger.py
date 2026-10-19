import json
import os

def record_audit_manifest(conn):
    manifest_path = os.getenv('STS_AUDIT_MANIFEST', '/workspace/data/audit_manifest.json')
    if os.path.exists(manifest_path):
        with open(manifest_path, 'r') as f:
            manifest = json.load(f)
        # Record the agent/integration session into the ledger initialization state
        conn.execute(
            "INSERT OR IGNORE INTO ledger_events (seq, payload, hash) VALUES (0, ?, ?)",
            (json.dumps(manifest), "GENESIS_AUDIT_BINDING")
        )
        conn.commit()
