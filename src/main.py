import sys
sys.path.append('.\src\modules')
from modules.registro_persona import RegistroPersona
from modules.persona import Persona
from modules.base_de_datos import BaseDeDatos
from modules.enviarCorreo import EnviadorDeCorreos

def main():
    registro = RegistroPersona()
    enviador_de_correos = EnviadorDeCorreos('trabajosgrupalesdelcole@gmail.com', 'eqnclstodvineoub')

    # Menu principal
    while True:
        print("\nMenú:")
        print("1. Agregar persona")
        print("2. Eliminar persona")
        print("3. Mostrar personas")
        print("4. Buscar persona")
        print("5. Salir")

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

        else:
            print("Opción no válida. Por favor, elija una opción válida.")

if __name__ == "__main__":
    main()
