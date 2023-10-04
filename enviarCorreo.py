from email.message import EmailMessage
import ssl
import smtplib
from persona import Persona
from base_de_datos import BaseDeDatos
from registro_persona import RegistroPersona
from datetime import datetime
import time
import random
import string
import pytz
class EnviadorDeCorreos:
    def __init__(self, email_emisor, email_contrasena):
        self.email_emisor = email_emisor
        self.email_contrasena = email_contrasena

    def enviar_correo(self, email_receptor, asunto, cuerpo):
        em = EmailMessage()
        em['From'] = self.email_emisor
        em['To'] = email_receptor
        em['Subject'] = asunto
        em.set_content(cuerpo)

        contexto = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as smtp:
            smtp.login(self.email_emisor, self.email_contrasena)
            smtp.sendmail(self.email_emisor, email_receptor, em.as_string())

    def generar_codigo_verificacion(self, longitud=6):
        """Genera un código de verificación aleatorio."""
        return ''.join(random.choice(string.digits) for _ in range(longitud))

    def verificar_correo(self, email_receptor):
        """Envía un código de verificación al correo del receptor y espera su confirmación."""
        codigo_verificacion = self.generar_codigo_verificacion()
        print(f"Enviando correo a {email_receptor} ")
        try:
            self.enviar_correo(email_receptor, "Código de verificación", f"Tu código de verificación es {codigo_verificacion}")
        except Exception as e:
            print(f"Error al enviar correo: {e}")
            return False
        codigo_usuario = input("Introduce el código de verificación que has recibido en tu correo: ")
        return codigo_verificacion == codigo_usuario

    
    def programar_correo(self):
        while True:
            now = datetime.datetime.now(pytz.timezone('America/Lima'))
            if now.hour == 22:  # Comprueba si son las 10 de la noche
                registro = RegistroPersona()
                personas = registro.obtener_personas()
                for persona in personas:
                    fecha_nacimiento = datetime.datetime.strptime(persona.fecha_nacimiento, "%d-%m-%Y")  # Asegúrate de que el formato de la fecha coincida con el de tus datos
                    if (now.day == fecha_nacimiento.day) and (now.month == fecha_nacimiento.month):  # Comprueba si hoy es el cumpleaños de la persona
                        email_receptor = persona.correo
                        asunto = "Feliz cumpleaños"
                        cuerpo = f"¡Feliz cumpleaños, {persona.nombre}!"
                        self.enviar_correo(email_receptor, asunto, cuerpo)
                        print(f"Correo enviado a {persona.nombre}")
                time.sleep(3600)  # Duerme durante una hora antes de comprobar de nuevo
            else:
                time.sleep(60)  # Duerme durante un minuto antes de comprobar de nuevo
         