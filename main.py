# Author: Jorgé Sandoval
# Assignment 1
# Date: 09-19-2024
# Main1: Creates a Turtle object for a figure then closes the window when clicked
# Main2: Creates a Turtle object to draw multiple figures instead of one
# Comparison of Main1 and Main2:
# - Main1 creates a new Turtle object each time a shape is drawn.
# - However, since each new object requires initialization it uses up more resources.
# On the other hand Main2 uses the same Turtle object to draw multiple figures.
# - This is more efficient in terms of memory, 
# this function also provides better  user experience as the user can draw multiple figures without having to restart the program each time.

# Import modules
import turtle

'''Function that takes in a turtle object and a side length and draws a square'''
def draw_square(my_turtle, side_length):
    # A loop that runs four times to draw the four sides of the square
    for i in range(4):
        my_turtle.forward(side_length)
        my_turtle.right(90)

'''Function that takes in a turtle object and a side length and draws an equilateral triangle'''
def draw_triangle(my_turtle, side_length):
    # A loop that runs three times to draw the three sides of the triangle
    for i in range(3):
        my_turtle.forward(side_length)
        my_turtle.right(120)

'''Function that takes in a turtle object and a radius and draws a circle'''
def draw_circle(my_turtle, radius):
    # Calls the circle method of the turtle object to draw a circle
    my_turtle.circle(radius)

'''Function that takes in a turtle object, the number of turns, and the initial side length and draws a spiral'''
def draw_spiral(my_turtle, num_turns, initial_side_length):
    # Stores initial side length in a variable
    side_length = initial_side_length
    # A loop that runs num_turns times to draw the spiral adding 5 to the side length each time
    for i in range(num_turns):
        my_turtle.forward(side_length)
        my_turtle.right(90)
        side_length += 5

'''Function that takes in a turtle object, the number of sides, and the side length and draws a polygon'''
def draw_polygon(my_turtle, num_sides, side_length):
    # Calculate the angle to turn based on the number of sides
    turn_angle = 360 / num_sides
    # A loop that runs num_sides times to draw the polygon
    for i in range(num_sides):
        my_turtle.forward(side_length)
        my_turtle.right(turn_angle)

'''Function to get the figure choice from the user'''
def get_user_choice():
    choice = input("Enter the figure you want to draw\nOptions:\nSquare\nTriangle\nCircle\nSpiral\nPolygon\n").strip().lower()
    return choice

'''Function to get the parameters needed for the chosen figure'''
def get_parameters(shape):
    # Dict of shape parameters
    shape_parameters = {
        'square': [('side_length', "Enter the side length: ")],
        'triangle': [('side_length', "Enter the side length: ")],
        'circle': [('radius', "Enter the radius: ")],
        'spiral': [
            ('num_turns', "Enter the number of turns: "),
            ('initial_side_length', "Enter the initial side length: ")
        ],
        'polygon': [
            ('num_sides', "Enter the number of sides: "),
            ('side_length', "Enter the side length: ")
        ]
    }

    # Check if the shape is in the dict
    if shape in shape_parameters:
        parameters = {}
        for param, prompt in shape_parameters[shape]:
            parameters[param] = int(input(prompt))
        return parameters
    else:
        print("Invalid choice")
        return None

# Function to process and draw the chosen figure
def process_choice(my_turtle, shape, parameters):
    if shape == 'square':
        draw_square(my_turtle, parameters['side_length'])
    elif shape == 'triangle':
        draw_triangle(my_turtle, parameters['side_length'])
    elif shape == 'circle':
        draw_circle(my_turtle, parameters['radius'])
    elif shape == 'spiral':
        draw_spiral(my_turtle, parameters['num_turns'], parameters['initial_side_length'])
    elif shape == 'polygon':
        draw_polygon(my_turtle, parameters['num_sides'], parameters['side_length'])
    else:
        print("Invalid choice")

'''Main function that creates a Turtle object for a figure then closes the window when clicked'''
def Main():
    # Create screen object
    screen = turtle.Screen()
 
    # Get the figure choice from the user
    user_choice = get_user_choice()
 
    # Get parameters needed for the shape
    parameters = get_parameters(user_choice)
 
    # Process the choice    
    if parameters:
        my_turtle = turtle.Turtle()  
        process_choice(my_turtle, user_choice, parameters)
        screen.mainloop()  
        screen.exitonclick() 

'''Main function that creates a Turtle object to draw multiple figures instead of one'''
def Main2():
    # Create screen object
    screen = turtle.Screen()
    my_turtle = turtle.Turtle()  

    # Loop to draw multiple figures
    while True:
        # Store the user choice and parameters
        user_choice = get_user_choice()
        parameters = get_parameters(user_choice)

        # Process the choice
        if parameters:
            process_choice(my_turtle, user_choice, parameters)
        cont = input('Do you want to draw another figure? (y/n): ').strip().lower()
        if cont != 'y':
            break
    
    screen.mainloop()

if __name__ == "__main__":
    Main()  
