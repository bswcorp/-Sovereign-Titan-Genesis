import os, time, sys
def run():
    os.system('clear')
    print("==================================================")
    print("  STG CORPORATE COMMAND CENTER - INDUSTRIAL v86.0")
    print("  EXECUTIVE: CAPO ANDI M. HARPIANTO")
    print("==================================================")
    print("001. [CORE] MK-SERIES INDUSTRIAL ENGINE")
    print("110. [AUDT] CONSOLIDATED ASSET AUDIT")
    print("505. [MANL] TECHNICAL SPECIFICATION & MANUAL")
    print("555. [EMIT] MAKRONESIA LIQUIDITY EMISSION")
    print("808. [META] QUANTUM METAPORTASI INTERFACE")
    print("810. [EXIT] SECURE SYSTEM TERMINATION")
    print("==================================================")
    c = input("INPUT COMMAND CODE: ").strip()
    p = "/home/userland/Sovereign-Titan-Genesis/library/"
    if c == '001': os.system(f"python3 {p}stg_primary_engine.py")
    elif c == '110': os.system(f"python3 {p}system_audit_v2.py")
    elif c == '505': os.system(f"cat {p}manual_book/MANUAL_BOOK_v1.md")
    elif c == '555': os.system(f"python3 {p}stg_homeschooling_v1.py")
    elif c == '808': os.system(f"python3 {p}metaportasi_v1.py")
    elif c == '810': sys.exit()
    else: print("\nERROR: INVALID COMMAND."); time.sleep(1)
if __name__ == "__main__":
    while True:
        try: run()
        except KeyboardInterrupt: sys.exit()
