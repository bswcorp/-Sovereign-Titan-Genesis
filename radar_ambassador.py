import urllib.request
import json
import time
import os

PROBE_ID = "19546"
API_URL = f"https://atlas.ripe.net{PROBE_ID}/"

def run_official_audit():
    print(f"\n🏛️  RIPE ATLAS AMBASSADOR MONITORING")
    print(f"🆔 PROBE ID: {PROBE_ID} | ARCHITECT: ANDI M. HARPIANTO")
    print("="*50)
    
    try:
        # Menarik data REAL dari API RIPE NCC
        response = urllib.request.urlopen(API_URL, timeout=15)
        data = json.loads(response.read().decode())
        
        status = data.get("status", {}).get("name", "UNKNOWN")
        country = data.get("country_code", "ID")
        address_v4 = data.get("address_v4", "HIDDEN")
        
        print(f"📍 LOCATION   : {country} (JAKARTA-KUNINGAN)")
        if status == "Connected":
            print(f"✅ STATUS     : {status} (BERDAULAT)")
        else:
            print(f"⚠️ STATUS     : {status} (CHECK CONNECTION)")
            os.system('echo -e "\a"')
            
        print(f"📡 IPv4 ADDR  : {address_v4}")
        print(f"📜 DESCRIPTION: {data.get('description', 'Ambassador Probe')}")
        
    except Exception as e:
        print(f"❌ ERROR: Gagal Menghubungi RIPE NCC API.")
        print(f"⚠️ DETEKSI: Potensi Interferensi atau Jalur Terblokir.")
        os.system('echo -e "\a"')

    print("="*50)
    print("✅ PENGUKURAN RESMI SELESAI. JAGA INTERNET BUMI!")

if __name__ == "__main__":
    run_official_audit()
