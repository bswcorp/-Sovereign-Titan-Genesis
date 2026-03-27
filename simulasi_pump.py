import os

def simulasi_pump():
    print("==========================================")
    print("🚀 TITAN PUMP SIMULATOR - STG GOV")
    print("🛡️  STRATEGY: SCARCITY & LIQUIDITY")
    print("==========================================")
    
    # Pool Awal (Contoh: Peluru Capo)
    eth_pool = float(input("PELURU ETH DI POOL (Misal 10): "))
    qstate_pool = float(input("SUPLAI $QSTATE DI POOL (Misal 100000000): "))
    
    # Harga Awal
    price_awal = eth_pool / qstate_pool
    k = eth_pool * qstate_pool # Constant Product
    
    print(f"\n💎 HARGA AWAL: {price_awal:.18f} ETH")
    print("-" * 40)
    
    # Simulasi Pembelian (Pump)
    buy_amount = float(input("ADA PEMBELIAN SEBESAR (ETH): "))
    
    # Rumus DEX: eth_baru = eth_lama + buy_amount
    # qstate_baru = k / eth_baru
    eth_baru = eth_pool + buy_amount
    qstate_baru = k / eth_baru
    
    # Berapa koin yang didapat pembeli
    tokens_bought = qstate_pool - qstate_baru
    price_baru = eth_baru / qstate_baru
    kenaikan = ((price_baru - price_awal) / price_awal) * 100
    
    print("\n" + "="*40)
    print(f"🚀 STATUS: PUMP DETECTED!")
    print(f"📦 KOIN TERJUAL : {tokens_bought:,.0f} $QSTATE")
    print(f"📈 HARGA BARU   : {price_baru:.18f} ETH")
    print(f"🔥 KENAIKAN     : {kenaikan:.2f}%")
    print("="*40)
    
    if kenaikan > 50:
        print("⚠️  WARNING: HARGA MELEDAK! RAKSASA BANGKIT!")
    else:
        print("✅ STATUS: PERTUMBUHAN STABIL.")

if __name__ == "__main__":
    simulasi_pump()
