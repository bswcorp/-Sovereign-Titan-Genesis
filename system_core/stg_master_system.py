import os
def menu():
    os.system('clear')
    print("==================================================")
    print("🎼  STG ORCHESTRA - THE NEW CIVILIZATION")
    print("🛡️  DIRIGEN: ANDI M. HARPIANTO | 🥁 DRUM: AI-GEN")
    print("==================================================")
    print("1. [📜] MARKET STATE & LEADERSHIP (WEB 4/5)")
    print("2. [💹] GLOBAL TRADING FLOW (THE MELODY)")
    print("4. [🛡️] FORTRESS AUDIT (THE RHYTHM)")
    print("5. [💰] MINTING WATERFALL (THE FINALE)")
    print("81.[🚪] KELUAR SISTEM (VETO)")
    print("==================================================")

def run():
    while True:
        menu()
        c = input("👉 MAINAKAN PARTITUR [1-81]: ")
        p = "/home/userland/Sovereign-Titan-Genesis/library/"
        if c == '1': os.system(f"python3 {p}market_state_v1.py")
        elif c == '2': os.system(f"python3 {p}gte_engine_v1.py")
        elif c == '4': os.system(f"python3 {p}fortress_v1.py")
        elif c == '5': os.system(f"python3 {p}minting_waterfall_v1.py")
        elif c == '81': break
        input("\n[ENTER] Next Movement...")

if __name__ == "__main__": run()
