import time, os, random, sys
def run():
    os.system('clear')
    print("==================================================")
    print("      STG LIQUIDITY EMISSION: PROJECT MAKRONESIA")
    print("      SPECIFICATION: 1.000.000 QUADRILLION ($Q)")
    print("==================================================")
    try:
        while True:
            val = random.randint(1000, 9999)
            sys.stdout.write(f"\r[LOG] BLOCK_EMISSION: +{val:,}.00 $QSTATE | STATUS: VERIFIED")
            sys.stdout.flush()
            time.sleep(0.01)
            print("") 
    except KeyboardInterrupt:
        print("\n\n[AUDIT] EMISSION SUSPENDED. ASSETS SECURED.")
        input("\n[RETURN_TO_COMMAND_CENTER]")
if __name__ == "__main__": run()
