import os

def hitung_valuasi():
    print("==========================================")
    print("🏛️  KALKULATOR VALUASI BAYI RAKSASA STG")
    print("🛡️  ANTI-MICIN STRATEGY | SOVEREIGN TITAN")
    print("==========================================")
    
    # Input Amunisi ETH (Peluru)
    eth_pool = float(input("MASUKKAN JUMLAH PELURU (ETH): "))
    
    # Input Amunisi $QSTATE (Suplai yang akan dilepas ke bursa)
    # Misal dari 1T, kita lepas 30% (300 Miliar) untuk sirkus awal
    qstate_supply = float(input("MASUKKAN JUMLAH $QSTATE DI BURSA: "))
    
    # Hitung Harga Awal per Koin
    price_eth = eth_pool / qstate_supply
    
    # Estimasi dalam Rupiah (Asumsi ETH = 60 Juta IDR)
    eth_to_idr = 60000000
    price_idr = price_eth * eth_to_idr
    
    market_cap_idr = (1000000000000 * price_idr)
    
    print("\n" + "="*40)
    print(f"💎 HARGA AWAL: {price_eth:.18f} ETH")
    print(f"🇮🇩 ESTIMASI  : Rp {price_idr:.8f} / $QSTATE")
    print(f"🏛️  MARKET CAP: Rp {market_cap_idr:,.0f}")
    print("="*40)
    
    if price_idr < 0.01:
        print("⚠️ STATUS: TERLALU MURAH (RAWAN MICIN!)")
        print(">>> SARAN: TAMBAH ETH ATAU KURANGI SUPLAI AWAL.")
    else:
        print("✅ STATUS: BERWIBAWA (RAKSASA TERDETEKSI)")

if __name__ == "__main__":
    hitung_valuasi()
