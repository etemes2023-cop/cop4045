class Comprehension:
    def __init__(self):
        pass

    #Part A
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

    #Part B
    def string_valid(self, strings):
        valid = []
        for string in strings:
            if len(string) < 5:
                valid.append((string.lower(), len(string)))
        return valid

    #Part C
    def revised_names(self, names):
        valid = []
        for name in names:
            name_parts = name.split()
            name_parts[1] = name_parts[1][0] + "."
            valid.append(" ".join(name_parts))
        return valid

    #Part D
    def find_anagrams(self, lst1, lst2):
        anagrams = []
        for word in lst1:
            for list in lst2:
                if sorted(word.lower()) == sorted(list.lower()):
                    anagrams.append((word, list))
        return anagrams
    
    def main(self):
        lst1 = ["Spam", "Trams", "Elbows", "Tops", "Astral"]
        lst2 = ["Bowels", "Sample", "Altars", "Stop", "Course", "Smart"]
        #names = ['Christopher Ashton Kutcher', 'Elizabeth Stamatina Fey']
        #strings = ["One", "SEVEN", "Three", "Two", "Ten"]
        print(self.find_anagrams(lst1, lst2))

solution = Comprehension()
solution.main()
