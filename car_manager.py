import turtle
import random

# Constants
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Car(turtle.Turtle):

    # Constructor
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.goto(x, y)
        self.color(random.choice(COLORS))
        self.shape("square")
        self.setheading(180)
        self.shapesize(stretch_len=2)

class CarManager:
    
    # Constructor
    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    # Generate car
    def generate_car(self):
        x = 300
        y = random.randint(-280, 280)
        self.cars.append(Car(x, y))

    # Move cars
    def move(self):
        for car in self.cars:
            car.forward(self.move_distance)
    
    # Increase speed
    def speedup(self):
        self.move_distance += MOVE_INCREMENT

    # Reset speed
    def reset(self):
        self.move_distance = STARTING_MOVE_DISTANCE
