from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument('.\driver\chromedriver')
browser = webdriver.Chrome(options=chromeOptions)
def enviarMensaje():
    time.sleep(5)
    chatbox = browser.find_element(By.XPATH, "//footer//p")
   
    chatbox.send_keys('prueba')

    chatbox.send_keys(Keys.ENTER)
    print("mensaje enviado")
    time.sleep(5)
    

def validQR():
    try:
        element = browser.find_element(By.TAG_NAME,'canvas')
    except:
        return False
    return True



def seleccionChat(nombre : str):
    print("buscamos chat")
    try:
        wait = WebDriverWait(browser, 150)
        wait.until(EC.presence_of_element_located((By.ID, 'side')))
        elements = browser.find_element(By.XPATH, "//div[@class='lhggkp7q ln8gz9je rx9719la']//span[@title='" + nombre + "']")
        print("Se encontró el chat")
        elements.click()
    except:
        print("Chat no encontrado")

def enviarImagen(ruta_imagen):
    print("se entro a enviar imagen")
    # Localiza el icono de clip para adjuntar un archivo
    clip_icon = browser.find_element(By.CSS_SELECTOR,"span[data-icon='attach-menu-plus']")
    clip_icon.click()
    print("se selecciono el icono correctamente")
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-icon='attach-menu-plus']")))

    clip_icon2= browser.find_element(By.CSS_SELECTOR, "div[class='tvf2evcx m0h2a7mj lb5m6g5c j7l1k36l ktfrpxia nu7pwgvd p357zi0d dnb887gk gjuq5ydh i2cterl7 fhf7t426 sap93d0t gndfcl4n ajgl1lbb lniyxyh2 fooq7fky bcfko8ch']")
    clip_icon2.click()
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='tvf2evcx m0h2a7mj lb5m6g5c j7l1k36l ktfrpxia nu7pwgvd p357zi0d dnb887gk gjuq5ydh i2cterl7 fhf7t426 sap93d0t gndfcl4n ajgl1lbb lniyxyh2 fooq7fky bcfko8ch']")))

    print("se selecciono el icono2 correctamente")

    send_keys(ruta_imagen)

    time.sleep(1)

    clip_icon2.send_keys(Keys.ENTER)


def botWhatsapp():
    browser.get('https://web.whatsapp.com/')
    time.sleep(5)
    espera = True
    while espera :
        print("Estamos esperando")
        espera = validQR()
        time.sleep(2)
        if espera== False :
            print("QR ingresado")
            break
    time.sleep(5)
    
    numero = 'Cosas Que Vendo'

    chat = seleccionChat(numero)
    enviarMensaje()
    enviarImagen("C:/Users/USER/OneDrive/Escritorio/auto")
    
    print("fin")


botWhatsapp()
time.sleep(40)