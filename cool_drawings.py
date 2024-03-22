"""
Put here your custom function to draw something.
The figure shouldn't surpass a square of 200x200 points.
The turtle passed should be start AND END pointing left at the right-left corner of the figure.
"""

def bluesquare_fernando(turtle):
    """
    Author: Fernando Santos
    Draws a simple 100x100 square
    """
    turtle.fillcolor('blue')
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(150)
        turtle.right(90)
    turtle.end_fill()

def square_fernando(turtle):
    """
    Author: Fernando Santos
    Draws a simple 100x100 square
    """ 
    turtle.fillcolor('green')
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(150)
        turtle.right(90)
    turtle.end_fill()
    
def fractal_fernando(t):
    """
    Author: Fernando Santos
    Draws a Koch line fractal
    """
    def koch_line(l):
        if l > unit:
            koch_line(l/3)
            t.left(60)
            koch_line(l/3)
            t.right(120)
            koch_line(l/3)
            t.left(60)
            koch_line(l/3)
        else:
            t.forward(unit)
    
    t.fillcolor('blue')
    t.begin_fill()
    unit, depth, poly_sides = 4, 3, 3
    length = (3**depth)*unit   # number is #segments
    for i in range(poly_sides):
        koch_line(length)
        t.right(360/poly_sides)
    t.end_fill()
    
  def square_Nation(t):
      """
      Author:Victoria Nation
      draws a blue square 100x100
      """
      turtle.fillcolor('blue')
      turtle.begin_fill()
      for i in range(4):
        turtle.forward(150)
        turtle.right(90)
      turtle.end_fill()
    
