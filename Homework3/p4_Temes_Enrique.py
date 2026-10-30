class TextEditor:
    def __init__(self):
        pass

    def ed_read(self, filename: str, from_:int=0, to:int=-1)->str:
        """Returns portion of file content based on the value of the parameter to."""
        with open(file=filename, encoding="utf-8") as temp_file:
            content = temp_file.read()
            len_content = len(content)
            if (len_content < to and to != -1) or from_ < 0 or from_ > len_content or (to != -1 and from_ > to):
                raise IndexError
            elif to == -1:
                return content[from_:]
            else:
                return content[from_:to]

    def ed_find(self, filename: str, search_str: str)->list[int]:
        """Returns a list of indexes where search_str begins in temp_file. If no occurences are found, 
        return an empty list."""
        with open(file=filename, encoding="utf-8") as temp_file:
            content = temp_file.read()
            positions = []
            position = content.find(search_str)
            while position != -1:
                positions.append(position)
                position = content.find(search_str, position+1)
            return positions

    def ed_replace(self, filename: str, search_str: str, replace_with: str, occurrence:int=-1)->int:
        """Returns number of times search_str is replaced with replace_with."""
        with open(file=filename, encoding="utf-8") as temp_file:
            content = temp_file.read()
            positions = self.ed_find(filename, search_str)
            if occurrence == -1:
                occurrences = content.count(search_str)
                content = content.replace(search_str, replace_with)
            elif occurrence >= 0:
                if occurrence < len(positions):
                    position = positions[occurrence]
                    occurrences = 1
                    content = content[:position] + replace_with + content[position + len(search_str):]
                else:
                    return 0
            else:
                raise ValueError

        with open(filename, "w", encoding="utf-8") as wrt_file:
            wrt_file.write(content)
        
        return occurrences

    def ed_append(self, filename: str, string: str)->int:
        """Appends string to end of file and returns number of characters in appended file."""
        with open(filename, "a", encoding="utf-8") as app_file:
            return app_file.write(string)

    def testif(self, b: bool, testname: str, msgOK: str="", msgFailed: str="") -> bool:
        """Function used for testing.
        param b: boolean, normally a tested condition: true if test passed, false
        otherwise
        param testname: the test name
        param msgOK: string to be printed if param b==True ( test condition true)
        param msgFailed: string to be printed if param b==False
        returns b
        """
        if b:
            print("Success: "+ testname + "; " + msgOK)
        else:
            print("Failed: "+ testname + "; " + msgFailed)
        return b  

    def test_ed_find(self)->None:
        """Test method for ed_find."""
        test_file = "test_file.txt"
        write = "Appends string to end of file and returns number of characters in appended file."
        with open(test_file, "w", encoding="utf-8") as wrt_file:
            wrt_file.write(write)
        self.testif(self.ed_find(test_file, "end") == [3, 18, 69], "Find end", "Test passed.", "Test failed.")
        self.testif(self.ed_find(test_file, "file") == [25, 75], "Find file", "Test passed.", "Test failed.")

    def test_ed_replace(self)->None:
        """Test method for ed_replace."""
        test_file = "test_file.txt"
        write = "Appends string to end of file and returns number of characters in appended file."
        with open(test_file, "w", encoding="utf-8") as wrt_file:
            wrt_file.write(write)
        self.testif(self.ed_replace(test_file, "end", "start", -1) == 3, "Replace end", "Test passed.", "Test failed.")
        self.testif(self.ed_replace(test_file, "file", "start", -1) == 2, "Replace file", "Test passed.", "Test failed.") 
        try:
            self.ed_replace(test_file, "file", "start", -2)   
            self.testif(False, "ValueError", "Test passed.", "Test failed.")
        except ValueError:
            self.testif(True, "ValueError", "Test passed.", "Test failed.")

    def main(self)->None:
        """Main method for calling all methods in part A."""
        test_file = "test_file.txt"
        write = "Appends string to end of file and returns number of characters in appended file."
        with open(test_file, "w", encoding="utf-8") as wrt_file:
            wrt_file.write(write)
        print(self.ed_read(test_file, 4, 20))
        print(self.ed_find(test_file, "end"))
        print(self.ed_replace(test_file, "file", "start", 1))
        print(self.ed_append(test_file, "finished"))

        self.test_ed_find()
        self.test_ed_replace()

solution = TextEditor()
print("Z23734170")
solution.main()