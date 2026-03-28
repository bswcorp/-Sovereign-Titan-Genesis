import os
import sys

def menu():
    os.system('clear')
    print("==================================================")
    print("🏛️  STG SOVEREIGN MASTER SYSTEM v2.5")
    print("🛡️  ARCHITECT: ANDI M. HARPIANTO")
    print("==================================================")
    print("1. [🔐] MASUK DAPUR PACU (SIRI GATE)")
    print("2. [🚀] LUNCURKAN WARP SPEED (SWISS HUB)")
    print("3. [📡] AUDIT KEDAULATAN (RIPE ATLAS)")
    print("4. [🛡️] SCAN LOG SRIGALA (PROFILING)")
    print("5. [🫀] REAL-WORK KERNEL MONITOR")
    print("6. [🚪] KELUAR SISTEM")
    print("==================================================")

def run():
    while True:
        menu()
        choice = input("👉 PILIH OPERASI [1-6]: ")
        if choice == '1': os.system('python3 ../library/siri_gate_v2.py')
        elif choice == '2': os.system('python3 ../library/warp_drive_v2.py')
        elif choice == '3': os.system('python3 ../library/log_kedaulatan_v1.py')
        elif choice == '4': os.system('python3 ../library/wolf_scanner_v1.py')
        elif choice == '5': os.system('python3 ../library/wolf_realwork_v1.py')
        elif choice == '6': 
            print("\n👋 Sistem Standby. Merdeka!")
            break
        input("\n[ENTER] Kembali ke System...")

if __name__ == "__main__":
    run()
