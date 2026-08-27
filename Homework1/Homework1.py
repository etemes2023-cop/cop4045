import matplotlib.pyplot
import math

class QuadraticFormula:
    def __init__(self):
        pass

    def main(self):
        a = input("Enter a: ")
        b = input("Enter b: ")
        c = input("Enter c: ")
        self.findQuadraticSolutions(a, b, c)

    def findQuadraticSolutions(self, a, b, c):
        while True:
            a = float(a)
            if a == "":
                break
            else:
                b = float(b)
                if b == "":
                    break
                else:
                    c = float(c)
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

    # def graphEquation(self, a, b, c):
    #     xmin = input("Enter minimum x: ")
    #     xmax = input("Enter maximum x: ")
    #     y = a*x**2 + b*x + c
    #     graph = matplotlib.pyplot.plot(x,y)
solution = QuadraticFormula()
solution.main()
print(solution)