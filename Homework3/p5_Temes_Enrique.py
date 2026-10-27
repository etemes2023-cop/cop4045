import turtle
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
        self.draw_leaf_straight(level-1, length*0.7)
        turtle.setposition(branch_position)
        turtle.setheading(branch_heading)
    
        turtle.right(40)
        self.draw_leaf_straight(level-1, length*0.7)
        turtle.setposition(branch_position)
        turtle.setheading(branch_heading)
    
        for i in range(10):    
            turtle.forward(length*0.04)
            turtle.left(2)

        turtle.setposition(position)
        turtle.setheading(heading)
    
    def main(self):
        turtle.up()
        turtle.goto(0, -120)
        turtle.setheading(90)
        turtle.down()
        #self.draw_leaf_straight(6, 120)
        self.draw_leaf_curved(8, 120)

solution = Leaf()
solution.main()