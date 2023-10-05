from base_de_datos import BaseDeDatos
from whasapp import Automatizacion  # Importa la clase Automatizacion
import time
import datetime
from enviarCorreo import EnviadorDeCorreos
from base_de_datos import BaseDeDatos
from datetime import datetime


class EnviadorDeWhatsApp:
    def __init__(self, archivo_db):
        self.db = BaseDeDatos(archivo_db)
        self.automatizacion = Automatizacion()  # Crea una instancia de Automatizacion

    def enviar_felicitacion_whatsapp(self, phone , nombre):
        # Obtener los datos de los destinatarios
        recipients = self.db.obtener_datos()


        # Enviar mensajes a cada destinatario
        for recipient in recipients:
            phone = recipient['numero']
            nombre = recipient['nombre']
            ruta = r"G:\Proyecto final\Proyecto-Datos-y-algoritmo\images\logo.png"
            self.automatizacion.bot_whatsapp(phone, ruta, nombre)  # Llama al método de Automatizacion
            time.sleep(3)
            print("saliendo del bucle")


    def enviar_felicitaciones_cumpleaños(self):
        ahora = datetime.now()
        db = BaseDeDatos("G:\\Proyecto final\\Proyecto-Datos-y-algoritmo\\intefaz\\personas.xlsx")

        recipients = db.obtener_datos()

        for recipient in recipients:
            genero_recipient = recipient['genero']
            nombre_recipient = recipient['nombre']
            fecha_nacimiento = datetime.strptime(recipient['fecha_nacimiento'], '%d/%m/%Y')

            if fecha_nacimiento.month == ahora.month and fecha_nacimiento.day == ahora.day:
                # Verificar si es el cumpleaños y definir el mensaje
                if genero_recipient == 'F':
                    mensaje = "¡Feliz cumpleaños, {nombre}! 🎉 (Mensaje para mujeres)"
                elif genero_recipient == 'M':
                    mensaje = "¡Feliz cumpleaños, {nombre}! 🎉 (Mensaje para hombres)"
                else:
                    print(f"No se reconoce el género para {nombre_recipient}")

                numero_telefono = recipient['numero']
                mensaje_personalizado = mensaje.format(nombre=nombre_recipient)
                print(f"Mensaje de cumpleaños preparado para {nombre_recipient}")

        # Llama al método una sola vez después de preparar todos los mensajes
        self.enviar_felicitacion_whatsapp(numero_telefono, mensaje_personalizado)

        print("Saliendo del bucle")






def enviadorCorreos():
    # Definir asunto y cuerpo del correo
    
    
    
    # Crear instancia de EnviadorDeCorreos
    enviador_de_correos = EnviadorDeCorreos('trabajosgrupalesdelcole@gmail.com', 'dysa uxym osmb wuci')
    db = BaseDeDatos("G:\Proyecto final\Proyecto-Datos-y-algoritmo\intefaz\personas.xlsx")
    asunto = "Asunto del correo"
    cuerpo = enviador_de_correos.mensaje_personalisado()
    recipients= db.obtener_datos()

    # Enviar mensajes a cada destinatario
    """ for recipient in recipients:
        email_receptor = recipient['correo']
        ruta = "G:\Proyecto final\Proyecto-Datos-y-algoritmo\images\logo.png"
        try:
            # Enviar correo
            enviador_de_correos.enviar_correo(email_receptor, asunto, cuerpo)
            print(f"Correo enviado a {email_receptor}")
        except Exception as e:
            print(f"Error al enviar correo a {email_receptor}: {str(e)}") 
        time.sleep(3)
        print("saliendo del bucle") """
        
    # Crear instancia de RegistroPersona para obtener los correos electrónicos
    #rp = RegistroPersona()
    
    # Obtener la lista de correos electrónicos
    #email_receptores = rp.extraer_emails()
    
    # Iterar a través de la lista de correos electrónicos y enviar correos a cada destinatario
"""    for email_receptor in email_receptores:
        try:
            # Enviar correo
            enviador_de_correos.enviar_correo(email_receptor, asunto, cuerpo)
            print(f"Correo enviado a {email_receptor}")
        except Exception as e:
            print(f"Error al enviar correo a {email_receptor}: {str(e)}") """





# Llamar a la función para enviar correos
#enviadorCorreos()

# Crear una instancia de la clase WhatsAppBot
archivo = "G:\Proyecto final\Proyecto-Datos-y-algoritmo\intefaz\personas.xlsx"
bot = EnviadorDeWhatsApp(archivo)
bot.enviar_felicitaciones_cumpleaños()
# Enviar mensajes a los destinatarios
#bot.enviar_mensajes()
