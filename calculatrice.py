# calculatrice.py

class Calculatrice:
    def addition(self, a, b):
        return a + b

    def soustraction(self, a, b):
        return a - b

    def division(self, a, b):
        if b == 0:
            raise ValueError("La division par zéro n'est pas autorisée.")
        return a / b
