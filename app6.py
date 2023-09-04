import pyautogui
import time

# Abre el menú Inicio (puedes ajustar la ubicación según tu resolución de pantalla)
pyautogui.hotkey('win', 'r')
time.sleep(1)

# Escribe "WhatsApp" y presiona Enter (ajusta esto según el nombre de la aplicación)
pyautogui.write("chrome")
pyautogui.press('enter')

# Espera a que el navegador se abra (ajusta el tiempo según la velocidad de tu sistema)51997322971

time.sleep(5)

# Abre WhatsApp Web (ajusta las coordenadas según tu resolución de pantalla)
#pyautogui.click(x=500, y=500)  # Reemplaza estas coordenadas con las correctas
pyautogui.hotkey('ctrl','l')
pyautogui.write("https://web.whatsapp.com/")
pyautogui.press('enter')

# Espera a que se cargue WhatsApp Web (ajusta el tiempo según la velocidad de tu sistema)
time.sleep(10)

# Ingresa el número de teléfono y el mensaje
pyautogui.write("51997322971")
pyautogui.press('enter')
time.sleep(2)
pyautogui.write("Mensaje de prueba")
pyautogui.press('enter')

# Realiza un clic en una posición específica en la pantalla (por ejemplo, x=600, y=600)
pyautogui.click(x=600, y=600)

# Cierra el navegador (ajusta las coordenadas según tu resolución de pantalla)
pyautogui.hotkey('alt', 'f4')

# Puedes agregar más acciones de PyAutoGUI según tus necesidades