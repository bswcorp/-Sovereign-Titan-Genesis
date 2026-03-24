#include <Wire.h>
#include "MAX30105.h"
#include "heartRate.h"

MAX30105 particleSensor;
void setup() {
  Serial.begin(115200);
  if (!particleSensor.begin(Wire, I2C_SPEED_FAST)) while (1);
  particleSensor.setup();
}
void loop() {
  long irValue = particleSensor.getIR();
  if (checkForBeat(irValue) == true) {
    Serial.print("QS_MINTED_KEY:STG-");
    Serial.println(millis());
  }
}

