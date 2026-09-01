import matplotlib.pyplot as plt
import math

class CreateFunctionGraphs:
    def __init__(self):
        pass

    def main(self):
        fun_str = input("Enter function with variable x: ")
        xmin = int(input("Enter minimum x-value: "))
        xmax = int(input("Enter maximum x-value: "))
        domain = (xmin, xmax)
        ns = int(input("Enter number of sample points: "))
        graph = self.plot_function(fun_str, domain, ns)
        print(graph)
        return 0

    def plot_function(self, fun_str, domain, ns):
        xs = []
        ys = []
        xmin = domain[0]
        xmax = domain[1]
        interval = (xmax-xmin) / (ns-1)
        for i in range(0, ns-1):
           x = xmin + i*interval
           xs.append(x)

        for x in xs:
            y = eval(fun_str)
            ys.append(y)

        print(f"{'x':>10} {'y':>10}")
        for i in range(0, ns-1):
            print(f"{xs[i]:>10.2f} {ys[i]:>10.2f}")

        plt.title("Function Graph")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.plot(xs, ys)
        plt.show()

solution = CreateFunctionGraphs()
solution.main()
print(solution)