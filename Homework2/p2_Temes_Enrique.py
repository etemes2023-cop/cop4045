class Comprehension:
    def __init__(self):
        pass

    def number_com(self):
        valid = []
        for a in range(1, 11):
            for b in range(1, 11):
                for c in range(1, 11):
                    for d in range(1, 11):
                        numbers = (a, b, c, d)
                        s = a**2 + b**2
                        t = c**2 + d**2
                        if s == t:
                            valid.append(numbers)
        return valid
    
    def main(self):
        print(self.number_com())

solution = Comprehension()
solution.main()
