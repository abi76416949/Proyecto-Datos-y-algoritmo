import pywhatkit as kit

# Número de teléfono del destinatario (debe incluir el código de país sin el signo +)
numero_telefono = "+51997322971"

# Ruta completa de la imagen que deseas enviar
ruta_de_imagen = "./gato.png"  # Reemplaza con la ruta de tu imagen

# Mensaje opcional
mensaje = "¡Aquí tienes una imagen!"

# Enviar la imagen a través de WhatsApp
kit.send_img(phone_num=numero_telefono, img_path=ruta_de_imagen, caption=mensaje)

# Asegúrate de tener WhatsApp Web abierto en tu navegador y escaneado el código QR previamente
