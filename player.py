import turtle

# Constants
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10

class Player(turtle.Turtle):
    
    # Constructor
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.reset_position()

    # Puts turtle in starting position
    def reset_position(self):
        self.goto(STARTING_POSITION)
    
    # Moves turtle forward
    def move(self):
        self.forward(MOVE_DISTANCE)
        
