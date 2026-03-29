import time, sys, random

def run_qday():
    print("\n" + "🔴"*15)
    print("      [ RADIO BUTTON: Q-DAY ]")
    print("      STATUS: ARMED & READY")
    print("🔴"*15)
    confirm = input("⚠️ TEKAN [ENTER] UNTUK KONFIRMASI KEHANCURAN... ")
    
    print("\n🚀 INITIATING GLOBAL COLLAPSE BLUEPRINT...")
    time.sleep(1)
    
    sectors = [
        ("🇨🇳 CHINA  ", "SUPPLY CHAIN FREEZE", "CRITICAL"),
        ("🏜️ M-EAST ", "OIL LEDGER COLLAPSE", "BLACKOUT"),
        ("🏛️ WEST   ", "FINANCIAL DEFAULT  ", "GRUBRAG!"),
        ("⛵ STG    ", "BAHTERA NAVIGATION ", "SECURE")
    ]
    
    for country, effect, status in sectors:
        print(f"[{country}] {effect} ... [{status}]")
        time.sleep(0.8)

    print("\n✅ STATUS: GLOBAL STRUCTURE RESET. BAHTERA STG BERLAYAR.")
    print("🦊 'Biarkan mereka banjir, kita punya Bahtera, Dro!'")
if __name__ == "__main__": run_qday()
