class Pairs:
    def __init__(self):
        pass

    acc=[]
    def make_pairs(self, seq1, seq2, acc):
        if not seq1 or not seq2:
            return acc
        
        x = seq1[0]
        y = seq2[0]
        pair = (x,y)
        acc.append(pair)
        return self.make_pairs(seq1[1:], seq2[1:], acc)

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

    def test_make_pairs(self):
        self.testif(self.make_pairs([1,2,3], ['a','b','c'], []) == [(1, 'a'), (2, 'b'), (3, 'c')], "Test 1", "Test passed.", "Test failed.")
        self.testif(self.make_pairs([1,2,3], ['a','b'], []) == [(1, 'a'), (2, 'b')], "Test 2", "Test passed.", "Test failed.")
        self.testif(self.make_pairs([1,2], ['a','b','c'], []) == [(1, 'a'), (2, 'b')], "Test 3", "Test passed.", "Test failed.")
        self.testif(self.make_pairs([1,2,3], [], []) == [], "Test 4", "Test passed.", "Test failed.")
        self.testif(self.make_pairs([], [], []) == [], "Test 5", "Test passed.", "Test failed.")

solution = Pairs()
solution.test_make_pairs()