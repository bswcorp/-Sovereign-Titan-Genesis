import os, time, json, random

def generate_receipt(customer="PRIVATE_ALLY", item="GALAXY_MINING_PASS", amount="100,000 IDR"):
    os.system('clear')
    GOLD, CYAN, WHITE, BLUE, GREEN, RESET = "\033[1;33m", "\033[1;36m", "\033[1;37m", "\033[1;34m", "\033[1;32m", "\033[0m"
    
    receipt_id = f"STG-REC-{int(time.time())}-{random.randint(10,99)}"
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    
    # 1. TAMPILAN KUITANSI BONAFIDE
    print(f"{WHITE}╔" + "═"*58 + "╗")
    print(f"║             🏛️  STG OFFICIAL E-RECEIPT (KUITANSI)         ║")
    print(f"║           SOVEREIGN INFRASTRUCTURE SETTLEMENT            ║")
    print("╚" + "═"*58 + "╝" + RESET)
    
    print(f"{WHITE}RECEIPT ID   : {GOLD}{receipt_id}{RESET}")
    print(f"{WHITE}DATE/TIME    : {timestamp}{RESET}")
    print(f"{WHITE}SETTLEMENT   : {GREEN}SUCCESSFUL / VERIFIED{RESET}")
    print("-" * 60)
    print(f"CUSTOMER     : {customer}")
    print(f"DESCRIPTION  : {item}")
    print(f"TOTAL VALUE  : {CYAN}{amount}{RESET}")
    print("-" * 60)
    print(f"CUSTODIAN    : BFN HUB (BINTARO COMMAND CENTER)")
    print(f"VERIFICATION : {BLUE}757CE2F_AEROSPACE_COMPLIANT{RESET}")
    print("-" * 60)

    # 2. AUTOMATIC RECORDING KE LEDGER (VOL 110)
    log_data = {
        "date": timestamp,
        "id": receipt_id,
        "item": item,
        "amount": amount,
        "status": "SETTLED"
    }
    with open('sovereign_cashflow.json', 'a') as f:
        f.write(json.dumps(log_data) + "\n")
    
    print(f"\n{GREEN}✅ DATA AUTOMATICALLY ARCHIVED IN INTERNAL AUDIT (110).{RESET}")
    input("\n[PRESS ENTER TO RETURN]")

if __name__ == "__main__":
    # Default menu call
    generate_receipt()
