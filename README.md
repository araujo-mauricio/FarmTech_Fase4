# FarmTech Solutions - Fase 4 - Sistema Inteligente de Irrigação

---

## Objetivo

Projeto desenvolvido para a Fase 4 da FIAP — FarmTech Solutions.

A proposta foi aprimorar o sistema de irrigação automatizado desenvolvido na Fase 3, agora integrando:

- Machine Learning com Scikit-Learn
- Dashboard interativo com Streamlit
- Banco de Dados SQLite
- Monitoramento físico no ESP32 (Wokwi)
- Visualização de variáveis em tempo real

---

## Tecnologias Utilizadas

- Python 3
- SQLite
- Scikit-Learn
- Streamlit
- ESP32 (Wokwi)
- C/C++
- LiquidCrystal I2C (biblioteca Wokwi)

---

## Arquitetura do Projeto

```
FarmTech_Fase4/
│
├── Banco_de_dados/
│   ├── criar_banco.py
│   └── farmtech.db
│
├── Dashboard/
│   └── farmtech_dashboard.py
│
├── ESP32/
│   ├── diagram.json
│   └── farmtech_esp32_lcd.ino
│
├── Machine_Learning/
│   └── modelo_irrigacao.py
│
├── Prints/
│   └── wokwi_circuito_montado.png
│
└── README.md
```

## Como Executar

### 1 Banco de Dados

```bash
python criar_banco.py
```

### 2 Treinamento do Modelo

```bash
python modelo_irrigacao.py
```

### 3 Executar o Dashboard

```bash
streamlit run farmtech_dashboard.py
```

### 4 Simulação ESP32

- Projeto criado manualmente no Wokwi
- LCD 16x2 (I2C)
- 2 Potenciômetros simulando sensores de Umidade e Nutrientes
- Código C++ no farmtech_esp32_lcd.ino

---

## Prints da Simulação (Wokwi)

### Circuito Montado
![Circuito Montado no Wokwi](Prints/wokwi_circuito_montado.png)

### Projeto montado no Wokwi  
[Clique e acesse o projeto funcionando](https://wokwi.com/projects/433779477529291777)

---

## Vídeo Demonstrativo

- Link do vídeo no Youtube:  
(https://youtu.be/AgKmg9TUS5U)

---

## Integrantes
- Mauricio Araújo - RM566040
- Igor Herson - RM563980