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

if __name__ == "__main__":
    calc = Calculatrice()

    # Test des opérations
    print("Addition de 5 et 3:", calc.addition(5, 3))
    print("Soustraction de 5 par 3:", calc.soustraction(5, 3))
    print("Division de 10 par 2:", calc.division(10, 2))
