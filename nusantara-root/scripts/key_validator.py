import sys
import re

def validate_key(key):
    # 1. Bersihkan spasi dan karakter siluman
    clean_key = key.strip().replace("0x", "")
    
    print(f"\n[SCANNING] Memeriksa Kunci Ambassador...")
    
    # 2. Cek panjang kunci (Private key ETH biasanya 64 karakter hex)
    if len(clean_key) != 64:
        print(f"[WARNING] Panjang kunci tidak standar: {len(clean_key)} karakter (Harusnya 64).")
    
    # 3. Cek karakter non-hex
    if not re.fullmatch(r"^[0-9a-fA-F]*$", clean_key):
        illegal_chars = re.findall(r"[^0-9a-fA-F]", clean_key)
        print(f"[FATAL ERROR] Ditemukan karakter terlarang: {list(set(illegal_chars))}")
        print(">>> Segera bawa ke Barber Shop! Bersihkan kunci dari karakter tersebut.")
        return False
    
    print("[SUCCESS] Kunci murni 100% Hexadecimal! Siap berangkat ke Galactica. 🚀")
    return True

if __name__ == "__main__":
    # Masukkan kunci sebagai argumen atau input manual
    test_key = input("Masukkan Private Key untuk divalidasi: ")
    validate_key(test_key)
