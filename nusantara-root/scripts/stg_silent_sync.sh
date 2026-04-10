#!/bin/bash

# --- STG SILENT SYNC: PENYELAMAT ALIRAN KEDAULATAN ---
REPO_DIR="$HOME/Sovereign-Titan-Genesis"
LOG_FILE="$REPO_DIR/nusantara-root/scripts/nohup.out" # Mengambil hasil dari nohup mining

while true
do
    cd $REPO_DIR
    
    # 1. Menarik data terbaru tanpa menghentikan arus
    git add .
    
    # 2. Memberi label timestamp pada setiap 'tetesan' data
    TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
    git commit -m "STG Sync: Arus Kedaulatan Berlanjut - $TIMESTAMP"
    
    # 3. Mendorong data ke Sekoci GitHub (Silently)
    git push origin main
    
    echo "[🛡️] Aset Berhasil Di-backup ke GitHub pada $TIMESTAMP"
    
    # Tunggu 30 menit sebelum sinkronisasi berikutnya (agar hemat baterai)
    sleep 1800
done
