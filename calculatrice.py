# calculatrice.py

class Calculatrice:
    def division(self, a, b):
        if b == 0:
            raise ValueError("La division par zéro n'est pas autorisée.")
        return a / b
