import time
import random
from mm_admin_titan import log_intrusion

def monitor_galerai():
    print("🛰️  RADAR SONAR WAR: ONLINE")
    try:
        while True:
            detection = random.random()
            if detection > 0.8:
                print("⚠️  DETEKSI PENYUSUP! MENGHUBUNGI ADMIN GPFS...")
                log_intrusion("SECTOR_02_ALUTSISTA", "CRITICAL")
            elif detection < 0.1:
                log_intrusion("SECTOR_03_SONAR", "INFO")
            time.sleep(5)
    except KeyboardInterrupt:
        print("\n[!] SHUTTING DOWN GPFS CLUSTER ADMIN.")

if __name__ == "__main__":
    monitor_galerai()
