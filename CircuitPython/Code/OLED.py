# Video https://youtu.be/XvvTKivE40c
# Post http://kontakts.ru/showthread.php/40884?p=86205#post86205
# Telega https://t.me/MrMicroPython
# 📜 Лицензия 🔗 Creative Commons Attribution-ShareAlike 4.0 (CC BY-SA)
# 📂 Оригинальный код для платы PicoMate https://wiki.deskpi.com/picomate/#pinout-diagram
import time  # Импортируем модуль для работы с задержками
import board  # Импортируем модуль для работы с пинами микроконтроллера
import busio  # Импортируем модуль для работы с I2C, SPI и UART
from adafruit_ssd1306 import SSD1306_I2C  # Импортируем драйвер для OLED-дисплея SSD1306

# Создаём объект I2C на портах GP17 (SCL) и GP16 (SDA)
i2c0 = busio.I2C(scl=board.GP17, sda=board.GP16)

# Инициализация OLED-дисплея 0.96" с разрешением 128x64 пикселя
display = SSD1306_I2C(128, 64, i2c0)

# Функция для вывода текста на экран
def display_text(str, line):
    """
    Отображает строку текста на OLED-дисплее.

    Аргументы:
    str  - текстовая строка для отображения
    line - номер строки (0-7), каждая строка занимает 8 пикселей по высоте
    """
    display.text(str, 0, (line % 8) * 8, 1, font_name="/lib/font5x8.bin")  # Выводим текст на указанной строке

# Бесконечный цикл для обновления экрана
while True:
    display.fill(0)  # Очищаем экран (заполняем черным)

    display_text("Hello, World!", 0)  # Выводим текст на первую строку дисплея
    display_text("It's DeskPi PicoMate!", 2)  # Выводим текст на третью строку дисплея

    display.show()  # Обновляем дисплей, чтобы изменения стали видимыми

    time.sleep(0.5)  # Делаем паузу в 0.5 секунды перед следующим обновлением
