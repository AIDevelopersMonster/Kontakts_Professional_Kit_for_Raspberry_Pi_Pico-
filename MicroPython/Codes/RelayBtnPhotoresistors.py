# Video https://youtu.be/xUFz9EuGOl4
# Post http://kontakts.ru/showthread.php/40884?p=86197#post86197
# Telega https://t.me/MrMicroPython
from machine import Pin, ADC
import time

# Инициализация реле (GPIO 16)
relay = Pin(16, Pin.OUT)

# Инициализация кнопки (GPIO 15, с подтяжкой PULL_UP)
button = Pin(15, Pin.IN, Pin.PULL_UP)

# Инициализация фоторезистора (ADC0 - GPIO26)
photoresistor = ADC(26)

# Флаг включения режима автоматического управления реле
auto_mode = False

# Порог включения и выключения реле
THRESHOLD_ON = 2000   # Включение при освещенности ниже 2000
THRESHOLD_OFF = 8000  # Выключение при освещенности выше 8000

# Переменная для хранения состояния реле
relay_state = False

# Функции управления реле
def relay_on():
    global relay_state
    relay.value(1)
    relay_state = True

def relay_off():
    global relay_state
    relay.value(0)
    relay_state = False

# Основной цикл программы
while True:
    # Читаем значение с фоторезистора
    light_level = photoresistor.read_u16()

    # Вывод в серийный монитор
    print(f"Освещенность (A0): {light_level} | Режим: {'Авто' if auto_mode else 'Выкл'} | Реле: {'ВКЛ' if relay_state else 'ВЫКЛ'}")

    # Проверяем нажатие кнопки (активный LOW)
    if button.value() == 0:
        time.sleep(0.05)  # Дебаунс
        if button.value() == 0:  # Повторная проверка
            auto_mode = not auto_mode  # Переключаем режим
            print(f"Авто-режим {'включен' if auto_mode else 'выключен'}")
            
            # Ожидание отпускания кнопки
            while button.value() == 0:
                time.sleep(0.05)

    # Управление реле с гистерезисом
    if auto_mode:
        if light_level < THRESHOLD_ON and not relay_state:  # Включаем реле при темноте
            relay_on()
            print("🌙 Темно! Реле ВКЛЮЧЕНО!")

        elif light_level > THRESHOLD_OFF and relay_state:  # Выключаем реле при свете
            relay_off()
            print("☀️ Светло! Реле ВЫКЛЮЧЕНО!")
    else:
        relay_off()  # Если авто-режим выключен, реле всегда выключено

    time.sleep(0.5)  # Задержка для стабильности
