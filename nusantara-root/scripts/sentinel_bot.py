import time
import json

# AKSARA-LOGIC CIPHER (Simplified for Welcome Protocol)
# Mapping characters to Ancient Nusantara-themed symbols
AKSARA_CIPHER = {
    'A': 'ꦄ', 'B': 'ꦧ', 'C': 'ꦼ', 'D': 'ꦢ', 'E': 'ꦌ', 
    'G': 'ꦒ', 'H': 'ꦲ', 'I': 'ꦆ', 'K': 'ꦏ', 'L': 'ꦭ',
    'N': 'ꦤ', 'O': 'ꦎ', 'R': 'ꦫ', 'S': 'ꦯ', 'T': 'ꦠ', 
    'U': 'ꦈ', 'V': 'ꦮ', 'Y': 'ꦪ', ' ': ' • '
}

def encrypt_aksara(text):
    return "".join([AKSARA_CIPHER.get(c.upper(), c) for c in text])

def welcome_guardian(wallet_address):
    raw_msg = "WELCOME GUARDIAN OF NUSANTARA ROOT"
    encrypted_msg = encrypt_aksara(raw_msg)
    
    print("-" * 60)
    print(f"📡 SENTINEL BOT: New Guardian Verified!")
    print(f"👤 WALLET: {wallet_address}")
    print("-" * 60)
    print(f"📜 ENCRYPTED GREETING (Aksara-Logic):")
    print(f"\n{encrypted_msg}\n")
    print(f"🗝️ DECODING KEY: 'The Giant is Breathing'")
    print("-" * 60)
    print("🚀 Status: Badge Airdrop Scheduled.")

if __name__ == "__main__":
    # Simulate monitoring the guardian_list.json
    try:
        with open("../../stg-web3/scripts/guardian_list.json", "r") as f:
            guardians = json.load(f)
            if guardians:
                last_guardian = guardians[-1]
                welcome_guardian(last_guardian)
            else:
                print("⏳ Sentinel is watching... No new Guardians yet.")
    except Exception as e:
        print(f"🚨 Bot Error: {e}")
      
