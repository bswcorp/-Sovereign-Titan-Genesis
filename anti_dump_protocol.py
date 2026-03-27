import time
import os

def play_alert():
    for _ in range(3):
        os.system('echo -e "\a"')
        time.sleep(0.2)

def log_wolf():
    try:
        with open('/home/userland/Garage/wolf_count.txt', 'r+') as f:
            count = int(f.read().strip())
            f.seek(0)
            f.write(str(count + 1))
            f.truncate()
    except:
        pass

def anti_dump_gate():
    print("==========================================")
    print("🛡️  BENTENG ANTI-DUMP SOVEREIGN TITAN")
    print("💀 STATUS: SKULL MODE ACTIVE")
    print("==========================================")
    
    LIMIT = 1000000000 # 0.1% dari 1T
    
    try:
        amount = float(input("MASUKKAN JUMLAH JUAL ($QSTATE): "))
        if amount > LIMIT:
            play_alert()
            log_wolf() # CATAT SRIGALA NAKAL!
            print("\n🚨 DUMP DETECTED! [SKULL RED ALERT]")
            print(f"❌ TRANSAKSI {amount:,.0f} DIBLOKIR VETO!")
        else:
            print("\n✅ TRANSAKSI AMAN.")
    except:
        print("Input error, Capo!")

if __name__ == "__main__":
    anti_dump_gate()
