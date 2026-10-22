from inventario import Inventario


class Personaje:

    def __init__(self, nombre, nivel, vida):

        self.nombre = nombre
        self.nivel = nivel
        self.vida = vida

        self.inventario = Inventario()

    def atacar(self):
        print(f"{self.nombre} realiza un ataque.")


    def recibir_danio(self, danio):

        self.vida -= danio

        if self.vida < 0:
            self.vida = 0

        print(f"{self.nombre} recibio {danio} puntos de daño")
        print(f"Vida actual:{self.vida}")

    def usar_habilidad(self):
        print(f"{self.nombre} utiliza una habilidad")

    def mostrar_informacion(self):

        print("\n ---Informacion del Personaje --- ")
        print(f"Nombre: {self.nombre}")
        print(f"Vida: {self.vida}")
        print(f"Nivel: {self.nivel}")

 
    