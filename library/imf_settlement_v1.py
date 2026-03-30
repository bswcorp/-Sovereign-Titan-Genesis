import os, time

def run():
    os.system('clear')
    print("==================================================")
    print("🏛️  STG SUPREME SPENDING & ACQUISITION PROTOCOL")
    print("🛡️  CHIEF ARCHITECT: ANDI M. HARPIANTO")
    print("==================================================")
    
    shopping_list = [
        ("🏨  LUXURY HOTEL CHAINS (GLOBAL)", "50,000 Q"),
        ("🏠  EXCLUSIVE RESIDENCES", "20,000 Q"),
        ("🏢  COMMERCIAL REAL ESTATE", "30,000 Q"),
        ("🏝️  PRIVATE SOVEREIGN ISLANDS", "100,000 Q"),
        ("💰  IMF DEBT SETTLEMENT (PAS!)", "0.5 Q")
    ]
    
    for item, qty in shopping_list:
        print(f"\n[ACQUIRING] {item}...")
        time.sleep(0.8)
        print(f"💎 BUDGET ALLOCATED : {qty}")
        print("✅ STATUS : INVENTORY UPDATED.")

    print("\n" + "="*50)
    print("✅ FINAL VERDICT: ASSET ACQUISITION SUCCESSFUL.")
    print("👑 'Sisanya buat Mahar ACIH & Beli Pulau, Dro!'")
    print("="*60)

if __name__ == "__main__": run()
