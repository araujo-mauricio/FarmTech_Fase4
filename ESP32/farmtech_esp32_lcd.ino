#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// Inicialização do LCD (endereço 0x27)
LiquidCrystal_I2C lcd(0x27, 16, 2);

// Sensores simulados via potenciômetro no Wokwi
const int sensorUmidade = 34;
const int sensorNutriente = 35;

// Variáveis otimizadas
int leituraUmidade = 0;
int leituraNutriente = 0;
float umidadePercent = 0;
float nutrientePercent = 0;

void setup() {
  Serial.begin(115200);

  lcd.init();
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("FarmTech Init");
  delay(2000);

  pinMode(sensorUmidade, INPUT);
  pinMode(sensorNutriente, INPUT);
}

void loop() {
  leituraUmidade = analogRead(sensorUmidade);
  leituraNutriente = analogRead(sensorNutriente);

  umidadePercent = (float)leituraUmidade * 100.0 / 4095.0;
  nutrientePercent = (float)leituraNutriente * 100.0 / 4095.0;

  Serial.print("Umidade: ");
  Serial.print(umidadePercent, 1);
  Serial.print("% | Nutriente: ");
  Serial.print(nutrientePercent, 1);
  Serial.println("%");

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("U:");
  lcd.print(umidadePercent, 0);
  lcd.print("% N:");
  lcd.print(nutrientePercent, 0);
  lcd.print("%");

  delay(2000);
}