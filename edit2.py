import pyautogui
import time

# Abre el menú Inicio (puedes ajustar la ubicación según tu resolución de pantalla)
pyautogui.hotkey('win', 'r')
time.sleep(1)

# Escribe "WhatsApp" y presiona Enter (ajusta esto según el nombre de la aplicación)
pyautogui.write("WhatsApp")
pyautogui.press('enter')