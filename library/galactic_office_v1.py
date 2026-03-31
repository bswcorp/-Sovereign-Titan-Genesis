import os, time
def run():
    os.system('clear')
    GOLD, CYAN, BLUE, RESET = "\033[1;33m", "\033[1;36m", "\033[1;34m", "\033[0m"
    print(f"{GOLD}╔" + "═"*58 + "╗")
    print(f"║  🏛️  STG GLOBAL COMMAND - REGISTERED OFFICE ADDRESS      ║")
    print(f"║  🌌 LOCATION: BEYOND EARTH JURISDICTION                  ║")
    print("╚" + "═"*58 + "╝" + RESET)
    
    offices = [
        ("📍 HEAD OFFICE   ", "GALAXY SECTOR-700 / ORBITAL STATION"),
        ("⛏️  MINING SITE   ", "ASTEROID PSYCHE-16 / MAKRONESIA HUB"),
        ("📡 DATA CENTER   ", "LUNAR CRATER 808 / DEEP SPACE NODE")
    ]
    
    for loc, addr in offices:
        print(f"\n{BLUE}[OFFICIAL_ADDR] {loc}{RESET}")
        print(f"   Address : {CYAN}{addr}{RESET}")
        time.sleep(1)

    print("\n" + "="*60)
    print("✅ VERDICT: PHYSICAL ACCESS RESTRICTED TO SOVEREIGN ALLIES.")
    print("👑 'Mau cari kantor kita? Silakan sewa Roket dulu, Dro!'")
    print("="*60)
    input("\n[EXECUTE_RETURN]")
if __name__ == "__main__": run()
