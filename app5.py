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
numero_telefono = "51997322971"
options = webdriver.ChromeOptions()
#options.add_argument(r"--user-data-dir=C:\Users\USER\AppData\Local\Google\Chrome\User Data")
#options.add_argument("--profile-directory=Default")
driver = webdriver.Chrome(options=options)


time.sleep(1)
driver.get(f"https://web.whatsapp.com/send?phone={numero_telefono}")
time.sleep(1)


wait = WebDriverWait(driver, 150)
wait.until(EC.presence_of_element_located((By.TAG_NAME, 'footer')))


mensaje = "Automatico"

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
