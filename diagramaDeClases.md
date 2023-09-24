# Diagrama de clases Felicitaciones


https://mermaid.live/edit#pako:eNqNVu9u2zYQfxVCQAF7kQ07ie1GHwa0dbYvWxq0HwpsHgxKOjssJFIlqbSp4YfZM-wR-mI9_pFMK7Izw7Ap3f1-d7w73nEXZSKHKImygiq1ZHQrabniBD9caCAbIcmnB6rVm6p6KzRZReRWaUqMOpBas4J9p4SSFWJorWlJNb7ImODkiaRGJ8cv1UKRTJSCMI5onjG6igIryPoHJRIKRP74jxsMaldCMfcMitTc2sgEz6DSwqgUlFRSGIc9TEgGXNPcOCTSz2CsDu7fvx8a5Jfa-KIyyVJ0nIfmECTBbUnhgyE22mjSsRhjBuE2jS5otAPWH4G-6R__WndrXApSYcQa44gTWlLlucfklvsXFS1oiovYshws2W0jd8OL8S9p7lm1RE7PPSbdCI7JYDTEiLBHAzC048HF8L5OC5aJRjnM5Wj0K3mLfi1haROUNPl0qvcglcBdj0a_kA-wZQrNN--SNgpO95Y_MrQql_BOSAlI9gJ5l_AF9a7bb2otglIL3TEAB7IlHbLu3HtCRuSjloxvCZXZA3sUDuU-FyFi4BUSDxiGehlISeVgmJBHwfJQIlKNvsi1LXyjQPlTKN_WVOa0kdtfq_OM6tUr85oER62ikvoDtSngG0sLrCsH2IfbfpaR55uHkrJiDSVTQp4QmrBilQKnjcKF9RBPCdJLlBvugYJiEzuEBGXOp4ypqrkWcVaDrMSwA7_35_aIYdikYd8s3FZ8jewOYWm95KJMJfQIsKuxrQgFjGsCOc1Jr7Zxok_C6xKk6BFsTYL7BBvIHuiaY2GWphuJo7yDvrMem5pw-qFYtWK3r7bqnlcYMr2zWzzJ5MUuEOeZbjEshgdD1CGxEhM1Kzzlh83gaT-s2IX4vB93NtinY-PELiXnmX632TnJ5MUuh-eZfjPpvGuzeZKyq7c5fu410qnzTk88qvcUMxD0pVBUOXXsIB749z_H_azDOzhqYjjwYYvn0LMM_H9L1hMVKHBTPMC8WGOlQPsHgOrrmWmtsoPKGgfeOvufJdwD5WfOEelpl-GA2TXhG5E87Qn7yNx0gvGTdMZRA79oumQJXNHPEGzbKZhf64XzoTPUdq0TONJBJuQTpEu7PBg4hjSZbQ2zkmKNDyRezPy6N4rYlGnBzED6YsdZKkQB9MQu_PlbayhgI3ibl5icaVqYI6HXX02QaVV1jnBMehw8Q7dvc28CEcURkuHsyfEWa2O2ivQDlLCKElzmsKF1oc39Z4-qJnMfn3gWJRtaKIijusJhCv7i276tKI-SXfQtSqaXs_Hs9eJycXU9nU9vFtNZHD1FyeVkNr6ZTCbX06vXi-l8Pp_t4-i7EEgxGS9urq8u59PL-Wwxu17EEeQMJ-Kf_qJt_qyFv6y6ljXsfwLUM7zb




```mermaid
classDiagram
    note for WhatsAppBot " Esta clase utiliza a \n autamatizacion y base de datos como instancia"
    note " La relación de composición es un \n concepto de la programación orientada a objetos (POO)\n que describe una relación entre clases en la que un objeto de una clase contiene \n o está compuesto por objetos de otras clases. En otras palabras, \n un objeto compone o está formado por otros objetos. "
    note " . (-) privado \n .(+)Publico"
    WhatsAppBot --> BaseDeDatos : utiliza
    Persona --* RegistroPersona : contiene
    EnviadorDeCorreos --> BaseDeDatos : utiliza
    RegistroPersona --> BaseDeDatos : utiliza
    WhatsAppBot --> Automatizacion : contiene

  
    class BaseDeDatos{
      - String archivo

        + BaseDeDatos(archivo: String)
        + cerrar(): void
        + obtener_datos(): any
        + guardar_datos(datos: any): void
        %% any se utiliza para datos flexibles.
    }
    class EnviadorDeCorreos{
      - String email_emisor
      - String email_contrasena
      + void enviar_correo(self,email_reseptor,asunto,cuerpo)
      + void Programar_correo(self)

    }

    class Persona{
        - String nombre
        - String codigo
        - int edad 
        - String correo 
        - String numero
        - String genero
        - String fecha_nacimiento
        + getNombre(): String
        + setNombre(nombre: String): void
        + getCodigo(): String
        + setCodigo(codigo: String): void
        + getEdad(): int
        + setEdad(edad: int): void
        + getCorreo(): String
        + setCorreo(correo: String): void
        + getNumero(): String
        + setNumero(numero: String): void
        + getGenero(): String
        + setGenero(genero: String): void
        + getFechaNacimiento(): String
        + setFechaNacimiento(fechaNacimiento: String): void
    }

    class RegistroPersona{
        - bd: BaseDeDatos
        - personas: Persona[]

        + RegistroPersona()
        + agregar_persona(persona: Persona): void
        + eliminar_persona(codigo: String): void
        + mostrar_personas(): void
        + buscar_persona_por_codigo(codigo: String): void
        + buscar_persona_por_nombre(nombre: String): void 
    }
    class WhatsAppBot {

    - db: BaseDeDatos
    - automatizacion: Automatizacion

    + enviar_mensajes(): void

    
  }
  class Automatizacion {
    - driver: WebDriver

    + Automatizacion()
    + enviar_imagen(ruta_imagen: String): void
    + validar_qr(): boolean
    + enviar_mensaje(numero_telefono: String, nombre: String): void
    + bot_whatsapp(numero: String, ruta_imagen: String, nombre: String): void
  }
       
    
```
