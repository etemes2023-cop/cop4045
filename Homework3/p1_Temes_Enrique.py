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
        return isinstance(other, NVector) and self.args == other.args
        

    
    
    