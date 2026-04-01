import os, time, random

def run():
    os.system('clear')
    GOLD, CYAN, WHITE, BLUE, GREEN, RESET = "\033[1;33m", "\033[1;36m", "\033[1;37m", "\033[1;34m", "\033[1;32m", "\033[0m"
    
    print(f"{GOLD}╔" + "═"*58 + "╗")
    print(f"║  🏛️  STG HYBRID MERCHANT: NFC + QRIS STANDARDIZED        ║")
    print(f"║  GATEWAY: SOVEREIGN REVENUE | STATUS: ONLINE             ║")
    print("╚" + "═"*58 + "╝" + RESET)
    
    print(f"{WHITE}SELECT PRODUCT FOR CHECKOUT:{RESET}")
    print(f"1. [NFT] GALAXY_MINING_PASS (Lvl 1) : 0.5 SOL / 100K IDR")
    print(f"2. [NFC] SOVEREIGN_KEY_HARDWARE    : 1.0 SOL / 250K IDR")
    print(f"3. [QST] SEED_LIQUIDITY_INJECTION  : 0.1 SOL / 25K IDR")
    print("-" * 60)
    
    choice = input(f"{CYAN}👉 SELECT PRODUCT (1-3): {RESET}").strip()
    
    if choice in ['1', '2', '3']:
        print(f"\n{WHITE}[GENERATING DYNAMIC PAYMENT INTERFACE...]{RESET}")
        time.sleep(1)
        
        # VISUALISASI QRIS (SIMULASI BOX)
        print(f"\n{WHITE}      [---- QRIS INTERFACE ----]")
        print(f"      [    █▀▀▀▀▀█ ▄▄ ▄ █▀▀▀▀▀█    ]")
        print(f"      [    █ ███ █ ▀▀ ▄ █ ███ █    ]")
        print(f"      [    █ ▀▀▀ █ ▄▀█▀ █ ▀▀▀ █    ]")
        print(f"      [    ▀▀▀▀▀▀▀ ▀ ▀ ▀▀▀▀▀▀▀    ]")
        print(f"      [    ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀    ]")
        print(f"      [------------------------]{RESET}")
        
        print(f"\n{GREEN}📡 NFC SENSOR: WAITING FOR DEVICE TOUCH...{RESET}")
        print(f"{GOLD}💰 STATUS: AWAITING SETTLEMENT VIA BFN HUB{RESET}")
        
        time.sleep(2)
        print(f"\n{CYAN}✅ TRANSACTION RECORDED IN INTERNAL LEDGER (110).")
        print(f"SYSTEM_CERTIFICATION: ASSET_TRANSFER_SUCCESSFUL{RESET}")
    else:
        print("\nERR: PRODUCT_NOT_FOUND")

    input("\n[EXECUTE_RETURN]")

if __name__ == "__main__": run()
