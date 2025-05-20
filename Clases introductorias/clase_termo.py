class Termo:
    def __init__(self, color, material, capacidad):
        self.color = color
        self.material = material
        self.capacidad = capacidad
        self.nivel = 0

    def __str__(self):
        return f"El termo es de color {self.color}, de {self.material}\ncapacidad: {self.capacidad} cm3   nivel actual: {self.nivel} cm3.\n"

    def rellenar(self):
        self.nivel = self.capacidad

    def cebar(self, agua_a_cebar):
        if self.nivel == 0:
            print("el termo está vacío!")
        elif agua_a_cebar <= self.nivel:
            self.nivel = self.nivel - agua_a_cebar
        else:
            print(f"no alcancé a cebar lo requerido, solo me dió para cebar {self.nivel}cm3")
            self.nivel = 0

    def nivel(self):
        return self.nivel

    def retorna_color(self):
        return self.color

