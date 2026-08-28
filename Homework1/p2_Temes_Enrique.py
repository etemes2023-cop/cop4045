class PythagoreanNumbers:
    def __init__(self):
        pass

    def main(self):
        n = int(input("Enter n: "))
        while n < 0:
            print("\nInvalid number.")
            n = int(input("Enter n: "))
        triples = self.find_pythagorean(n)
        print(triples)
    
    def find_pythagorean(self, n):
        triples = []
        for a in range(1, n+1):
            for b in range(1, n+1):
                for c in range(1, n+1):
                    if (a**2 + b**2 == c**2):
                        triples.append((a,b,c))

        return triples

solution = PythagoreanNumbers()
solution.main()