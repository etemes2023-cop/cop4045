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

    #Part E
    def find_string_lengths(self, string_list):
        string_lengths = {}
        for string in string_list:
            string_lengths[string] = len(string)
        return string_lengths

    #Part F
    def vowel_count(self, text):
        vowels = {}
        index = 0
        for letter in text:
            if letter.lower() == 'a' or letter.lower() == 'e' or letter.lower() == 'i' or letter.lower() == 'o' or letter.lower() == 'u':
                vowels[index] = letter
            index += 1
        return vowels
    
    def main(self):
        text = "Hello world"
        s = ["One", "Two", "Three"]
        lst1 = ["Spam", "Trams", "Elbows", "Tops", "Astral"]
        lst2 = ["Bowels", "Sample", "Altars", "Stop", "Course", "Smart"]
        names = ['Christopher Ashton Kutcher', 'Elizabeth Stamatina Fey']
        strings = ["One", "SEVEN", "Three", "Two", "Ten"]

        print(self.number_com())
        print(f"\n{self.string_valid(strings)}")
        print(f"\n{self.revised_names(names)}")
        print(f"\n{self.find_anagrams(lst1, lst2)}")
        print(f"\n{self.find_string_lengths(s)}")
        print(f"\n{self.vowel_count(text)}")

solution = Comprehension()
solution.main()