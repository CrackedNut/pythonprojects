#define BPIN 7

int tempo = 750;
int a = 1;

void melody() {
	tone(BPIN, 587, 2*tempo);
	delay(2*tempo);
	tone(BPIN, 440, 2*tempo);
	delay(2*tempo);
	tone(BPIN, 494, 2*tempo);
	delay(2*tempo);
	tone(BPIN, 370, 2*tempo);
	delay(2*tempo);
	tone(BPIN, 392, 2*tempo);
	delay(2*tempo);
	tone(BPIN, 293, 2*tempo);
	delay(2*tempo);
	tone(BPIN, 392, 2*tempo);
	delay(2*tempo);
	tone(BPIN, 440, 2*tempo);
	delay(2*tempo);
	tone(BPIN, 740, 2*tempo);
	delay(2*tempo);
	tone(BPIN, 659, 2*tempo);
	delay(2*tempo);
	tone(BPIN, 587, 2*tempo);
	delay(2*tempo);
	tone(BPIN, 554, 2*tempo);
	delay(2*tempo);
	tone(BPIN, 494, 2*tempo);
	delay(2*tempo);
	tone(BPIN, 440, 2*tempo);
	delay(2*tempo);
	tone(BPIN, 494, 2*tempo);
	delay(2*tempo);
	tone(BPIN, 554, 2*tempo);
	delay(2*tempo);
	tone(BPIN, 587, 2*tempo);
	delay(2*tempo);
	tone(BPIN, 554, 2*tempo);
	delay(2*tempo);
	tone(BPIN, 494, 2*tempo);
	delay(2*tempo);
	tone(BPIN, 440, 2*tempo);
	delay(2*tempo);
	tone(BPIN, 392, 2*tempo);
	delay(2*tempo);
	tone(BPIN, 370, 2*tempo);
	delay(2*tempo);
	tone(BPIN, 392, 2*tempo);
	delay(2*tempo);
	tone(BPIN, 329, 2*tempo);
	delay(2*tempo);
	tone(BPIN, 293, 1*tempo);
	delay(1*tempo);
	tone(BPIN, 370, 1*tempo);
	delay(1*tempo);
	tone(BPIN, 440, 1*tempo);
	delay(1*tempo);
	tone(BPIN, 392, 1*tempo);
	delay(1*tempo);
	tone(BPIN, 370, 1*tempo);
	delay(1*tempo);
	tone(BPIN, 293, 1*tempo);
	delay(1*tempo);
	tone(BPIN, 370, 1*tempo);
	delay(1*tempo);
	tone(BPIN, 329, 1*tempo);
	delay(1*tempo);
	tone(BPIN, 293, 1*tempo);
	delay(1*tempo);
	tone(BPIN, 247, 1*tempo);
	delay(1*tempo);
	tone(BPIN, 293, 1*tempo);
	delay(1*tempo);
	tone(BPIN, 440, 1*tempo);
	delay(1*tempo);
	tone(BPIN, 392, 1*tempo);
	delay(1*tempo);
	tone(BPIN, 494, 1*tempo);
	delay(1*tempo);
	tone(BPIN, 440, 1*tempo);
	delay(1*tempo);
	tone(BPIN, 392, 1*tempo);
	delay(1*tempo);
	tone(BPIN, 370, 1*tempo);
	delay(1*tempo);
	tone(BPIN, 587, 1*tempo);
	delay(1*tempo);
	tone(BPIN, 659, 1*tempo);
	delay(1*tempo);
	tone(BPIN, 554, 1*tempo);
	delay(1*tempo);
	tone(BPIN, 587, 1*tempo);
	delay(1*tempo);
	tone(BPIN, 740, 1*tempo);
	delay(1*tempo);
	tone(BPIN, 880, 1*tempo);
	delay(1*tempo);
	tone(BPIN, 440, 1*tempo);
	delay(1*tempo);
	tone(BPIN, 494, 1*tempo);
	delay(1*tempo);
	tone(BPIN, 392, 1*tempo);
	delay(1*tempo);
	tone(BPIN, 440, 1*tempo);
	delay(1*tempo);
	tone(BPIN, 370, 1*tempo);
	delay(1*tempo);
	tone(BPIN, 293, 1*tempo);
	delay(1*tempo);
	tone(BPIN, 587, 1*tempo);
	delay(1*tempo);
	tone(BPIN, 587, 1*tempo);
	delay(1*tempo);
	tone(BPIN, 587, 0.125*tempo);
	delay(0.125*tempo);
	tone(BPIN, 554, 0.125*tempo);
	delay(0.125*tempo);
	tone(BPIN, 587, 2*tempo);
	delay(2*tempo);
	delay(2*tempo);
}

void setup() {

}

void loop() {
  while(a<2) {
    melody();
    a++;
  }
}
