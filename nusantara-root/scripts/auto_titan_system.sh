#!/bin/bash

# 1. MEMBERSI IZIN (PERMITS)
echo "--------------------------------------------------"
    echo "      SOVEREIGN TITAN AUTO-ENGINE v1.0            "
    echo "      FOUNDER: ANDI MUHAMMAD HARPIANTO            "
    echo "--------------------------------------------------"

# 2. MEMULAI JANTUNG LOKAL (GANACHE) DI LATAR BELAKANG
echo ">>> Menghidupkan Jantung Ganache (Shanghai Mode)..."
fuser -k 8545/tcp > /dev/null 2>&1 # Bersihkan port jika masih nyala
ganache --hardfork shanghai --port 8545 > /dev/null 2>&1 &
sleep 5 # Tunggu jantung berdetak

# 3. DEPLOY OTOMATIS KOIN $QSTATE
echo ">>> Mencetak 1 Triliun $QSTATE ke Blockchain..."
DEPLOY_LOG=$(python3 ~/Sovereign-Titan-Genesis/nusantara-root/scripts/deploy_sandbox.py)
NEW_ADDRESS=$(echo "$DEPLOY_LOG" | grep -oE "0x[a-fA-F0-9]{40}")

if [ -z "$NEW_ADDRESS" ]; then
    echo "![ERROR] Gagal mendapatkan Alamat Kontrak. Cek skrip deploy!"
    exit 1
fi

echo ">>> SUKSES! Alamat Kontrak Baru: $NEW_ADDRESS"

# 4. UPDATE SKRIP CEK SALDO SECARA OTOMATIS
sed -i "s/CONTRACT_ADDRESS = \".*\"/CONTRACT_ADDRESS = \"$NEW_ADDRESS\"/" ~/Sovereign-Titan-Genesis/nusantara-root/scripts/cek_saldo_aksa.py

# 5. TAMPILKAN HASIL AKHIR (SIRKUS DIMULAI)
echo ">>> Membuka Brankas Aksara..."
python3 ~/Sovereign-Titan-Genesis/nusantara-root/scripts/cek_saldo_aksa.py

echo "--------------------------------------------------"
echo ">>> SIRKUS BESAR DIMULAI! TUNJUKKAN PADA DUNIA!   "
echo "--------------------------------------------------"
