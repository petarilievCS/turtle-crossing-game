import turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(turtle.Turtle):
    
    # Constructor
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-280, 260)
        self.hideturtle()
        self.level = 0
        self.update()

    # Increase level
    def level_up(self):
        self.level += 1
        self.update()

    # Resets level
    def reset(self):
        self.level = 0
        self.update()
    
    # Update score
    def update(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", align="left", font=FONT)
