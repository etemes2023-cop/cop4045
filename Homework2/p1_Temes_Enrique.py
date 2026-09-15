import ast
class ParseFiles:
    def __init__(self):
        pass

    def line_number(self, inp: str, out: str) -> None:
        """Reads input text file, adds line numbers to each line, and writes each line to output file. If file is not found,
        an error message is printed and the exception is reraised."""
        try: 
            input_file = open(inp, "r")
            output_file = open(out, "w")
            line_count = 1
            for line_str in input_file:
                prefix = f"{line_count}."
                line_str = prefix + line_str
                print(line_str, file=output_file)
                line_count += 1

            input_file.close()
            output_file.close()

        except FileNotFoundError:
            print("File ", inp, "doesn't exist.")
            raise

    def parse_functions(self, filename: str) -> tuple:
        """Reads input file and creates a tuple of tuples. Each individual tuple contains the function definition line number,
        the function name, each function argument, and a list of code for that function definition. Empty lines or comments
        are skipped."""
        try:
            input_file = open(filename, "r")
            source_code = input_file.readlines()
            tree = ast.parse("".join(source_code))
            functions = []
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    starting_number = node.lineno
                    name = node.name
                    arguments = ast.unparse(node.args)
                    ending_number = node.end_lineno
                    code = []
                    for i in range(starting_number, ending_number+1):
                        if source_code[i-1].strip() == "" or source_code[i-1].strip().startswith("#"): 
                            continue
                        code.append(source_code[i-1])
                    functions.append((starting_number, name, arguments, "".join(code)))

            functions.sort(key=lambda x:x[1])
            return tuple(functions)  
           
        except FileNotFoundError:
                print("File ", filename, "doesn't exist.")
                raise

    def main(self, inp, out):
        self.line_number(inp, out)
        print(self.parse_functions(inp))

parse = ParseFiles()       
parse.main("C:/Users/eteme/Documents/FAU/Python Programming/Homework1/p2_Temes_Enrique.py", "output.txt")