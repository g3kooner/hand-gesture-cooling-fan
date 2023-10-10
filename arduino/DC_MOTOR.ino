#include <cvzone.h>
#include <LiquidCrystal.h>

SerialData serialData(1, 3);

#define BUTTON 2
#define ENABLE 13
#define DIRA 11
#define DIRB 12
LiquidCrystal lcd(3, 4, 5, 6, 7, 8);
 
int i;
int button = 0;
int valuesRec[1];

void setup() {
  // put your setup code here, to run once:
  pinMode(ENABLE,OUTPUT);
  pinMode(DIRA,OUTPUT);
  pinMode(DIRB,OUTPUT);
  pinMode(BUTTON, INPUT);

  lcd.begin(16, 1);
  lcd.print("   Status: ON");
  Serial.begin(9600);

  serialData.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly: 
  serialData.Get(valuesRec);

  digitalWrite(DIRA,HIGH); //one way
  digitalWrite(DIRB,LOW);
  analogWrite(ENABLE, valuesRec[0]); //enable on

  button = digitalRead(BUTTON);
  if (button == 1) {
    lcd.clear();
    lcd.print(" Status: PAUSED");

    while(digitalRead(BUTTON) == 1){}
    while(digitalRead(BUTTON) == 0 ){}

    lcd.clear();
    lcd.print("  Status: ON");
    delay(1000);
  }
}
