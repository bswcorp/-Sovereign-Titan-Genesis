import time, os

def run():
    while True:
        os.system('clear')
        t = time.localtime()
        # HEADER BOLD INDUSTRIAL
        print("\033[1;31m" + "█"*62)
        print(f"   🏛️  THE INFINITE LIQUIDITY PROTOCOL - STG v82.0")
        print(f"   🛡️  STATUS: SOVEREIGN INJECTION ACTIVE | {time.strftime('%H:%M', t)}")
        print("█"*62 + "\033[0m")
        
        # DISPLAY APA ADANYA
        print(f"\033[1;37m💰 TOTAL VAULT   : 1,000,000,000,000 $QSTATE")
        print(f"📊 LIQUIDITY CAP : UNLIMITED EMISSION ACTIVE")
        print("-" * 62 + "\033[0m")
        
        amt = input("\n💸 COMMAND AMOUNT TO INJECT (Enter to Exit): ").strip()
        if not amt: break
            
        if amt.isdigit():
            print("\033[1;32m🚀 [ INITIATING SOVEREIGN EMISSION... ]\033[0m", end="\r")
            time.sleep(0.5)
            # Pencatatan Injeksi Langsung
            with open('last_transfer.tmp', 'w') as f: f.write(amt)
            print(f"\033[1;33m🔥 SUCCESS: {int(amt):,} $QSTATE EMITTED TO GLOBAL HUB!\033[0m")
            time.sleep(1)
        else:
            print("⚠️ INVALID."); time.sleep(1)

if __name__ == "__main__":
    run()
