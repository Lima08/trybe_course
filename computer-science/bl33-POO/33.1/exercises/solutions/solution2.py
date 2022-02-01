class quadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcula_area(self):
        return self.lado * self.lado

    def calcula_perimetro(self):
        return 4 * self.lado
