from registro_persona import RegistroPersona
from persona import Persona
<<<<<<< HEAD
import sys

def Agregar_persona(registro):
    nombre = input("Nombre y apellido: ")
    edad = int(input("Edad: "))
    codigo = input("Código: ")
    correo = input("Correo electrónico (sin @gmail.com): ")
    correo = correo + "@gmail.com"
    numero = input("Número de teléfono: ")
    genero = input("Género (F/M): ")
    fecha_nacimiento = input("Fecha de nacimiento (dd/mm/aaaa): ")

    persona = Persona(nombre, codigo, edad, correo, numero, genero, fecha_nacimiento)
    registro.agregar_persona(persona)

def Eliminar_persona(registro):
    codigo = input("Ingrese el codigo de la persona a eliminar: ")
    registro.eliminar_persona(codigo)

def Mostrar_personas(registro):
    registro.mostrar_personas()

def Buscar_persona(registro):
    codigo = input("Ingrese el codigo de la persona a buscar: ")
    registro.buscar_persona(codigo)

def exit_program():
    print("Saliendo del programa...")
    sys.exit(0)

# Diccionario
opciones = {
    "1": Agregar_persona,
    "2": Eliminar_persona,
    "3": Mostrar_personas,
    "4": Buscar_persona,
    "0": exit_program
}
=======
from base_de_datos import BaseDeDatos
from enviar import EnviadorDeCorreos
>>>>>>> tevis

def main():
    registro = RegistroPersona()
    enviador_de_correos = EnviadorDeCorreos('trabajosgrupalesdelcole@gmail.com', 'eqnclstodvineoub')

    while True:
        print("MENU DE OPCIONES")
        print("1. Agregar persona")
        print("2. Eliminar persona")
        print("3. Mostrar personas")
        print("4. Buscar persona")
        print("0. Salir")

<<<<<<< HEAD
        seleccion = input("Seleccione una opción: ")
=======
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            # Solicitar datos al usuario
            nombre = input("Nombre y apellido: ")
            edad = int(input("Edad: "))
            codigo = input("Codigo: ")
            correo = input("Correo electrónico (sin @gmail.com): ")
            
            op_correo = input("que tipo de correo usa? (1)gmail (2)hotmail (3)yahoo: ")
            if op_correo == "1":
                correo = correo + "@gmail.com"
            if op_correo == "2":
                correo = correo + "@hotmail.com"
            if op_correo == "3":
                correo = correo + "@yahoo.com" 
            numero = input("Número de teléfono: ")
            genero = input("Genero(F/M): ")
            fecha_nacimiento = input("Fecha de nacimiento(dd/mm/aaaa): ")

            # Crear objeto Persona
            persona = Persona(nombre, codigo, edad, correo, numero, genero, fecha_nacimiento)

            # Agregar persona al registro
            registro.agregar_persona(persona)

            # Enviar correo electrónico a la persona recién registrada
            enviador_de_correos.enviar_correo(correo, "Registro exitoso", "Has sido registrado exitosamente.")

        elif opcion == "2":
            codigo = input("Ingrese el codigo de la persona a eliminar: ")
            registro.eliminar_persona(codigo)

        elif opcion == "3":
            registro.mostrar_personas()

        elif opcion == "4":
            codigo = input("Ingrese el codigo de la persona a buscar: ")
            registro.buscar_persona_por_codigo(codigo)

        elif opcion == "5":
            print("Saliendo del programa...")
            break
>>>>>>> tevis

        if seleccion in opciones:
            opciones[seleccion](registro)
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()

