#include <WiFi.h>
#include "h2k_internal.h"

void setup() {
  // Inisialisasi sensor detak jantung pada pin ADC
  // Aktifkan ESP-NOW untuk komunikasi Mesh tanpa Router
}

void loop() {
  int pulse = analogRead(34); 
  String aksaraKey = H2K_Sign(pulse);
  sendToMesh(aksaraKey);
}
