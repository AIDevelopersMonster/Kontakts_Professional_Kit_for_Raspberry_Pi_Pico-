# Video https://youtu.be/IX0w0CLMyTs
# Post  http://kontakts.ru/showthread.php/40884?p=86162#post86162
from machine import Pin, Timer,I2C
import utime
from ssd1306 import SSD1306_I2C
import framebuf
# Инициализация I2C
i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)
# Включение отладки для мониторинга
debug = True
# Раскладка кнопок на клавиатуре
# Описание кнопок:
# Цифры (0-9) — стандартные цифры для ввода чисел.
# A — это знак сложения '+'
# B — это знак вычитания '-'
# C — это знак умножения '*'
# D — это знак деления '/'
# * — очищает текущий ввод (сбрасывает все введенные данные)
# # (equals) — = выводит результат

keyName = [['1','2','3','+'],
           ['4','5','6','-'],
           ['7','8','9','*'],
           ['c','0','=','/']]
keypadRowPins = [13, 12, 11, 10]
keypadColPins = [9, 8, 7, 6]

# Инициализация строк и столбцов для клавиатуры
row = []
col = []
keypadState = []
for i in keypadRowPins:
    row.append(Pin(i, Pin.IN, Pin.PULL_UP))
    keypadState.append([0, 0, 0, 0])
for i in keypadColPins:
    col.append(Pin(i, Pin.OUT))

# Функция для выполнения операций калькулятора
def solve(oprt, oprdA, oprdB):
    if oprt == "+":
        return oprdA + oprdB
    elif oprt == "-":
        return oprdA - oprdB
    elif oprt == "*":
        return oprdA * oprdB
    elif oprt == "/":
        return round(oprdA / oprdB, 6)

# Основная функция для вычислений
def calc(lst):
    operand = []
    operator = []

    # Обработка каждого элемента в списке lst
    for i in lst:
        if debug:
            print(i)
        if i == '+':
            while len(operator) != 0 and (operator[-1] == '*' or operator[-1] == '/' or operator[-1] == '-' or operator[-1] == '+'):
                b = operand.pop(-1)
                a = operand.pop(-1)
                c = operator.pop(-1)
                operand.append(solve(c, a, b))
            operator.append(i)
        elif i == '-':
            while len(operator) != 0 and (operator[-1] == '*' or operator[-1] == '/' or operator[-1] == '-' or operator[-1] == '+'):
                b = operand.pop(-1)
                a = operand.pop(-1)
                c = operator.pop(-1)
                operand.append(solve(c, a, b))
            operator.append(i)
        elif i == '*':
            while len(operator) != 0 and (operator[-1] == '*' or operator[-1] == '/'):
                b = operand.pop(-1)
                a = operand.pop(-1)
                c = operator.pop(-1)
                operand.append(solve(c, a, b))
            operator.append(i)
        elif i == '/':
            while len(operator) != 0 and (operator[-1] == '*' or operator[-1] == '/'):
                b = operand.pop(-1)
                a = operand.pop(-1)
                c = operator.pop(-1)
                operand.append(solve(c, a, b))
            operator.append(i)
        elif i == '(':
            operator.append(i)
        elif i == ')':
            while operator[-1] != '(':
                b = operand.pop(-1)
                a = operand.pop(-1)
                c = operator.pop(-1)
                operand.append(solve(c, a, b))
            operator.pop(-1)
        else:
            operand.append(i)

    # Выполнение оставшихся операций
    while len(operator) != 0:
        b = operand.pop(-1)
        a = operand.pop(-1)
        c = operator.pop(-1)
        operand.append(solve(c, a, b))

    return operand[0]

