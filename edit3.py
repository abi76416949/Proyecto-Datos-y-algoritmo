from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

#whitout options
#driver = webdriver.Chrome()

options = Options()
numero_telefono = "917628284"
options = webdriver.ChromeOptions()
#options.add_argument("--user-data-dir=./driver/data3")
options.add_argument("--user-data-dir=C:\\Users\\USER\\AppData\\Local\\Google\\Chrome SxS\\User Data")
options.add_argument("--profile-directory=Default")
driver = webdriver.Chrome(options=options) 

def enviarImagen(ruta_imagen):
    print("se entro a enviar imagen")
    # Localiza el icono de clip para adjuntar un archivo
    clip_icon = driver.find_element(By.CSS_SELECTOR,"span[data-icon='attach-menu-plus']")
    clip_icon.click()
    print("se selecciono el icono correctamente")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-icon='attach-menu-plus']")))

    clip_icon2= driver.find_element(By.CSS_SELECTOR, "div[class='tvf2evcx m0h2a7mj lb5m6g5c j7l1k36l ktfrpxia nu7pwgvd p357zi0d dnb887gk gjuq5ydh i2cterl7 fhf7t426 sap93d0t gndfcl4n ajgl1lbb lniyxyh2 fooq7fky bcfko8ch']").send_keys(ruta_imagen)
    clip_icon2.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='tvf2evcx m0h2a7mj lb5m6g5c j7l1k36l ktfrpxia nu7pwgvd p357zi0d dnb887gk gjuq5ydh i2cterl7 fhf7t426 sap93d0t gndfcl4n ajgl1lbb lniyxyh2 fooq7fky bcfko8ch']")))

    print("se selecciono el icono2 correctamente")

  

    time.sleep(1)

    clip_icon2.send_keys(Keys.ENTER)


time.sleep(1)
driver.get(f"https://web.whatsapp.com/send?phone={numero_telefono}")
time.sleep(1)


wait = WebDriverWait(driver, 150)
wait.until(EC.presence_of_element_located((By.TAG_NAME, 'footer')))


mensaje = " "

#get in footer

test = driver.find_element(By.TAG_NAME, 'footer')
#get in p in footer
message_box = test.find_element(By.TAG_NAME, 'p')
message_box.click()
message_box.send_keys(mensaje)
time.sleep(2)
message_box.send_keys(Keys.ENTER)
time.sleep(5)

print(f"Mensaje enviado a {numero_telefono}: {mensaje}")

enviarImagen("G:\portadas\IMAGEN PORTADA.png")