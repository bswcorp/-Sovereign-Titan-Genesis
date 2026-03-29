import time, random, sys

def run_waterfall():
    print("\n" + "💰"*15)
    print("🏛️  STG MINTING MONITOR - GENESIS FLOW")
    print("💰"*15)
    print("CTRL+C UNTUK BERHENTI\n")
    
    try:
        while True:
            coins = ["$QSTATE", "$QUBIC", "$QSTATE-LP"]
            coin = random.choice(coins)
            amount = random.randint(1000000, 9999999)
            sqid = "0x" + "".join([random.choice("0123456789ABCDEF") for _ in range(8)])
            
            # Gaya Ping IP (Running Text)
            sys.stdout.write(f"\r🚀 MINTING SUCCESS: {amount:,.0f} {coin} | TO: {sqid} | STATUS: CONFIRMED")
            sys.stdout.flush()
            time.sleep(0.1)
            print("") # New line like ping
    except KeyboardInterrupt:
        print("\n\n✅ MONITORING PAUSED. ASSETS SECURED.")

if __name__ == "__main__": run_waterfall()
