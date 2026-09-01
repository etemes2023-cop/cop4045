class DetermineSubstrings:
    def __init__(self):
        pass

    def main(self):
        s = input("Enter string: ")
        n = int(input("Enter length of substring: "))
        dup = self.find_dup_str(s, n)
        lon = self.find_max_dup(s)
        print(dup)
        print(lon)

    def find_dup_str(self, s, n):
        substrings = []
        for i in range(0, (len(s)-n)+1):
            start = i
            end = n+i
            substring = s[start:end]
            substrings.append(substring)

        for i in range(0, len(substrings)):
            for j in range(i+1, len(substrings)):
                if (substrings[i] == substrings[j]):
                    return substrings[i]

        return ""

    def find_max_dup(self, s):
        n = len(s)
        for i in range(n, 0, -1):
            if (self.find_dup_str(s, i) == ""):
                continue
            else:
                return self.find_dup_str(s,i)
        return ""
            
solution = DetermineSubstrings()
solution.main()