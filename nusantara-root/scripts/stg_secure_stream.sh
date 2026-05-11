#!/bin/bash
# STG-Chain: Secure Stream Seal (AES-256 Encryption)
# Objective: Encrypted Handshake with the Council of Five

STREAM_URL="srt://quorumstate.international:1935"
STREAM_KEY="DEWAN_LIMA_SOVEREIGN_KEY_2026"
ENCRYPTION_PASSPHRASE=$(echo -n "SIRI_NA_PACCE_STG" | sha256sum | cut -d' ' -f1)

echo "------------------------------------------------------------"
echo ">>> [STG] INITIALIZING ENCRYPTED STREAM FOR COUNCIL..."
echo "------------------------------------------------------------"

# Perintah untuk menjalankan FFmpeg dengan enkripsi SRT
# Hanya Dewan Lima yang memiliki passphrase ini yang bisa mendekripsi stream.
ffmpeg -re -i inauguration_video.mp4 \
    -c:v libx264 -preset veryfast -b:v 3000k \
    -c:a aac -b:a 128k \
    -f mpegts "$STREAM_URL?mode=caller&passphrase=$ENCRYPTION_PASSPHRASE&pbkeylen=32"

echo ">>> [STATUS] SECURE STREAM ACTIVE. ENCRYPTION: AES-256"
