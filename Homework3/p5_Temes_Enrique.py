class Conversion:
    def __init__(self):
        pass

    def strB(self, n, base):
        conversion = ""
        if n < base:
            if n >= 10:
                return chr(n-10 + ord('A'))
            return str(n)
        else:
            quotient = n // base
            remainder = n % base
            if remainder >= 10:
                remainder = chr(remainder-10 + ord('A'))
            else:
                remainder = str(remainder)

            conversion += self.strB(quotient, base)
            conversion += remainder
        return conversion

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

    def main(self):
        #print(self.strB(25, 2))
        #print(self.strB(10, 2))
        #print(self.strB(25, 26))
        #print(self.strB(0, 10))

        self.testif(self.strB(25, 2)=="11001", "Test 1", "Test passed.", "Test failed.")
        self.testif(self.strB(10, 2)=="1010", "Test 2", "Test passed.", "Test failed.")
        self.testif(self.strB(25, 26)=="P", "Test 3", "Test passed.", "Test failed.")
        self.testif(self.strB(0, 10)=="0", "Test 4", "Test passed.", "Test failed.")


solution = Conversion()
solution.main()