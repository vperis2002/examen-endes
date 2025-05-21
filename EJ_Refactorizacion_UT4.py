from abc import ABC, abstractmethod

# Clase abstracta para representar una receta
class Receta(ABC):
    def __init__(self, nombre, ingredientes, pasos):
        self.nombre = nombre  # nombre
        self.ingredientes = ingredientes  # ingredientes
        self.pasos = pasos  # pasos
    
    @abstractmethod
    def mostrar(self):
        print("Ingredientes:")
        for ingrediente in self.ingredientes:
            print(f"- {ingrediente}")
        print("Pasos:")
        for paso in self.pasos:
            print(f"{paso}")
        pass


# Clase para recetas vegetarianas
class RecetasVegetarianas(Receta):
    def mostrar(self):
        print(f"Receta vegetariana: {self.nombre}")
        Receta.mostrar(self)


# Clase para recetas no vegetarianas
class RecetasNoVegetarianas(Receta):
    def mostrar(self):
        print(f"Receta NO vegetariana: {self.nombre}")
        Receta.mostrar(self)



# Clase con utilidades del restaurante
class Utilidades:
    lista_recetas = []
    def crear_receta():
        cantidad_recetas = int(input("Dime la cantidad de recetas que quieres añadir: "))
        contador_recetas = 0
        
        while contador_recetas < cantidad_recetas:
            lista_ingredientes = []
            lista_pasos = []
            tipo_receta = input("Si es una receta vegetariana escribe v, si no es vegetariana escribe nv: ")
            nombre = input("Dime el nombre de la receta: ")
            cantidad_ingredientes = int(input("Dime cuantos ingredientes quieres meter: "))
            contador_ingredientes = 0
            while contador_ingredientes <  cantidad_ingredientes:
                ingrediente = input("Dime el ingrediente: ")
                lista_ingredientes.append(ingrediente)
                contador_ingredientes += 1
            cantidad_pasos = int(input("Dime la cantidad de pasos que tiene: "))
            contador_pasos = 0
            while contador_pasos < cantidad_pasos:
                paso = input("Dime el paso: ")
                lista_pasos.append(paso)
                contador_pasos += 1
            contador_recetas += 1
            if tipo_receta == "v":
                receta = RecetasVegetarianas(nombre, lista_ingredientes, lista_pasos)
            elif tipo_receta == "nv":
                receta = RecetasVegetarianas(nombre, lista_ingredientes, lista_pasos)
            else:
                print("No válido")
            Utilidades.lista_recetas.append(receta)

    @staticmethod
    def imprimir_receta(receta):
        print("====================================")
        receta.mostrar()
        print("====================================")

    @staticmethod
    def mostrar_lista_ingredientes(lista):
        for ingrediente in lista:
            print(f"* {ingrediente}")

# Función principal
def principal():
    Utilidades.crear_receta()
    print("MOSTRAR RECETAS")
    for receta in Utilidades.lista_recetas:
        Utilidades.imprimir_receta(receta)


# Ejecutar el programa
if __name__ == "__main__":
    principal()

