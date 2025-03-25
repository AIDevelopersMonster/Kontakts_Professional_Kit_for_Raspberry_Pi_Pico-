# Video https://youtu.be/Ub-NpSWvNr8
# Post http://kontakts.ru/showthread.php/40884?p=86210#post86210
# Telega https://t.me/MrMicroPython
# 📜 Лицензия 🔗 Creative Commons Attribution-ShareAlike 4.0 (CC BY-SA)
# 📂 Оригинальный код для платы PicoMate https://wiki.deskpi.com/picomate/#pinout-diagram

import time 
import board 
import busio
from ltr381rgb import LTR381RGB  # Импорт библиотеки для работы с оптическим сенсором LTR381RGB

# Настройка I2C интерфейса с использованием пинов GP15 (SCL) и GP14 (SDA) на плате
i2c1 = busio.I2C(scl = board.GP15, sda = board.GP14)

# Инициализация оптического сенсора LTR381RGB через I2C
optical = LTR381RGB(i2c1) 

# Установка режима работы сенсора на "CS" (Color Sensing, для измерения освещенности и цвета)
optical.mode = "CS" 

# Включение сенсора
optical.enable()

# Бесконечный цикл для вывода данных
while True:
    # Получение и вывод измеренной освещенности в люксах (lux)
    print(f"ALS: {optical.lux} lx") 

    # Вывод необработанных данных сенсора (например, для диагностики или анализа)
    print(optical.raw_data) 

    # Пауза на 0.5 секунды перед следующим циклом
    time.sleep(0.5)

