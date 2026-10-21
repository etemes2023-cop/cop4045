class NVector:
    def __init__(self, *args):
        """Constructor that initializes the length of vector."""
        if len(args) == 1:
            args_list = list(args[0])
        else:
            args_list = list(args)
        self.args = args_list

    def __len__(self):
        """"Returns the length of the args instance."""
        return len(self.args)

    def __getitem__(self, index):
        """Returns item in args instance list at the corresponding index."""
        return self.args[index]
   
    def __setitem__(self, index, value):
        """Sets item in args instance list at the corresponding index equal to value."""
        self.args[index] = value

    def __str__(self):
        """Returns a conversion of the args instance list to a string."""
        return str(self.args)

    def __eq__(self, other):
        """If the other vector is a NVector instance and self.args equals other.args, return true. Otherwise, return False."""
        return isinstance(other, NVector) and self.args == other.args

    def __ne__(self, other):
        """Returns True when objects are not equal and false otherwise."""
        return not self.__eq__(other)

    def __add__(self, other):
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

    def __radd__(self, other):
        """Performs reflected addition by calling the __add__ method and passing in the other parameter."""
        return self.__add__(other)

    def __mul__(self, other):
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

    def __rmul__(self, other):
        """Performs reflected multiplication by calling the __mul__ method and passing in the other parameter."""
        return self.__mul__(other)

    
    

    
        

    
    
    