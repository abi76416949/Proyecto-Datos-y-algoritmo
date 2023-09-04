from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Número de veces que deseas enviar el mensaje con imagen
num_envios = 5


# Iniciar el navegador (asegúrate de tener el controlador de WebDriver correspondiente)
driver = webdriver.Chrome()

#--------------------CREAR UN ARCHIVO TXT PARA GUARDAR COOKIES--------------------------------
archivo = 'contra.txt'
try:
    with open(archivo, "w") as archivo:
        
        pass
    
        # Puedes agregar más contenido aquí si lo deseas
    
except IOError as e:
    print(f"No se pudo crear el archivo '{archivo}': {e}")
# Abre WhatsApp Web
driver.get("./gato.png")

time.sleep(15)  # Espera a que cargue WhatsApp Web
cookies = driver.get_cookies()
archivo_nombre = 'contra.txt'
with open(archivo_nombre,"a") as archivo_nombre:
    archivo_nombre.write(str(cookies))

# Función para enviar un mensaje con imagen
def enviar_mensaje_con_imagen(contacto, mensaje, imagen_path):
    input_box = driver.find_element_by_xpath("//div[@contenteditable='true']")
    input_box.send_keys(contacto + Keys.ENTER)

    # Adjuntar imagen
    attachment_button = driver.find_element_by_xpath("//div[@title='Adjuntar']")
    attachment_button.click()

    image_input = driver.find_element_by_xpath("//input[@accept='image/*,video/mp4,video/3gpp,video/quicktime']")
    image_input.send_keys(imagen_path)
    time.sleep(3)  # Espera a que se cargue la imagen

    # Enviar mensaje
    send_button = driver.find_element_by_xpath("//span[@data-icon='send']")
    send_button.click()

# Loop para enviar mensajes con imágenes
for i in range(num_envios):
    texto = f"Felicitaciones  {i + 1}"
    imagen_path = "gato.png"  # Ruta de la imagen que deseas enviar
    
    enviar_mensaje_con_imagen("+51 997 322 971", texto, imagen_path)

    # Espera un tiempo antes de enviar el siguiente mensaje con imagen
    if i < num_envios - 1:
        tiempo_espera = 10  # Tiempo en segundos
        time.sleep(tiempo_espera)

# Cierra el navegador al finalizar
driver.quit()





