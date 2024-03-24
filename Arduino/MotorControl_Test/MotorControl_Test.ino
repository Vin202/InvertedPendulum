// Motor A
const int pin1 = 4;  // Connect to L298N IN1
const int pin2 = 5;  // Connect to L298N IN2
const int enable = 3;  // Connect to L298N ENA

void setup() {
  // Set motor control pins as outputs
  pinMode(pin1, OUTPUT);
  pinMode(pin2, OUTPUT);
  pinMode(enable, OUTPUT);
}

void loop() {
  // Run the motor in one direction for 2 seconds
  digitalWrite(pin1, HIGH);
  digitalWrite(pin2, LOW);
  analogWrite(enable, 50);  // Set motor speed (0 to 255)
  delay(2000);

  // Stop the motor for 1 second
  digitalWrite(pin1, LOW);
  digitalWrite(pin2, LOW);
  analogWrite(enable, 0);
  delay(1000);

  // Run the motor in the opposite direction for 2 seconds
  digitalWrite(pin1, LOW);
  digitalWrite(pin2, HIGH);
  analogWrite(enable, 255);
  delay(2000);

  // Stop the motor for 1 second
  digitalWrite(pin1, LOW);
  digitalWrite(pin2, LOW);
  analogWrite(enable, 0);
  delay(1000);
}
