# Video https://youtu.be/nbHxZ0Id58M
# Post http://kontakts.ru/showthread.php/40884?p=86206#post86206
# Telega https://t.me/MrMicroPython
# 📜 Лицензия 🔗 Creative Commons Attribution-ShareAlike 4.0 (CC BY-SA)
# 📂 Оригинальный код для платы PicoMate https://wiki.deskpi.com/picomate/#pinout-diagram
import time  # Импортируем модуль для работы с задержками
import array  # Импортируем модуль для работы с массивами
import math  # Импортируем модуль для математических вычислений
import board  # Импортируем модуль для работы с пинами микроконтроллера
import audiobusio  # Импортируем модуль для работы с аудиодатчиками через PDM

# Функция для вычисления среднего значения массива (используется для удаления смещения DC)
def mean(values):
    """
    Вычисляет среднее арифметическое списка значений.

    Аргументы:
    values - список числовых значений

    Возвращает:
    Среднее значение списка
    """
    return sum(values) / len(values)

# Функция для вычисления нормализованного RMS (Root Mean Square - среднеквадратичное значение)
def normalized_rms(values):
    """
    Вычисляет нормализованное среднеквадратичное значение (RMS).

    Аргументы:
    values - массив аудиосемплов

    Возвращает:
    RMS уровень аудиосигнала
    """
    minbuf = int(mean(values))  # Вычисляем среднее значение для удаления DC-смещения
    samples_sum = sum(
        float(sample - minbuf) * (sample - minbuf) for sample in values)  # Вычисляем сумму квадратов отклонений

    return math.sqrt(samples_sum / len(values))  # Извлекаем квадратный корень для получения RMS

# Инициализация PDM-микрофона
mic = audiobusio.PDMIn(
    board.GP9, board.GP8,  # GP9 - Data (DOUT), GP8 - Clock (CLK)
    sample_rate=16000,  # Частота дискретизации 16 кГц
    bit_depth=16  # Глубина битности 16 бит
)

# Создаем массив для хранения аудиосемплов (160 значений типа 'H' - 16-битные числа)
samples = array.array('H', [0] * 160)

# Основной цикл для записи и анализа аудиосигнала
while True:
    mic.record(samples, len(samples))  # Записываем 160 сэмплов с микрофона
    magnitude = normalized_rms(samples)  # Вычисляем RMS уровень сигнала
    print((magnitude,))  # Выводим результат в консоль (для использования в Plotter в Mu Editor)
    time.sleep(0.1)  # Делаем паузу в 100 мс перед следующей записью

