# COUNCIL TRIAL MISSION GENERATOR v1.0
# Only accessible to SSA Rank 1-10

import hashlib
import time

MISSION_ID = "OP-ORCHID-FINAL"
MISSION_TEXT = (
    "OBJECTIVE: Audit the 'DecoyBridge.sol'. "
    "There is a hidden re-entrancy path hidden within the Aksara-Logic validator. "
    "The Five who fix it first, while maintaining H2K integrity, shall ascend."
)

def generate_trial_packet(guardian_wallet):
    # Unique salt for each Top 10 member
    salt = str(time.time())
    mission_hash = hashlib.sha256((guardian_wallet + MISSION_ID + salt).encode()).hexdigest()
    
    print("\n" + "⚔️ "*15)
    print(f"🏛️ THE COUNCIL TRIAL: {MISSION_ID}")
    print(f"👤 GUARDIAN: {guardian_wallet}")
    print("⚔️ "*15)
    print(f"\n📜 INSTRUCTIONS (ENCRYPTED):")
    print(f"{MISSION_TEXT}")
    print(f"\n🔐 TRIAL_SESSION_TOKEN: {mission_hash}")
    print("\n" + "⚔️ "*15)
    print("⚠️ WARNING: Failure to maintain secrecy results in immediate Rank Demotion.")
    print("⚔️ "*15 + "\n")

if __name__ == "__main__":
    # Simulation: Rank 3 Guardian receives their trial
    generate_trial_packet("0xSovereign_Guardian_3")
  
