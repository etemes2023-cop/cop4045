class TextEditor:
    def __init__(self):
        pass

    def ed_read(self, filename: list[str], from_:int=0, to:int=-1)->str:
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
        """Returns a list of indexes where search_str begins in temp_file."""
        with open(file=filename, encoding="utf-8") as temp_file:
            content = temp_file.read()
            positions = []
            position = content.find(search_str)
            while position != -1:
                positions.append(position)
                position = content.find(search_str, position+1)
            return positions

    def ed_replace(self, filename: str, search_str: str, replace_with, occurrence:int=-1)->int:
        """Returns number of times search_str is replaced with replace_with."""
        with open(file=filename, encoding="utf-8") as temp_file:
            content = temp_file.read()
            positions = self.ed_find(filename, search_str)
            if occurrence == -1:
                occurrences = content.count(search_str)
                content = content.replace(search_str, replace_with)
                return 1
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
    
                  
