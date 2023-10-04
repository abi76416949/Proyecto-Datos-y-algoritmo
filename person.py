import datetime

class Persona:
    def __init__(self, nombre, codigo, edad, correo, numero, genero, fecha_nacimiento):
        self.nombre = nombre
        self.codigo = codigo
        self.edad = edad
        self.numero = numero
        self.genero = genero
        self.fecha_nacimiento = fecha_nacimiento
        self.correo = correo

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_codigo(self):
        return self.codigo

    def set_codigo(self, codigo):
        self.codigo = codigo

    def get_edad(self):
        return self.edad

    def set_edad(self, edad):
        self.edad = edad

    def get_numero(self):
        return self.numero

    def set_numero(self, numero):
        self.numero = numero

    def get_genero(self):
        return self.genero

    def set_genero(self, genero):
        self.genero = genero

    def get_fecha_nacimiento(self):
        return self.fecha_nacimiento

    def set_fecha_nacimiento(self, fecha_nacimiento):
        if self.validar_fecha_nacimiento(fecha_nacimiento):
            self.fecha_nacimiento = fecha_nacimiento
        else:
            raise ValueError("Fecha de nacimiento no válida")

    def get_correo(self):
        return self.correo

    def set_correo(self, correo):
        self.correo = correo

    @staticmethod
    def validar_fecha_nacimiento(fecha_nacimiento):
        try:
            dia, mes, anio = map(int, fecha_nacimiento.split('/')) # Asumiendo que la fecha está en formato dd/mm/yyyy
            datetime.datetime(anio, mes, dia) # Esto lanzará un error si la fecha es inválida
            return True
        except ValueError:
            return False
