// libraries
// temp/humidity
#include "DHT.h"
#define DHTTYPE DHT22

// pins
#define CS_PIN PIN_PB2
#define MOSI_PIN PIN_PB3
#define MISO_PIN PIN_PB4
#define SCK_PIN PIN_PB5
#define SPEED_PIN PIN_PC1
#define DIR_PIN PIN_PC2
#define SET_PIN PIN_PC3
// PC4 and PC5 are SDA and SCL respectively, they don't need to be defined
// PC6 is RST, this is used by the ISP and doesn't need to be defined
#define GPS_OUT_PIN PIN_PD0
#define GPS_IN_PIN PIN_PD1
#define TEMP_PIN PIN_PD2
#define FREQ_BUT_PIN PIN_PD4
#define RED_PIN PIN_PD5
#define GREEN_PIN PIN_PD6
#define BLUE_PIN PIN_PD7

// library setup
DHT dht(TEMP_PIN, DHTTYPE);

void setup() {
  // PB
  pinMode(CS_PIN, OUTPUT);
  pinMode(MOSI_PIN, OUTPUT);
  pinMode(MISO_PIN, INPUT);
  pinMode(SCK_PIN, OUTPUT);

  // PC
  pinMode(SPEED_PIN, INPUT);
  pinMode(DIR_PIN, INPUT);
  pinMode(SET_PIN, OUTPUT); // should switch between high-Z and low! do not output 5V (high) to the sensor
                            // this can be accomplished by switching the pin to an input when in sleep mode (I think)
  // PD
  // note: GPS pins don't need to be defined, there is a library that handles GPS I/O
  // note: temp pin doesn't need to be defined, there is a library that handles temp/humidity I/O
  pinMode(FREQ_BUT_PIN, INPUT);
  pinMode(RED_PIN, OUTPUT);
  pinMode(GREEN_PIN, OUTPUT);
  pinMode(BLUE_PIN, OUTPUT);
  
  // enable internal pullup
  digitalWrite(FREQ_BUT_PIN, HIGH);

  // initialize sensors working with libraries
  dht.begin();
}

void loop() {
  // Read humidity
  float h = dht.readHumidity();
  // Read temperature as Fahrenheit (isFahrenheit = true)
  float f = dht.readTemperature(true);

  if (isnan(h) || isnan(t) || isnan(f)) {
    Serial.println(F("Failed to read from DHT sensor!"));
  }
  
//  // read potentiometer and rescale to 0-1s delay
//  int delay_time = 1000 * int32_t(analogRead(POT_PIN)) / 1024;
//
//  // blink while button depressed
//  if (digitalRead(BUT_PIN) == LOW) {
//    digitalWrite(LED_PIN, HIGH);
//    delay(delay_time);
//    digitalWrite(LED_PIN, LOW);
//    delay(delay_time);
//  } else {
//    digitalWrite(LED_PIN, LOW);
//  }

}
