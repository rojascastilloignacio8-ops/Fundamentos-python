class Persona:
    def __init__(self, rut, edad, nombre):
        self.__rut = rut
        self.__edad = edad
        self.__nombre = nombre
    def get_rut(self):
        return self.__rut
    def get_edad(self):
        return self.__edad
    def get_nombre(self):
        return self.__nombre
    def set_edad(self, nueva_edad):
        self.__edad = nueva_edad
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
        