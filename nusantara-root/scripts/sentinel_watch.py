import time
import subprocess
import os

# Ambang batas deteksi (Threshold) untuk tahun 2026
MAX_FAILED_ATTEMPTS = 5
WATCH_INTERVAL = 2 # detik

def check_intruders():
    # Simulasi pemindaian log koneksi SRT dan HTTP
    print(">>> [SENTINEL WATCH] Memindai percobaan peretasan...")
    
    # Deteksi Anomali AI (Trend 2026): Mencari pola traffic yang tidak lazim
    # Dalam implementasi nyata, ini akan memantau akses ke port 1935 (SRT)
    # Jika terdeteksi IP mencurigakan, IP tersebut akan langsung di-banned.
    
    # Placeholder untuk perintah ban IP otomatis (Sovereign Firewall)
    # os.system("sudo iptables -A INPUT -s <IP_PENYERANG> -j DROP")

if __name__ == "__main__":
    print("------------------------------------------------------------")
    print(">>> [STG] SENTINEL WATCH: ACTIVE & MONITORING...")
    print("------------------------------------------------------------")
    try:
        while True:
            check_intruders()
            time.sleep(WATCH_INTERVAL)
    except KeyboardInterrupt:
        print(">>> [SENTINEL WATCH] Nonaktif. Tetap waspada.")
      
