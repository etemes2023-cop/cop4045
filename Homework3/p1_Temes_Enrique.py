class NVector:
    """NVector class use a vector of numbers for a variety of purposes such as determining its length,
    getting vector items, setting vector item values, converting to a string, checking if other vectors are
    instances, and performing vector/scalar addition, reflective addition, vector/scalar multiplication, and
    reflective multiplication."""
    def __init__(self, *args: float | int | list[int | float])-> None:
        """Constructor that initializes NVector object and stores elements in new list."""
        if len(args) == 1:
            args_list = list(args[0])
        else:
            args_list = list(args)
        self.args = args_list

    def __len__(self)-> int:
        """"Returns the length of the args instance."""
        return len(self.args)

    def __getitem__(self, index: int)-> int | float:
        """Returns item in args instance list at the corresponding index."""
        return self.args[index]
   
    def __setitem__(self, index: int, value: int | float)-> None:
        """Sets item in args instance list at the corresponding index equal to value."""
        self.args[index] = value

    def __str__(self)-> str:
        """Returns a conversion of the args instance list to a string."""
        return str(self.args)

    def __eq__(self, other: object)-> bool:
        """If the other vector is a NVector instance and self.args equals other.args, return true. Otherwise, return False."""
        return isinstance(other, NVector) and self.args == other.args

    def __ne__(self, other: object)-> bool:
        """Returns True when objects are not equal and false otherwise."""
        return not self.__eq__(other)

    def __add__(self, other: NVector | int | float)-> NVector:
        """Performs vector addition if other is an instance of NVector and both vectors are the same size.
          Otherwise, perform scalar addition."""
        if isinstance(other, NVector):
            if len(self.args) == len(other.args):
                vector_sum = NVector([self.args[index] + other.args[index] for index in range(len(self.args))])
            else:
                raise ValueError
        else:
            vector_sum = NVector([self.args[index] + other for index in range(len(self.args))])
        
        return vector_sum

    def __radd__(self, other: float | int)-> NVector:
        """Performs reflected addition by calling the __add__ method and passing in the other parameter."""
        return self.__add__(other)

    def __mul__(self, other: NVector | float | int)-> int | float | NVector:
        """Performs vector multiplication if other is an instance of NVector and both vectors are the same size.
        Otherwise, perform scalar multiplication."""
        if isinstance(other, NVector):
            if len(self.args) == len(other.args):
                vector_product = sum([self.args[index] * other.args[index] for index in range(len(self.args))])
            else:
                raise ValueError
        else:
           vector_product = NVector([self.args[index] * other for index in range(len(self.args))])  

        return vector_product

    def __rmul__(self, other: float | int | NVector)-> NVector:
        """Performs reflected multiplication by calling the __mul__ method and passing in the other parameter."""
        return self.__mul__(other)

    @classmethod
    def zeros(cls, n: int)-> NVector:
        """Returns an NVector object with as many zeros equal to the value of parameter n. If n is negative, ValueError is raised."""
        if n < 0:
            raise ValueError
        
        return cls([0]*n)

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
    
    def main(self)-> None:
        v = NVector(1, 2, 3, 4)
        ov = NVector(3, 4, 5, 6)
        v[3] = 10
        print("Z23734170")
        v.testif(len(v) == 4, "Vector length", "Test passed.", "Test failed.")
        v.testif(v.__getitem__(0) == 1, "Get element", "Test passed.", "Test failed.")
        v.testif(v.__str__() == "[1, 2, 3, 10]", "Convert v", "Test passed.", "Test failed.")
        v.testif(v.__eq__(other=ov) == False, "Compare v and ov", "Test passed.", "Test failed.")
        v.testif(v.__ne__(other=ov) == True, "Negate v and ov", "Test passed.", "Test failed.")
        v.testif(v+ov == NVector(4, 6, 8, 16), "Add v and ov", "Test passed.", "Test failed.")
        v.testif(5+v == NVector(6,7,8,15), "Reflective addition", "Test passed.", "Test failed.")
        v.testif(v.__mul__(other=ov) == 86, "Multiply v and ov", "Test passed.", "Test failed.")
        v.testif(5*v == NVector(5, 10, 15, 50), "Reflective multiplication", "Test passed.", "Test failed.")
        v.testif(NVector.zeros(4) == NVector(0, 0, 0, 0), "Vector of length n", "Test passed.", "Test failed.")
solution = NVector()
solution.main()    