// LIBRARIES
// temp/humidity
#include "DHT.h"
#define DHTTYPE DHT22

// SD
#include "SPI.h"
#include "SD.h"
File myFile;

// GPS
#include "TinyGPSPlus.h"
#include "SoftwareSerial.h"
int GPSBaud = 9600;
TinyGPSPlus gps;

// PM
#include <Seeed_HM330X.h>
HM330X pmSensor;
u8 pmBuf[30];

// PINS
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

// LIBRARY SETUP
SoftwareSerial gpsSerial(GPS_OUT_PIN, GPS_IN_PIN);
DHT dht(TEMP_PIN, DHTTYPE);

// MISC
enum frequency { five_min, one_hr, three_hr };

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
  gpsSerial.begin(GPSBaud);
  pmSensor.init();
}

void loop() {
  // wind info is wack: https://www.youtube.com/watch?v=KHrTqdmYoAk

  // --------------------------------------------------- //
  // TEMP/HUMIDITY //
  // --------------------------------------------------- //
  
  // Read humidity
  float h = dht.readHumidity();
  // Read temperature as Fahrenheit (isFahrenheit = true)
  float f = dht.readTemperature(true);

  if (isnan(h) || isnan(f)) {
    Serial.println(F("Failed to read from DHT sensor!"));
  }

  // --------------------------------------------------- //
  // PM //
  // --------------------------------------------------- //
  
  if(!pmSensor.read_sensor_value(pmBuf,29)){
    u16 value=0;
    if(NULL==pmBuf)
        Serial.println(F("Failed to read from PM sensor!"));;
    for(int i=5;i<8;i++)
    {
         value = (u16)pmBuf[i*2]<<8|pmBuf[i*2+1];
         // value holds PM1.0, then PM2.5, then PM10
 
    }
  }


  // --------------------------------------------------- //
  // GPS //
  // --------------------------------------------------- //

  
  if (gpsSerial.available() > 0 && gps.encode(gpsSerial.read())){
    if (gps.location.isValid())
    {
      Serial.print("Latitude: ");
      Serial.println(gps.location.lat(), 6);
      Serial.print("Longitude: ");
      Serial.println(gps.location.lng(), 6);
      Serial.print("Altitude: ");
      Serial.println(gps.altitude.meters());
    }
    else
    {
      Serial.println("Location: Not Available");
    }
    
    Serial.print("Date: ");
    if (gps.date.isValid())
    {
      Serial.print(gps.date.month());
      Serial.print("/");
      Serial.print(gps.date.day());
      Serial.print("/");
      Serial.println(gps.date.year());
    }
    else
    {
      Serial.println("Not Available");
    }
  
    Serial.print("Time: ");
    if (gps.time.isValid())
    {
      if (gps.time.hour() < 10) Serial.print(F("0"));
      Serial.print(gps.time.hour());
      Serial.print(":");
      if (gps.time.minute() < 10) Serial.print(F("0"));
      Serial.print(gps.time.minute());
      Serial.print(":");
      if (gps.time.second() < 10) Serial.print(F("0"));
      Serial.print(gps.time.second());
      Serial.print(".");
      if (gps.time.centisecond() < 10) Serial.print(F("0"));
      Serial.println(gps.time.centisecond());
    }
    else
    {
      Serial.println("Not Available");
    }
  }

  // --------------------------------------------------- //
  // WIND DIRECTION //
  // --------------------------------------------------- //

  int windDirVal = analogRead(DIR_PIN);

  if (windDirVal <= 800 && windDirVal >= 770){
    Serial.println("N");
  } else if (windDirVal >= 450 && windDirVal <= 480){
    Serial.println("NE");
  } else if (windDirVal >= 87 && windDirVal <= 110){
    Serial.println("E");
  } else if (windDirVal >= 170 && windDirVal <= 200){
    Serial.println("SE");
  } else if (windDirVal >= 270 && windDirVal <= 300){
    Serial.println("S");
  } else if (windDirVal >= 620 && windDirVal <= 650){
    Serial.println("SW");
  } else if (windDirVal >= 930 && windDirVal <= 960){
    Serial.println("W");
  } else if (windDirVal >= 875 && windDirVal <= 905){
    Serial.println("NW");
  } else if (windDirVal >= 395 && windDirVal <= 415){
    Serial.println("N/NE");
  } else if (windDirVal >= 75 && windDirVal <= 86){
    Serial.println("E/NE");
  } else if (windDirVal >= 60 && windDirVal <= 70){
    Serial.println("E/SE");
  } else if (windDirVal >= 120 && windDirVal <= 130){
    Serial.println("S/SE");
  } else if (windDirVal >= 240 && windDirVal <= 250){
    Serial.println("S/SW");
  } else if (windDirVal >= 595 && windDirVal <= 605){
    Serial.println("W/SW");
  } else if (windDirVal >= 825 && windDirVal <= 835){
    Serial.println("W/NW");
  } else if (windDirVal >= 700 && windDirVal <= 710){
    Serial.println("N/NW");
  } else {
    Serial.println("ERROR");
  }

  // --------------------------------------------------- //
  // WIND SPEED //
  // --------------------------------------------------- //
  // Need to count the number of times the sensor jumps
  // between 0 and a positive value. Gives us RPM and
  // therefore speed.
  // Code source: https://www.aeq-web.com/arduino-anemometer-wind-sensor/?lang=en

  int start = millis() ;
    int t = 0;
    if (!analogRead(SPEED_PIN)){
      while( !analogRead(SPEED_PIN) && t < 3000)
      {
        t = millis() - start ;
      }
      while( analogRead(SPEED_PIN) && t < 3000)
      {
        t = millis() - start ;
      }
    }
    else {
      while( analogRead(SPEED_PIN) && t < 3000)
      {
        t = millis() - start ;
      }
      while( !analogRead(SPEED_PIN) && t < 3000)
      {
        t = millis() - start ;
      }
    }
    t = millis() - start ;
    float windSpeed = 0;
    if (t >= 3000){
      windSpeed = 0;
    }
    else{
     windSpeed = (1 /(float)t * 2000) * 1.4912904;
    }
    
  Serial.println(windSpeed);

  // --------------------------------------------------- //
  // SD CARD //
  // --------------------------------------------------- //

  // write to SD card
  if (!SD.begin(10)) {
    Serial.println("initialization failed!");
    while (1);
  }
  
  myFile = SD.open("data.txt", FILE_WRITE);
  if (myFile) {
    myFile.println("testing 1, 2, 3.");
    myFile.close();
  } else {
    // if the file didn't open, print an error:
    Serial.println("error opening test.txt");
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
