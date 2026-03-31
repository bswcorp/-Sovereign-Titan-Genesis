import os, time

def run():
    os.system('clear')
    GOLD, CYAN, WHITE, RESET = "\033[1;33m", "\033[1;36m", "\033[1;37m", "\033[0m"
    
    print(f"{GOLD}╔" + "═"*58 + "╗")
    print(f"║       🛰️  STG SOVEREIGN E-PASS CARD (CLEARANCE)          ║")
    print(f"║       HOLDER: CHIEF ARCHITECT - ANDI M. HARPIANTO        ║")
    print("╚" + "═"*58 + "╝" + RESET)
    
    print(f"{WHITE}LEGAL COMPLIANCE BASE:{RESET}")
    print("- USA SPACE ACT 2015 (SEC 51303)")
    print("- LUXEMBOURG SPACE RESOURCE LAW 2017")
    print("- UAE FEDERAL SPACE LAW 2020")
    print("- ITALY SPACE LAW NO. 89/2025")
    print("-" * 60)
    
    print(f"{CYAN}AUTHORIZED ACTIVITIES (VOL 700):{RESET}")
    print("✅ SPACE STATION & PORT OPERATIONS (METAKARTA)")
    print("✅ CELESTIAL RESOURCE EXTRACTION (MAKRONESIA MINING)")
    print("✅ INTERPLANETARY COMMERCIAL SERVICES (STG-TSC)")
    
    print(f"\n{GOLD}NOTICE: STG OPERATES AS A SOVEREIGN TRUSTEE.{RESET}")
    print("NON-CLAIM TERRITORY STATUS: [ACTIVE]")
    print("PRIVATE RESOURCE OWNERSHIP: [VERIFIED]")
    print("-" * 60)
    input("\n[ENTER] TO RECORD CLEARANCE...")

if __name__ == "__main__": run()
