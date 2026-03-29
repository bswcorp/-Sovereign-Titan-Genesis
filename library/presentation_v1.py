import time, os

def run():
    os.system('clear')
    print("\033[1;33m" + "🏛️ " * 20)
    print("      STG GLOBAL MANIFESTO - JCC AUGUST")
    print("      CHIEF ARCHITECT: ANDI M. HARPIANTO")
    print("      STATUS: SOVEREIGN AUTHORITY ACTIVE")
    print("🏛️ " * 20 + "\033[0m")
    
    manifesto = [
        "💎 KAMI DI SINI BUKAN UNTUK MEMINTA. KAMI DI SINI UNTUK MEMBERIKAN.",
        "💎 KUADRILIUN BUKANLAH ANGKA, TETAPI REALITAS.",
        "💎 BAHTERA NUH 2028 TERBUKA UNTUK SEKUTU YANG TERVERIFIKASI.",
        "💎 KONDISI KUORUM ADALAH SATU-SATUNYA STRATEGI KELUAR YANG BERDAULAT."
    ]
    
    for point in manifesto:
        print(f"\n📢 {point}")
        time.sleep(1.5)

    print("\n" + "="*60)
    print("✅ STATUS: SOVEREIGN AUTHORITY ESTABLISHED.")
    print("⚓ 'SEKALI LAYAR TERKEMBANG, PANTANG SURUT!'")
    print("="*60)

if __name__ == "__main__":
    run()
