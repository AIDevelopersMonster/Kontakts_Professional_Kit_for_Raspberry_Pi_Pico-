# Video https://youtu.be/SpZiV2xJ1zA
# Post http://kontakts.ru/showthread.php/40884?p=86208#post86208
# Telega https://t.me/MrMicroPython
# 📜 Лицензия 🔗 Creative Commons Attribution-ShareAlike 4.0 (CC BY-SA)
# 📂 Оригинальный код для платы PicoMate https://wiki.deskpi.com/picomate/#pinout-diagram
import time  # Импортируем модуль time для работы с задержками
import board  # Импортируем модуль для работы с пинами платы
import busio  # Импортируем модуль для работы с интерфейсом I2C
from adafruit_lsm6ds.lsm6ds3trc import LSM6DS3TRC  # Импортируем класс LSM6DS3TRC из библиотеки для работы с датчиком

# Настройка I2C интерфейса с использованием пинов GP15 (SCL) и GP14 (SDA) на Raspberry Pi Pico
i2c1 = busio.I2C(scl = board.GP15, sda = board.GP14)

# Инициализация сенсора LSM6DS3TRC с использованием I2C интерфейса
imu_sensor = LSM6DS3TRC(i2c1)

# Бесконечный цикл для вывода показаний акселерометра
while True:
    # Печатаем показания акселерометра, которые включают значения по осям X, Y и Z
    print(imu_sensor.acceleration) 
    # Задержка 0.1 секунды перед следующим измерением
    time.sleep(0.1)

# Следующий код для гироскопа закомментирован. Если необходимо, раскомментируйте его
# Gyro plotter 
# while True:
#     # Печатаем показания гироскопа, которые включают значения угловой скорости по осям X, Y и Z
#     print(imu_sensor.gyro) 
#     # Задержка 0.1 секунды перед следующим измерением
#     time.sleep(0.1)
