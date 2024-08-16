# Ejemplo # 2.5
class SuperficieRectangular:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def calcular_superficie(self):
        return self.ancho * self.alto

ancho_superficie = float(input("Especifica la medida del ancho del terreno (en unidades): "))
alto_superficie = float(input("Especifica la medida del alto del terreno (en unidades): "))

terreno = SuperficieRectangular(ancho_superficie, alto_superficie)
superficie = terreno.calcular_superficie()
print(f"La superficie del terreno es: {superficie} unidades cuadradas.")


# Ejemplo # 2.7
class Ganadero:
    def __init__(self, volumen_litros):
        self.volumen_litros = volumen_litros
        
    def a_galones(self):
        return self.volumen_litros / 3.785
    
    def mostrar_volumen_galones(self):
        galones = self.a_galones()
        print(f"El ganadero produce {galones:.2f} galones de leche")


# Ejemplo # 2.9 
class Obrero:
    def __init__(self, horas_laborales, tarifa_hora):
        self.horas_laborales = horas_laborales
        self.tarifa_hora = tarifa_hora
        
    def calcular_pago_semanal(self):
        return self.horas_laborales * self.tarifa_hora
horas_trabajadas = float(input("Ingresa la cantidad de horas trabajadas: "))
tarifa_hora = float(input("Ingresa la tarifa por cada hora: "))

obrero = Obrero(horas_trabajadas, tarifa_hora)

pago_semanal = obrero.calcular_pago_semanal()
print(f"El salario semanal del obrero es: {pago_semanal}.")