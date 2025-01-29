# Video https://youtu.be/TgXlUb0fcmA
# Post http://kontakts.ru/showthread.php/40884?p=86201#post86201
# Telega https://t.me/MrMicroPython
# 📜 Лицензия 🔗 Creative Commons Attribution-ShareAlike 4.0 (CC BY-SA)
# 📂 Оригинальный код для платы PicoMate https://wiki.deskpi.com/picomate/#pinout-diagram
import time  # Модуль для работы со временем (задержки)
import board  # Модуль для работы с пинами микроконтроллера
import neopixel  # Модуль для управления адресными светодиодами NeoPixel

# Определяем цвета в формате RGB (Red, Green, Blue)
R = (50, 0, 0)  # Красный цвет с яркостью 50
G = (0, 50, 0)  # Зеленый цвет с яркостью 50
B = (0, 0, 50)  # Синий цвет с яркостью 50

# Список доступных цветов
COLORS = (R, G, B)

# Инициализируем NeoPixel на GPIO 22 с 1 светодиодом
pixels = neopixel.NeoPixel(board.GP22, 1)

# Бесконечный цикл смены цветов
while True:
    for color in COLORS:  # Перебираем каждый цвет из списка
        pixels[0] = color  # Устанавливаем цвет для первого (и единственного) светодиода
        time.sleep(1)  # Ждем 1 секунду перед сменой цвета
