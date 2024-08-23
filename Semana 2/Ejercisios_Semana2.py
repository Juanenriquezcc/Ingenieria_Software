## Ejercicio 2.10
class Costurera:
    def __init__(self, metros_tela):
        self.metros_tela = metros_tela
        
        # constantes
        self.PULGADA_EN_METRO = 0.0254
        self.METRO_EN_PULGADA = 39.37
        
    def calcular_pulgadas_requeridas(self):
        return self.metros_tela / self.PULGADA_EN_METRO

    # método para convertir pulgadas a metros    
    def convertir_pulgadas_a_metros(self, pulgadas):
        return pulgadas / self.METRO_EN_PULGADA
    
# Pruebas
costurera = Costurera(45)
print(costurera.calcular_pulgadas_requeridas())
print(costurera.convertir_pulgadas_a_metros(1771.6535433070867))

## Ejercicio 2.11
PRECIO_POR_METRO_CUBICO = 5600

def calcular_precio_volumen(ancho, largo, profundidad):
    if any(dim <= 0 for dim in [ancho, largo, profundidad]):
        raise ValueError("Las dimensiones deben ser mayores a cero.")
        
    volumen = ancho * largo * profundidad
    return volumen * PRECIO_POR_METRO_CUBICO

print(calcular_precio_volumen(4, 7, 2))

## Ejercicio 3.1
def obtener_mayor_valor(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    return "Ambos valores son iguales"

print(obtener_mayor_valor(5, 6))
print(obtener_mayor_valor(7, 6))
print(obtener_mayor_valor(5, 5))