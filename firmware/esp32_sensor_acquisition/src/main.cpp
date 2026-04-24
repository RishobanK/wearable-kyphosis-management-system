#include <Arduino.h>
#include <Wire.h>
#include <MPU6050.h>

// EMG sensor pins
#define EMG_PIN_TOP_RIGHT     4
#define EMG_PIN_TOP_LEFT      26
#define EMG_PIN_MIDDLE_RIGHT  2
#define EMG_PIN_MIDDLE_LEFT   25
#define EMG_PIN_BOTTOM_RIGHT  15
#define EMG_PIN_BOTTOM_LEFT   33

// Vibration motor pins
#define MOTOR_TOP_LEFT        32
#define MOTOR_TOP_RIGHT       5
#define MOTOR_MIDDLE_LEFT     35
#define MOTOR_MIDDLE_RIGHT    18
#define MOTOR_BOTTOM_LEFT     34
#define MOTOR_BOTTOM_RIGHT    19

MPU6050 mpu1;
MPU6050 mpu2;

int emgData[6];

int16_t ax1, ay1, az1;
int16_t gx1, gy1, gz1;
int16_t ax2, ay2, az2;
int16_t gx2, gy2, gz2;

void setup() {
  Serial.begin(115200);

  pinMode(EMG_PIN_TOP_RIGHT, INPUT);
  pinMode(EMG_PIN_TOP_LEFT, INPUT);
  pinMode(EMG_PIN_MIDDLE_RIGHT, INPUT);
  pinMode(EMG_PIN_MIDDLE_LEFT, INPUT);
  pinMode(EMG_PIN_BOTTOM_RIGHT, INPUT);
  pinMode(EMG_PIN_BOTTOM_LEFT, INPUT);

  pinMode(MOTOR_TOP_LEFT, OUTPUT);
  pinMode(MOTOR_TOP_RIGHT, OUTPUT);
  pinMode(MOTOR_MIDDLE_LEFT, OUTPUT);
  pinMode(MOTOR_MIDDLE_RIGHT, OUTPUT);
  pinMode(MOTOR_BOTTOM_LEFT, OUTPUT);
  pinMode(MOTOR_BOTTOM_RIGHT, OUTPUT);

  Wire.begin();

  mpu1.initialize();
  mpu2.initialize();

  if (!mpu1.testConnection()) {
    Serial.println("MPU6050 1 not connected!");
  } else {
    Serial.println("MPU6050 1 connected.");
  }

  if (!mpu2.testConnection()) {
    Serial.println("MPU6050 2 not connected!");
  } else {
    Serial.println("MPU6050 2 connected.");
  }
}

void loop() {
  emgData[0] = analogRead(EMG_PIN_TOP_RIGHT);
  emgData[1] = analogRead(EMG_PIN_TOP_LEFT);
  emgData[2] = analogRead(EMG_PIN_MIDDLE_RIGHT);
  emgData[3] = analogRead(EMG_PIN_MIDDLE_LEFT);
  emgData[4] = analogRead(EMG_PIN_BOTTOM_RIGHT);
  emgData[5] = analogRead(EMG_PIN_BOTTOM_LEFT);

  Serial.print("EMG Top Right: ");
  Serial.print(emgData[0]);
  Serial.print(", EMG Top Left: ");
  Serial.print(emgData[1]);
  Serial.print(", EMG Middle Right: ");
  Serial.print(emgData[2]);
  Serial.print(", EMG Middle Left: ");
  Serial.print(emgData[3]);
  Serial.print(", EMG Bottom Right: ");
  Serial.print(emgData[4]);
  Serial.print(", EMG Bottom Left: ");
  Serial.println(emgData[5]);

  mpu1.getAcceleration(&ax1, &ay1, &az1);
  mpu1.getRotation(&gx1, &gy1, &gz1);

  mpu2.getAcceleration(&ax2, &ay2, &az2);
  mpu2.getRotation(&gx2, &gy2, &gz2);

  Serial.print("MPU1 Accel: X=");
  Serial.print(ax1);
  Serial.print(", Y=");
  Serial.print(ay1);
  Serial.print(", Z=");
  Serial.println(az1);

  Serial.print("MPU1 Gyro: X=");
  Serial.print(gx1);
  Serial.print(", Y=");
  Serial.print(gy1);
  Serial.print(", Z=");
  Serial.println(gz1);

  Serial.print("MPU2 Accel: X=");
  Serial.print(ax2);
  Serial.print(", Y=");
  Serial.print(ay2);
  Serial.print(", Z=");
  Serial.println(az2);

  Serial.print("MPU2 Gyro: X=");
  Serial.print(gx2);
  Serial.print(", Y=");
  Serial.print(gy2);
  Serial.print(", Z=");
  Serial.println(gz2);

  delay(500);
}