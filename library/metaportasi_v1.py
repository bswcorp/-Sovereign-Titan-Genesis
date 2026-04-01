import os, time

def run():
    os.system('clear')
    RED, GOLD, CYAN, RESET = "\033[1;31m", "\033[1;33m", "\033[1;36m", "\033[0m"
    print(f"{RED}╔" + "═"*58 + "╗")
    print(f"║   ⚠️  STG LONG-TERM MISSION CONTROL (2026-2046)          ║")
    print(f"║   CLASSIFICATION: ARCHITECT EYES ONLY                    ║")
    print("╚" + "═"*58 + "╝" + RESET)
    
    phases = [
        ("📅 PHASE 1 (1-5Y) ", "DEBT CLEARANCE & BFN ESTABLISHMENT"),
        ("☄️  PHASE 2 (6-15Y)", "GALACTIC MINING & VOL 700 EXPANSION"),
        ("🏛️  PHASE 3 (20Y+) ", "FULL SOVEREIGNTY HANDOVER TO HEIR"),
        ("🛡️  PQC STATUS    ", "ACTIVE - LATTICE BASED (FIPS 203)")
    ]
    
    for p, d in phases:
        print(f"\n{GOLD}[MISSION] {p}{RESET}")
        print(f"   Objective : {CYAN}{d}{RESET}")
        time.sleep(1)

    print("\n" + "="*60)
    print("✅ RAHASIA TERKUNCI: 'KITA BUKAN MENUNGGU, KITA MENDAHULUI.'")
    print("="*60)
    input("\n[EXECUTE_STAY_SILENT]")

if __name__ == "__main__": run()
