#!/bin/bash
# SCRIPT BANK UMUM 005 - VERSI EFISIEN PANGLIMA

while true; do
    clear
    echo "=========================================="
    echo "       SISTEM BANK UMUM [OFFICIAL]        "
    echo "=========================================="
    read -p "MASUKKAN KODE AKSES: " kode
    
    if [ "$kode" == "005" ]; then
        echo -e "\n[!] AKSES DITERIMA: Unit Bank Aktif"
        echo "------------------------------------------"
        echo "[A] MENERIMA  [B] MEMBAYAR"
        echo "[C] TRANSFER  [D] CEK SALDO"
        read -p "Pilih Aksi (A/B/C/D): " aksi

        echo -e "\n[1] KRIPTO  [2] FOREX  [3] E-FOREX"
        read -p "Pilih Jalur Mata Uang: " kategori

        # Logika Otomatis Berdasarkan Pilihan
        case $kategori in
            1) daftar="[1] ETH [2] BTC [3] SOLANI [4] USDT [5] COINBASE" ;;
            2) daftar="[1] YEN [2] US$ [3] POUND [4] RP [5] CENT" ;;
            3) daftar="[1] E-YUAN [2] E-RP [3] E-EURO [4] E-SIN" ;;
        esac
        
        echo -e "\nDAFTAR ITEM: $daftar"
        read -p "Pilih Unit Tujuan: " unit

        echo -e "\n[1] HOT WALLET  [2] COLD WALLET  [3] E-WALLET"
        read -p "Pilih Suhu Dompet: " dompet

        case $dompet in
            1) sub="[1] METAMASK [2] TRUST [3] CAPO [4] BINANCE" ;;
            2) sub="[1] ES WALLET [2] ES DAWET [3] DINGIN WALLET" ;;
            3) sub="[1] DANA [2] FLIP [3] WISE [4] FISE [5] SAKUKU" ;;
        esac

        echo -e "\nTUJUAN AKHIR: $sub"
        read -p "Pilih Provider: " prov
        
        echo "------------------------------------------"
        read -p "KETIK JUMLAH NOMINAL: " jumlah
        echo -e "\n[✔] PROSES BERHASIL!"
        echo "[INFO] $jumlah telah masuk ke sistem."
        echo "------------------------------------------"
        read -p "Tekan [ENTER] Untuk Kembali ke Dashboard..."
    else
        echo "[!] KODE SALAH. AKSES DITOLAK."
        sleep 1
    fi
done
