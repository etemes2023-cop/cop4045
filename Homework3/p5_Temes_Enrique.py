class NChooseK:
    n_choose_k = {}

    def __init__(self):
        pass

    def cnk_m(self, n, k):
        if (n,k) in self.n_choose_k:
            return self.n_choose_k[(n,k)]
        
        if k == 0 or k == n:
            self.n_choose_k[(n,k)] = 1
            return 1
        elif k > n or k < 0:
            self.n_choose_k[(n,k)] = 0
            return 0
        else:
            value = self.cnk_m(n-1, k-1) + self.cnk_m(n-1, k)
            self.n_choose_k[(n,k)] = value

        return value

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

    def run_cnk(self):
       self.testif(self.cnk_m(5,2)==10, "Test 1", "Test passed.", "Test failed.")
       self.testif(self.cnk_m(6,3)==20, "Test 2", "Test passed.", "Test failed.")
       self.testif(self.cnk_m(5,0)==1, "Test 3", "Test passed.", "Test failed.")
       self.testif(self.cnk_m(2,3)==0, "Test 4", "Test passed.", "Test failed.")


n = int(input("Enter n: "))
k = int(input("Enter k: "))
value = NChooseK()
result = value.cnk_m(n,k)
print(result)
value.run_cnk()