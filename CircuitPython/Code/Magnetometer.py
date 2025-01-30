# Video https://youtu.be/rOdW0SOZBA8
# Post http://kontakts.ru/showthread.php/40884?p=86209#post86209
# Telega https://t.me/MrMicroPython
# 📜 Лицензия 🔗 Creative Commons Attribution-ShareAlike 4.0 (CC BY-SA)
# 📂 Оригинальный код для платы PicoMate https://wiki.deskpi.com/picomate/#pinout-diagram
import time 
import board 
import busio
from adafruit_mmc56x3 import MMC5603  # Импортируем библиотеку для работы с магнитометром MMC5603

# Настройка I2C интерфейса для общения с магнитометром
i2c1 = busio.I2C(scl = board.GP15, sda = board.GP14)  # Устанавливаем I2C с пинами GP15 для SCL и GP14 для SDA

# Инициализация магнитометра MMC5603, подключенного к шине I2C
magnetometer = MMC5603(i2c1)

# Устанавливаем частоту обновления данных магнитометра в 1000 Гц (значение может варьироваться от 1 до 1000 Гц)
magnetometer.data_rate = 1000   # Частота обновления данных в герцах (от 1 до 255 или 1000)

# Включаем непрерывный режим работы магнитометра, чтобы он постоянно передавал данные
magnetometer.continuous_mode = True

# Основной цикл для получения данных о магнитном поле
while True:
    # Чтение данных о магнитном поле (магнитные компоненты по осям X, Y, Z)
    print(magnetometer.magnetic)
    
    # Задержка на 0.1 секунды перед следующим измерением
    time.sleep(0.1)
