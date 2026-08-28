import matplotlib.pyplot as plt
import math

class QuadraticFormula:
    def __init__(self):
        pass

    def main(self):
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))
        self.findQuadraticSolutions(a, b, c)
        self.graphEquation(a, b, c)

    def findQuadraticSolutions(self, a, b, c):
        while True:
            if a == "":
                break
            else:
                if b == "":
                    break
                else:
                    if c == "":
                        break
                    else:
                        discriminant = b**2-4*a*c
                        if discriminant < 0:
                            print("\nNo real solutions.")
                            break
                        elif discriminant == 0:
                            x1 = (-b + math.sqrt(discriminant)) / (2*a)
                            print(f"\nOne real solution: x1={x1}")
                            break
                        else:
                            x1 = (-b + math.sqrt(discriminant)) / (2*a)
                            x2 = (-b - math.sqrt(discriminant)) / (2*a)
                            print(f"\nTwo real solutions: x1={x1}, x2={x2}")
                            break

    def graphEquation(self, a, b, c):
        xmin = float(input("Enter minimum x: "))
        xmax = float(input("Enter maximum x: "))
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