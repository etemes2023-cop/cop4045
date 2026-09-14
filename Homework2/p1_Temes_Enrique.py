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

    def main(self, inp, out):
        self.line_number(inp, out)
        
