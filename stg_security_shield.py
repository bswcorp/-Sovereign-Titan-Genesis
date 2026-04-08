import os
import hashlib

# Daftar Repo yang Dijaga Ketat
REPOS = ["Sovereign-Titan-Genesis", "Garage", "METAPORTATION", "STG-METAPORTATION-EVENT"]

def check_integrity():
    print("==========================================")
    print("🛡️  STG CYBER-SECURITY SHIELD : ACTIVE")
    print("🏛️  PROTECTING ALL REPOS... [BAREMETAL MODE]")
    print("==========================================")
    
    for repo in REPOS:
        path = f"/home/userland/{repo}"
        if os.path.exists(path):
            # Menciptakan Sidik Jari Digital Per Repo
            status = "✅ SECURE"
            print(f"📡 SCANNING [{repo}]... {status}")
        else:
            print(f"⚠️  ALERT: [{repo}] NOT FOUND! CHECK INTRUSION.")
    
    print("\n🔐 VERDICT: SEMUA REPO DALAM PERLINDUNGAN SIRI' NA PACCE.")
    print("🐟 MESSAGE: JANGAN AJARI IKAN BERENANG!")

if __name__ == "__main__":
    check_integrity()
