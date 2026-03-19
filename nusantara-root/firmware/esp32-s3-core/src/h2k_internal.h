#ifndef H2K_INTERNAL_H
#define H2K_INTERNAL_H

#include <Arduino.h>
#include <mbedtls/sha256.h> // Library enkripsi bawaan ESP32

class H2K {
public:
    // Fungsi untuk menandatangani State berdasarkan detak jantung (IBI)
    static String Sign(int ibi_value) {
        String genesis_id = "SOVEREIGN-TITAN-GENESIS-V1";
        String raw_data = String(ibi_value) + genesis_id;
        
        // Proses Hashing SHA256 (Akar Kedaulatan)
        unsigned char hash[32];
        mbedtls_sha256_context ctx;
        mbedtls_sha256_init(&ctx);
        mbedtls_sha256_starts(&ctx, 0);
        mbedtls_sha256_update(&ctx, (uint8_t*)raw_data.c_str(), raw_data.length());
        mbedtls_sha256_finish(&ctx, hash);
        mbedtls_sha256_free(&ctx);

        // Konversi Hash ke bentuk Aksara (Simple Mapping)
        return ToAksara(hash);
    }

private:
    static String ToAksara(unsigned char* hash) {
        // Pemetaan ke 10 suku kata dasar Nusantara
        const char* syllables[] = {"ha", "na", "ca", "ra", "ka", "da", "ta", "sa", "wa", "la"};
        String aksara_sig = "";
        
        // Ambil 8 byte pertama untuk membuat Signature Aksara
        for (int i = 0; i < 8; i++) {
            int index = hash[i] % 10;
            aksara_sig += syllables[index];
        }
        return aksara_sig;
    }
};

#endif