# Функция для считывания нажатой кнопки
def keypadRead():
    global row
    j_ifPressed = -1
    i_ifPressed = -1
    for i in range(0, len(col)):
        col[i].low()
        utime.sleep(0.005)  # Время для стабилизации
        for j in range(0, len(row)):
            pressed = not row[j].value()
            if pressed and (keypadState[j][i] != pressed):  # Если состояние кнопки изменилось
                keypadState[j][i] = pressed
            elif not pressed and (keypadState[j][i] != pressed):  # Если состояние кнопки изменилось на отпущенное
                keypadState[j][i] = pressed
                j_ifPressed = j
                i_ifPressed = i
        col[i].high()
    if j_ifPressed != -1 and i_ifPressed != -1:
        return keyName[j_ifPressed][i_ifPressed]
    else:
        return -1

# Функция для вывода данных на OLED дисплей
def printOled(lst):
    oledPos = {
            "x": 0,
            "y": 0
          }

    oled.fill(0)
    string = ''
    for i in lst:
        string += str(i)
    l = 0
    while l < len(string):
        oled.text(string[l:l + 16], oledPos["x"], oledPos["y"])
        oledPos["y"] = oledPos["y"] + 10
        l = l + 16
    oled.show()

# Инициализация дисплея и приветственное сообщение
shiftFlag = False
signFlag = False
inputList = ['']

oled.show()
oled.fill(0)
oled.show()
oled.text("Elecrow", 30, 9, 1)
oled.text("Simple", 35, 28, 1)
oled.text("calculator", 18, 38, 1)
oled.show()

if __name__ == '__main__':
    while True:
        key = keypadRead()

        if key != -1:
            if (key <= '9' and key >= '0') or key == '.':
                inputList[-1] = inputList[-1] + key
            elif key == '+' or key == '-' or key == '*' or key == '/':
                if inputList != ['']:
                    if inputList[-1] == '' and (inputList[-2] == '+' or inputList[-2] == '-' or inputList[-2] == '*' or inputList[-2] == '/'):
                        inputList[-2] = key
                    elif inputList[-1] == '':
                        inputList[-1] = key
                        inputList.append('')
                    else:
                        inputList[-1] = float(inputList[-1])
                        inputList.append(key)
                        inputList.append('')
            elif key == 's':
                shiftFlag = not shiftFlag
            elif key == 'a':
                if shiftFlag:
                    if inputList[-1] != '':
                        inputList[-1] = float(inputList[-1])
                        inputList.append(')')
                        inputList.append('')
                    else:
                        inputList[-1] = ')'
                        inputList.append('')
                    shiftFlag = False
                else:
                    signFlag = not signFlag
                    if inputList[-1] == '':
                        inputList[-1] = '-'
                    else:
                        if inputList[-1][0] == '-':
                            inputList[-1] = inputList[-1][1:]
                        else:
                            inputList[-1] = '-' + inputList[-1]

            elif key == 'b':
                if shiftFlag:
                    if inputList[-1] == '':
                        inputList[-1] = '('
                    else:
                        inputList.append('(')
                    inputList.append('')
                    shiftFlag = False
                else:
                    if inputList[-1] == '':
                        inputList[-1] = 3.14
                    else:
                        inputList.append(3.14)
                    inputList.append('')
            elif key == 'c':
                if shiftFlag:
                    inputList = ['']
                    shiftFlag = False
                else:
                    if inputList == ["error"]:
                        inputList = ['']
                    if inputList != ['']:
                        if inputList[-1] == '':
                            inputList.pop()
                            inputList[-1] = str(inputList[-1])[:-1]
                        else:
                            inputList[-1] = str(inputList[-1])[:-1]
            elif key == '=':
                if inputList[-1] == '':
                    inputList.pop(-1)
                elif inputList[-1] != ')':
                    inputList[-1] = float(inputList[-1])
                try:
                    ans = calc(inputList)
                    inputList = [str(ans)]
                except:
                    ans = ''
                    inputList = []
                    inputList.append("error")

            # Вывод на OLED дисплей и монитор порта
            printOled(inputList)
            print(inputList)  # Выводим результат в монитор порта




