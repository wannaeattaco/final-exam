import turtle
import random


def draw_polygon(num_sides, size, orientation, location, color, border_size):
    turtle.penup()
    turtle.goto(location[0], location[1])
    turtle.setheading(orientation)
    turtle.color(color)
    turtle.pensize(border_size)
    turtle.pendown()
    for _ in range(num_sides):
        turtle.forward(size)
        turtle.left(360/num_sides)
    turtle.penup()


def get_new_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


choice = int(input("Which art do you want to generate? Enter a number between 1 to 8,inclusive:"))
turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)

size = random.randint(50, 150)
orientation = random.randint(0, 90)
location = [random.randint(-300, 300), random.randint(-200, 200)]
color = get_new_color()
border_size = random.randint(1, 10)
if choice == 1:
    num_sides = 3  # triangle, square, or pentagon
    for i in range(10):
        draw_polygon(num_sides, size, orientation, location, color, border_size)

if choice == 2:
    num_sides = 4  # triangle, square, or pentagon
    for i in range(10):
        draw_polygon(num_sides, size, orientation, location, color, border_size)

if choice == 3:
    num_sides = 5  # triangle, square, or pentagon
    for i in range(10):
        draw_polygon(num_sides, size, orientation, location, color, border_size)
# draw a polygon at a random location, orientation, color, and border line thickness

num_sides = 3  # triangle, square, or pentagon
size = random.randint(50, 150)
orientation = random.randint(0, 90)
location = [random.randint(-300, 300), random.randint(-200, 200)]
color = get_new_color()
border_size = random.randint(1, 10)
# draw_polygon(num_sides, size, orientation, location, color, border_size)

# specify a reduction ratio to draw a smaller polygon inside the one above
reduction_ratio = 0.618

# reposition the turtle and get a new location
turtle.penup()
turtle.forward(size*(1-reduction_ratio)/2)
turtle.left(90)
turtle.forward(size*(1-reduction_ratio)/2)
turtle.right(90)
location[0] = turtle.pos()[0]
location[1] = turtle.pos()[1]

# adjust the size according to the reduction ratio
size *= reduction_ratio

# draw the second polygon embedded inside the original
# draw_polygon(num_sides, size, orientation, location, color, border_size)

# hold the window; close it by clicking the window close 'x' mark
turtle.done()


class Shape:
    def __init__(self, num_sides, size, orientation, location, color, border_size):
        self.num_sides = num_sides
        self.size = size
        self.orientation = orientation
        self.location = location
        self.color = color
        self.border_size = border_size

    def draw(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360/self.num_sides)
        turtle.penup()


class DrawShape:
    def __init__(self, choice):
        self.shape_list = []
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        turtle.colormode(255)
        for i in range(10):
            num_sides = 0
            if choice == 1 or choice == 5:
                num_sides = 3
            elif choice == 2 or choice == 6:
                num_sides = 4
            elif choice == 3 or choice == 7:
                num_sides = 4
            elif choice == 4 or choice == 8:
                num_sides = random.randint(3, 5)
            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-200, 200)]
            border_size = random.randint(1, 10)
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.shape_list.append(Shape(num_sides, size, orientation, location, color, border_size))

            reduction_ratio = 0.618
            size *= reduction_ratio
            turtle.penup()
            turtle.forward(size*(1-reduction_ratio)/2)
            turtle.left(90)
            turtle.forward(size*(1-reduction_ratio)/2)
            turtle.right(90)
            location[0] = turtle.pos()[0]
            location[1] = turtle.pos()[1]
            self.shape_list.append(Shape(num_sides, size, orientation, location, color, border_size))

    def run(self):
        while True:
            turtle.clear()
            for i in range(10):
                self.shape_list[i].draw()
            turtle.update()
        # hold the window; close it by clicking the window close 'x' mark
        turtle.done()


in_choice = int(input("Which art do you want to generate? Enter a number between 1 to 8,inclusive: "))
my_simulator = DrawShape(in_choice)
my_simulator.run()
