# Video https://youtu.be/KzB65K-rlGk
# Post http://kontakts.ru/showthread.php/40884?p=86207#post86207
# Telega https://t.me/MrMicroPython
# 📜 Лицензия 🔗 Creative Commons Attribution-ShareAlike 4.0 (CC BY-SA)
# 📂 Оригинальный код для платы PicoMate https://wiki.deskpi.com/picomate/#pinout-diagram
import board  # Импортируем модуль для работы с пинами микроконтроллера
import digitalio  # Импортируем модуль для работы с цифровыми входами/выходами

# Инициализация PIR-датчика движения (подключён к GP28)
pir_sensor = digitalio.DigitalInOut(board.GP28)  # Указываем, что датчик подключён к GP28
pir_sensor.direction = digitalio.Direction.INPUT  # Устанавливаем пин как вход
pir_sensor.pull = digitalio.Pull.DOWN  # Включаем подтягивающий резистор к GND (Pull.DOWN)

# Переменная для хранения предыдущего состояния датчика
last_value = pir_sensor.value

# Бесконечный цикл для отслеживания изменений состояния PIR-датчика
while True:
    if last_value != pir_sensor.value:  # Если состояние изменилось (сработал или перестал срабатывать)
        last_value = pir_sensor.value  # Обновляем предыдущее состояние
        # Выводим сообщение о движении или его отсутствии
        print('Motion ' + ('detected!' if pir_sensor.value else 'removed!'))
