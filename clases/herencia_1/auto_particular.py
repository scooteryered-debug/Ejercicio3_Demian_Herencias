from clases.herencia_2.persona import Persona

class AutoParticular(Persona):
    def __init__(self, clave, nombre, edad, marca, color, placa):
        super().__init__(clave, nombre, edad)
        self.marca = marca
        self.color = color
        self.placa = placa
        
    def __str__(self):
        return super().__str__() + " " + self.marca + " " + self.color + " " + self.placa
        
    def SubirseAuto(self):
        print("Subiendo al auto...")
    def EncenderAuto(self):
        print("Encendiendo el radio...")
        print("Arrancando el auto...")
    def LlegarDestino(self):
        print("Llegando al destino...")
    def BajarseAuto(self):
        print("Bajando del auto...")
    
    