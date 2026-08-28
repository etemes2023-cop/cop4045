import matplotlib.pyplot as plt
import math

class QuadraticFormula:
    def __init__(self):
        pass

    def main(self):
        while True:
            a = (input("Enter a: "))
            b = (input("Enter b: "))
            c = (input("Enter c: "))
            if a == "":
                break
            if b == "":
                break
            if c == "":
                break
            a = float(a)
            b = float(b)
            c = float(c)
            xmin, xmax = self.findQuadraticSolutions(a, b, c)
            self.graphEquation(a, b, c, xmin, xmax)

    def findQuadraticSolutions(self, a, b, c):
        discriminant = b**2-4*a*c
        xmin = 0
        xmax = 0
        if discriminant < 0:
            print("\nNo real solutions.")
            xmin = (-b / (2*a)) - 10
            xmax = (-b / (2*a)) + 10
        elif discriminant == 0:
            x1 = (-b + math.sqrt(discriminant)) / (2*a)
            xmin = x1 - 10
            xmax = x1 + 10
            print(f"\nOne real solution: x1={x1}")
        else:
            x1 = (-b + math.sqrt(discriminant)) / (2*a)
            x2 = (-b - math.sqrt(discriminant)) / (2*a)
            xmin = min(x1, x2) - 10
            xmax = max(x1, x2) + 10
            print(f"\nTwo real solutions: x1={x1}, x2={x2}")
        return xmin, xmax

    def graphEquation(self, a, b, c, xmin, xmax):
        x = []
        y = []
        interval = (xmax-xmin) / 149
        for i in range(150):
            x_i = xmin + i * interval
            y_i = a*x_i**2 + b*x_i + c
            x.append(x_i)
            y.append(y_i)
        plt.plot(x,y)
        plt.show()

solution = QuadraticFormula()
solution.main()
print(solution)