import numpy as np
from sklearn.ensemble import IsolationForest
import datetime

# 🚢 SIMULASI DATA TRANSAKSI PELABUHAN STG
# Fitur: [Jumlah_AKSA, Waktu_Jam, Status_H2K (1=Valid, 0=Invalid)]
# Kita latih Sentinel dengan pola "Normal" Sultan
normal_operations = np.array([
    [1000, 9, 1],   # Pagi, transaksi kecil, H2K OK
    [5000, 14, 1],  # Siang, transaksi sedang, H2K OK
    [10000, 20, 1], # Malam, transaksi besar, H2K OK
    [2000, 10, 1]   # Pagi, transaksi kecil, H2K OK
])

# Inisialisasi Otak Sentinel (Isolation Forest untuk deteksi anomali)
sentinel_brain = IsolationForest(contamination=0.1)
sentinel_brain.fit(normal_operations)

def check_transaction(amount, hour, h2k_status):
    current_tx = np.array([[amount, hour, h2k_status]])
    prediction = sentinel_brain.predict(current_tx)
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"--- [SENTINEL AUDIT] {timestamp} ---")
    if prediction == 1:
        print(f"✅ STATUS: NORMAL. Buruh Pelabuhan diizinkan bongkar muat {amount} AKSA.")
        return True
    else:
        print(f"🚨 STATUS: ANOMALI TERDETEKSI! Mandor menghentikan operasi!")
        print(f"⚠️ PERINGATAN: Transaksi {amount} AKSA pada jam {hour} mencurigakan!")
        return False

# 🧪 UJI COBA SINKRONISASI
if __name__ == "__main__":
    print("🚀 Melatih Sentinel AI dengan pola kedaulatan Sultan...")
    # Contoh transaksi normal
    check_transaction(1500, 11, 1)
    # Contoh serangan (Jumlah raksasa, jam 3 pagi, H2K gagal)
    check_transaction(9999999, 3, 0)
  
