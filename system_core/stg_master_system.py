import os, time, sys

def draw_tsc_header():
    os.system('clear')
    G, B, W, R = "\033[1;32m", "\033[1;34m", "\033[1;37m", "\033[0m"
    print(f"{W}┌" + "─"*48 + "┐")
    print(f"│ {G}● ACTIVE {W}│ {B}  THE SOVEREIGN CORE - TSC v1.0       {W}│")
    print(f"├" + "─"*12 + "┬" + "─"*35 + "┤")
    print(f"│ {W}ARCHT: ANDI {W}│ {W}SYSTEM: INDUSTRIAL REVENUE HUB      {W}│")
    print(f"└" + "─"*12 + "┴" + "─"*35 + "┘")
    print(f"{B}INDUSTRIAL STATUS: [REVENUE_MODE_ACTIVE v103.1]{R}")
    print("-" * 50)

def run():
    while True:
        draw_tsc_header()
        print("001. [CORE] BFN ROUTING & TRANSACTION HUB")
        print("110. [AUDT] CONSOLIDATED ASSET AUDIT")
        print("111. [BILL] E-KUITANSI QUANTUM INVOICE GENERATOR FISCAL AUDIT")
        print("112. [PASS] BINTARO TRAFFIC VISUALIZATION")
        print("113. [LOYL] FUTURE LOYALTY & REWARD LOG")
        print("114. [CERT] E-CERTIFICATE: KHAMEL M. GUFRANY")
        print("115. [DBUG] ZERO-BUG INTEGRITY SENSOR")
        print("116. [REVN] NFC-NFT REVENUE MERCHANT")
        print("212. [RBOT] TACTICAL ROBOT & MINING MAP")
        print("222. [AUTO] SELF-MANAGED CUSTODIAN")
        print("505. [SPEC] 3-MINUTE PITCH & TECH MANUAL")
        print("555. [FLOW] LIQUIDITY TSUNAMI (1MQ)")
        print("808. [LINK] QUANTUM METAPORTASI BRIDGE")
        print("810. [EXIT] SECURE SYSTEM TERMINATION")
        print("-" * 50)
        
        choice = input("ENTER COMMAND CODE: ").strip()
        p = os.path.expanduser("~/Sovereign-Titan-Genesis/library/")
        
        map_files = {
            '001': 'stg_primary_engine.py',
            '110': 'system_audit_v2.py',
            '111': 'stg_invoice_v1.py',
            '112': 'stg_epass_card.py',
            '113': 'stg_loyalty_ledger.py',
            '114': 'stg_shareholder_cert.py',
            '115': 'stg_debug_sensor.py',
            '116': 'stg_nft_hub.py',
            '212': 'stg_robot_dash_v1.py',
            '222': 'stg_auto_custodian.py',
            '555': 'stg_homeschooling_v1.py',
            '808': 'metaportasi_v1.py'
        }

        if choice in map_files:
            os.system(f"python3 {p}{map_files[choice]}")
        elif choice == '505':
            os.system(f"cat {p}manual_book/MANUAL_BOOK_v1.md")
            input("\n[PRESS ENTER TO RETURN]")
        elif choice == '810':
            sys.exit()
        else:
            print("\nERR: INVALID_CODE"); time.sleep(1)

if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        sys.exit()
