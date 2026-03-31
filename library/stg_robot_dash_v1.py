import os, time, random

def run():
    os.system('clear')
    GOLD, CYAN, WHITE, BLUE, RESET = "\033[1;33m", "\033[1;36m", "\033[1;37m", "\033[1;34m", "\033[0m"
    
    print(f"{BLUE}╔" + "═"*58 + "╗")
    print(f"║   🤖 TACTICAL ROBOT MONITOR & GALACTIC MINING MAP        ║")
    print(f"║   LOCATION: ASTEROID 16-PSYCHE | COORDINATES: 2.92 AU    ║")
    print("╚" + "═"*58 + "╝" + RESET)
    
    print(f"{WHITE}SITE COORDINATES (RA/DEC): 05h 35m 17s / -05° 23′ 28″{RESET}")
    print(f"{WHITE}MINING SECTOR      : DELTA-7 (HIGH GOLD CONCENTRATION){RESET}")
    print("-" * 60)
    
    units = [
        ("STG-SWARM-01", "EXTRACTION", "92%", "WORKING"),
        ("STG-SWARM-02", "PROCESSING", "68%", "WORKING"),
        ("STG-PHINISI-X", "UPLINK", "100%", "ORBITAL")
    ]
    
    print(f"{WHITE}UNIT_ID        | TASK        | LOAD | STATUS{RESET}")
    for uid, task, load, stat in units:
        print(f"{CYAN}{uid:<14} {WHITE}| {task:<11} | {load:<4} | {GOLD}{stat}{RESET}")
    
    print("-" * 60)
    print(f"💎 CURRENT ASSET ESTIMATION: {GOLD}1,000,000 QUADRILLION $Q{RESET}")
    print(f"🛰️  UPLINK STATUS: {BLUE}QUANTUM BRIDGE ACTIVE (STABLE){RESET}")
    print("-" * 60)
    input("\n[ENTER] TO RETURN TO TACTICAL HUB...")

if __name__ == "__main__": run()
