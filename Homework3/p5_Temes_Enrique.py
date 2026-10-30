import turtle
def testif(b: bool, testname: str, msgOK: str="", msgFailed: str="") -> bool:
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

class Leaf:
    def draw_leaf_straight(self, level, length):
        position = turtle.position()
        heading = turtle.heading()
        if level == 1:
            turtle.forward(length*0.4)
            branch_position = turtle.position()
            branch_heading = turtle.heading()

            turtle.left(45)
            turtle.forward(length*0.5)
            turtle.setposition(branch_position)
            turtle.setheading(branch_heading)

            turtle.right(45)
            turtle.forward(length*0.5)
            turtle.setposition(branch_position)
            turtle.setheading(branch_heading)

            turtle.forward(length*0.5)
            turtle.setposition(position)
            turtle.setheading(heading)
            return

        turtle.forward(length*0.4)
        branch_position = turtle.position()
        branch_heading = turtle.heading()

        turtle.left(45)
        self.draw_leaf_straight(level-1, length*0.7)
        turtle.setposition(branch_position)
        turtle.setheading(branch_heading)

        turtle.right(45)
        self.draw_leaf_straight(level-1, length*0.7)
        turtle.setposition(branch_position)
        turtle.setheading(branch_heading)

        turtle.forward(length*0.6)
        turtle.setposition(position)
        turtle.setheading(heading)

    #Extra Credit
    def draw_leaf_curved(self, level, length):
        position = turtle.position()
        heading = turtle.heading()
        if level == 1:
            for i in range(10):    
                turtle.forward(length*0.04)
                turtle.left(2)

            branch_position = turtle.position()
            branch_heading = turtle.heading()
    
            turtle.left(40)
            turtle.forward(length*0.5)
            turtle.setposition(branch_position)
            turtle.setheading(branch_heading)
    
            turtle.right(40)
            turtle.forward(length*0.5)
            turtle.setposition(branch_position)
            turtle.setheading(branch_heading)
    
            for i in range(10):    
                turtle.forward(length*0.04)
                turtle.left(2)
            return
        
        for i in range(10):    
            turtle.forward(length*0.04)
            turtle.left(2)

        branch_position = turtle.position()
        branch_heading = turtle.heading()
    
        turtle.left(40)
        self.draw_leaf_curved(level-1, length*0.7)
        turtle.setposition(branch_position)
        turtle.setheading(branch_heading)
    
        turtle.right(40)
        self.draw_leaf_curved(level-1, length*0.7)
        turtle.setposition(branch_position)
        turtle.setheading(branch_heading)
    
        for i in range(10):    
            turtle.forward(length*0.04)
            turtle.left(2)

        turtle.setposition(position)
        turtle.setheading(heading)
    
    def main(self):
        turtle.speed(0)
        turtle.delay(0)
        turtle.up()
        turtle.goto(0, -120)
        turtle.setheading(90)
        turtle.down()
        self.draw_leaf_straight(6, 120)

        turtle.reset()
        turtle.goto(0, -120)
        turtle.setheading(90)
        turtle.down()

solution = Leaf()
solution.main()
solution.draw_leaf_curved(6, 120)

class Conversion:
    def __init__(self):
        pass

    def strB(self, n, base=10):
        if not isinstance(n,int) or isinstance(n,bool) or n < 0:
            raise ValueError

        if not isinstance(base, int) or isinstance(base, bool) or not 2 <= base <= 26:
            raise ValueError
        
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

    def main(self):
        testif(self.strB(25, 2)=="11001", "Test 1", "Test passed.", "Test failed.")
        testif(self.strB(10, 2)=="1010", "Test 2", "Test passed.", "Test failed.")
        testif(self.strB(25, 26)=="P", "Test 3", "Test passed.", "Test failed.")
        testif(self.strB(0, 10)=="0", "Test 4", "Test passed.", "Test failed.")

solution = Conversion()
solution.main()

class NChooseK:
    n_choose_k = {}

    def __init__(self):
        pass

    def Cnk_m(self, n, k):
        if (n,k) in self.n_choose_k:
            return self.n_choose_k[(n,k)]
        
        if k == 0 or k == n:
            self.n_choose_k[(n,k)] = 1
            return 1
        elif k > n or k < 0:
            self.n_choose_k[(n,k)] = 0
            return 0
        else:
            value = self.Cnk_m(n-1, k-1) + self.Cnk_m(n-1, k)
            self.n_choose_k[(n,k)] = value

        return value

    def run_Cnk(self):
       testif(self.Cnk_m(5,2)==10, "Test 1", "Test passed.", "Test failed.")
       testif(self.Cnk_m(6,3)==20, "Test 2", "Test passed.", "Test failed.")
       testif(self.Cnk_m(5,0)==1, "Test 3", "Test passed.", "Test failed.")
       testif(self.Cnk_m(2,3)==0, "Test 4", "Test passed.", "Test failed.")


n = int(input("Enter n: "))
k = int(input("Enter k: "))
value = NChooseK()
result = value.Cnk_m(n,k)
print(result)
value.run_Cnk()

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

    def test_make_pairs(self):
        testif(self.make_pairs([1,2,3], ['a','b','c'], []) == [(1, 'a'), (2, 'b'), (3, 'c')], "Test 1", "Test passed.", "Test failed.")
        testif(self.make_pairs([1,2,3], ['a','b'], []) == [(1, 'a'), (2, 'b')], "Test 2", "Test passed.", "Test failed.")
        testif(self.make_pairs([1,2], ['a','b','c'], []) == [(1, 'a'), (2, 'b')], "Test 3", "Test passed.", "Test failed.")
        testif(self.make_pairs([1,2,3], [], []) == [], "Test 4", "Test passed.", "Test failed.")
        testif(self.make_pairs([], [], []) == [], "Test 5", "Test passed.", "Test failed.")

solution = Pairs()
print("Z23734170")
solution.test_make_pairs()