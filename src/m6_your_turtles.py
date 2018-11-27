"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Jacob Lauteri.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################
import rosegraphics as rg
########################################################################
# TODO: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
window = rg.TurtleWindow()
octavious = rg.SimpleTurtle('turtle')
octavious.pen = rg.Pen('turquoise', 15)
octavious.speed = 15

size = 300

for k in  range(10):
    octavious.draw_square(size)
    octavious.pen_up()
    octavious.right(60)
    octavious.forward(35)
    octavious.left(60)
    octavious.pen_down()
    size = size - 15

window.tracer(25)

rose = rg.SimpleTurtle('triangle')
rose.pen = rg.Pen('red',5)
rose.backward(25)

for k in range(500):
    rose.left(35)
    rose.forward(k)

window.close_on_mouse_click()