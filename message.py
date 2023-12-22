import turtle

FONT = ("Courier", 24, "normal")

class Message(turtle.Turtle):
    
    # Constructor
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 0)

    def write_message(self, message):
        self.clear()
        self.write(arg=message, align="center", font=FONT)
        
