from clases.herencia_1.taxi import Taxi
from clases.herencia_1.auto_particular import AutoParticular

def main(): 
    coche = Taxi("123-GTO","Versa",1000,"123-a")
    
    print("****************")
    print(coche) 
    coche.encender() 
    coche.subirPasajeros() 
    coche.acelerar() 
    coche.frenar() 
    coche.cobrarCuota() 
    
    ap = AutoParticular("123", "Demian", 15, "Volvo", "Plata", "987-G")
    print(ap)
    ap.SubirseAuto()
    ap.EncenderAuto()
    ap.LlegarDestino()
    ap.BajarseAuto()

if __name__ == '__main__': 
    main()