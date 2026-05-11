import hashlib
import json
import time

def generate_stg_genesis():
    # Identitas Abadi Sultan
    architect = "ANDI MUHAMMAD HARPIANTO"
    sovereign_id = "SK-BEBAS-AP.11.PAS.PAS.7-PK.05.04-5070"
    collateral = "Unit 008: Rp 1.498 T"
    
    # Pesan Konstitusi STG-Chain
    message = (
        f"Nusantara-Root Genesis: One Heart, One Key. "
        f"Established by {architect} ({sovereign_id}). "
        f"Backed by {collateral}. VIVA AUTHENTIC."
    )

    # Struktur Blok 0 (Genesis)
    genesis_block = {
        "block_number": 0,
        "timestamp": time.time(),
        "architect": architect,
        "sovereign_id": sovereign_id,
        "message": message,
        "previous_hash": "0" * 64, # Tidak ada blok sebelumnya
        "nonce": 777,               # Angka Kedaulatan
        "network": "STG-Chain Mainnet-Alpha"
    }

    # Generate Hash Keabadian (SHA-256)
    block_string = json.dumps(genesis_block, sort_keys=True).encode()
    genesis_hash = hashlib.sha256(block_string).hexdigest()
    
    genesis_block["genesis_hash"] = genesis_hash

    # Simpan ke Database Internal
    with open("../database/stg_genesis_block.json", "w") as f:
        json.dump(genesis_block, f, indent=4)

    print("-" * 60)
    print("🚀 STG-CHAIN GENESIS BLOCK GENERATED SUCCESSFULLY")
    print(f"🏛️ ARCHITECT : {architect}")
    print(f"🔐 HASH      : {genesis_hash}")
    print(f"📜 STATUS    : PERMANENTLY SEALED IN NUSANTARA-ROOT")
    print("-" * 60)

if __name__ == "__main__":
    generate_stg_genesis()
  
