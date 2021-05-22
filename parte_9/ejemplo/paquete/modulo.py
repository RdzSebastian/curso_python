
"""Módulo de clases"""


class Restaurante:
    """Clase la cual representa un Restaurante"""

    restaurantes = []

    def __init__(self, nombre, cuit, categoria, concepto):
        self.nombre = nombre
        self.cuit = cuit
        self.categoria = categoria
        self.concepto = concepto
        self.restaurantes.append(nombre)

    def un_cliente(self):
        self.cliente1 = Cliente(0)
        self.cliente1.factura(0)
        self.cliente1.impuesto()

    def get_categoria(self, categoria):
        return self.__categoria

    def set_categoria(self, categoria):
        self.__categoria = categoria

    def __str__(self):
        cadena = self.nombre+', número de cuit:'+self.cuit + \
            ', de categoría: '+str(self.categoria)+', tipo: ' + self.concepto
        return cadena

class Gerente:
    """Clase la cual representa el Gerente del Restaurante"""

    def __init__(self, dni, apellido):
        self.dni = dni
        self.apellido = apellido

    def marcacion(self):
        print(f"Apellido: {self.apellido}: Marca asistencia 1 vez.")

    def __str__(self):
        cadena = self.apellido+', número de dni:'+self.dni
        return cadena


class Encargado:
    """Clase la cual representa el Encargado del Restaurante"""

    def marcacion(self):
        print("Marca asistencia 2 veces.")


class Mozo:
    """Clase la cual representa el Mozo del Restaurante"""

    def marcacion(self):
        print("Marca asistencia 2 veces y firma planilla.")


def marcacionTrabajador(trabajador):
    trabajador.marcacion()


class Hotel(Restaurante, Gerente):
    """Clase la cual representa un Hotel del Restaurante"""

    def __init__(self, nombre, cuit, categoria, concepto, dni, apellido, pileta):
        # super().__init__(nombre, cuit, categoria, concepto)
        self.pileta = pileta
        Restaurante.__init__(self, nombre, cuit, categoria, concepto)
        Gerente.__init__(self, dni, apellido)

    def get_pileta(self):
        return self.pileta
    
    def __str__(self):
        cadena = 'Nombre: '+self.nombre+', Cuit: ' + self.cuit + ', Categoría: ' + \
            str(self.categoria)+', Concepto: ' + self.concepto + \
            ', Gerente:' + self.apellido + ', Pileta:' + self.pileta
        return cadena

class Cliente:
    """Clase la cual representa un Cliente del Restaurante"""

    def __init__(self, nombre):
        self.nombre = nombre
        self.monto = 0
        self.factura(self.monto)
        self.impuesto()

    def factura(self, monto):
        self.monto = self.monto + monto

    def impuesto(self):
        self.monto = self.monto + (self.monto * 0.21)
        return self.monto

    def __str__(self):
        cadena = self.nombre+', el importe a abonar es de $ ' + str(self.monto)
        return cadena
