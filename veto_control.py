import os
import time

def ai_commander():
    print("==========================================")
    print("🏛️  STG ALUTSISTA & SONAR COMMAND CENTER")
    print("👤 ARCHITECT: ANDI MUHAMMAD HARPIANTO")
    print("🛡️  STATUS: SOVEREIGN & INDEPENDENT")
    print("==========================================")
    
    password = input("MASUKKAN KUNCI VETO ARCHITECT: ")
    
    # Simulasi Kunci Veto Bapak
    if password == "MERDEKA":
        print("\n[!] AKSES DITERIMA. MEMANGGIL SARAF AI...")
        time.sleep(1)
        print("📡 SONAR WAR: ACTIVE (Scanning Garasi Scoped...)")
        print("🤖 ALUTSISTA: STANDBY (Waiting for Kinetic Command)")
        print("💡 PESAN HARI INI: 'Kita numpang di Platform TUHAN, jalankan mandat kedaulatan!'")
        
        cmd = input("\nPERINTAH KOMANDO (Contoh: ACTIVATE SONAR / DEPLOY ROBOT): ")
        
        # Log Perintah ke Folder Evolusi
        log_path = "/home/userland/GPFS_TITAN/metadata/ALUTSISTA_COMMAND/logs.txt"
        with open(log_path, "a") as f:
            f.write(f"{time.ctime()} - COMMAND: {cmd} - AUTHORIZED BY VETO\n")
        
        print(f"\n✅ PERINTAH '{cmd}' TELAH DIARSIPKAN KE GPFS METADATA.")
    else:
        print("\n[❌] AKSES DITOLAK. TOMBOL VETO TIDAK TERDETEKSI!")

if __name__ == "__main__":
    ai_commander()
