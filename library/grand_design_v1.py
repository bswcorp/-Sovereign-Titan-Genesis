import time, os

def run():
    os.system('clear')
    print("\033[1;36m" + "🌳"*20)
    print("      🏛️  STG GRAND DESIGN: THE SOVEREIGN TREE")
    print("      ARCHITECT: ANDI M. HARPIANTO")
    print("🌳"*20 + "\033[0m")
    
    sectors = [
        ("🛰️  SPACE TECH", "ROBOTICS & AEROSPACE EDUCATION (20 YRS PLAN)"),
        ("🏢  DATA CENTER", "HOTEL & DATA CENTER INFRASTRUCTURE"),
        ("🍃  GREEN IKN", "ROADS, BRIDGES & RENEWABLE ENERGY"),
        ("📡  3C CENTER", "DATA, MEDIA & CRISIS COMMAND")
    ]
    
    for sector, desc in sectors:
        print(f"\n[INITIATING] {sector}...")
        time.sleep(1)
        print(f"✅ OBJECTIVE: {desc}")

    print("\n" + "="*50)
    print("✅ STATUS: BUDGET LOCKED & CURRICULUM SYNCED.")
    print("👑 'Duitnya buat bangun Bangsa, bukan buat Srigala, Dro!'")
    print("="*50)

if __name__ == "__main__": run()
