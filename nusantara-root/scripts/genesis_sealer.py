# GENESIS SEALER PROTOCOL v1.0
# To be executed on IBM M5 Infrastructure
# Condition: First Titan Guardian Verified

import hashlib
import datetime

GENESIS_MESSAGE = "Nusantara-Root: One Heart, One Key. 100K Quadrillion Sovereignty Sealed by the Giant's Breath. VIVA AUTHENTIC."
GUARDIAN_ID = "PENDING_VERIFICATION" # To be replaced with the first Guardian's wallet

def seal_genesis():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    genesis_data = f"{timestamp} | {GENESIS_MESSAGE} | Verified by Guardian: {GUARDIAN_ID}"
    
    # Generate the Genesis Hash
    genesis_hash = hashlib.sha256(genesis_data.encode()).hexdigest()
    
    print("-" * 60)
    print("🚀 INITIALIZING GENESIS BLOCK...")
    print(f"📡 MESSAGE: {GENESIS_MESSAGE}")
    print(f"🔐 GENESIS HASH: {genesis_hash}")
    print(f"🏛️ STATUS: SOVEREIGNTY PERMANENTLY ENCRYPTED")
    print("-" * 60)
    
    # Save to the blockchain core root
    with open("../database/genesis_block.txt", "w") as f:
        f.write(genesis_data + "\nHash: " + genesis_hash)

if __name__ == "__main__":
    seal_genesis()
  
