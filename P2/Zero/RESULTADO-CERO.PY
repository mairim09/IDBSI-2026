"""
Fecha   : 22/04/2026
Grupo   : 2-I CSDSI
Nombre  : [AQUI PON TU NOMBRE COMPLETO]
"""

"""
Encontrar que elementos de una lista suman cero

Escribe una clase de python que encuentre 3 elementos que sumen cero
Los elementos se encuentran en una lista y son numeros enteros +-
"""

class SumaCero:
    
    def __init__(self, lista_numeros):
        self.lista = lista_numeros

    def encontrar_tríos(self):
        resultados = []
        n = len(self.lista)
        
        # Iteramos sobre todas las combinaciones posibles de 3 elementos
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if self.lista[i] + self.lista[j] + self.lista[k] == 0:
                        trio = sorted([self.lista[i], self.lista[j], self.lista[k]])
                        if trio not in resultados: # Evitamos duplicados
                            resultados.append(trio)
        return resultados

# -------------------------------------------------------------------------#
# EJECUCIÓN DEL PROGRAMA
# -------------------------------------------------------------------------#

# Ejemplo de lista con números positivos y negativos
numeros = [-1, -4, -2, 0, 1, 2, 3, 4, -3]

# Creamos el objeto
buscador = SumaCero(numeros)

# Obtenemos los resultados
triples = buscador.encontrar_tríos()

# Mostramos el resultado
print("="*50)
print("LISTA DE NÚMEROS:", numeros)
print("Tríos que suman 0:")
print("-" * 30)

if triples:
    for t in triples:
        print(f"{t[0]} + {t[1]} + {t[2]} = 0")
else:
    print("No se encontraron combinaciones que sumen cero.")

print("="*50)


"""
Resultado

==================================================
LISTA DE NÚMEROS: [-1, -4, -2, 0, 1, 2, 3, 4, -3]
Tríos que suman 0:
------------------------------
-4 + 0 + 4 = 0
-4 + 1 + 3 = 0
-3 + -1 + 4 = 0
-3 + 0 + 3 = 0
-3 + 1 + 2 = 0
-2 + -1 + 3 = 0
-2 + 0 + 2 = 0
-1 + 0 + 1 = 0
==================================================

"""