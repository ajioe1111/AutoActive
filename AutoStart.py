import subprocess
import time
import pyautogui


# Чтение пути к программе из файла
with open('path.txt', 'r', encoding='utf-8') as file:
    program_path = file.read().strip()

# Запуск программы
subprocess.Popen(program_path)

# Пауза для того, чтобы программа успела открыться
time.sleep(20)

# Нажатие клавиши "1"
pyautogui.press('1')

# Пауза
time.sleep(20)

# Нажатие клавиши "Enter"
pyautogui.press('enter')

