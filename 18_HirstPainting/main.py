# ------ Importing libraries ------ #
import random
import turtle as t

# ------ Setting up the screen and turtle ------ #
t1 = t.Turtle()
screen = t.Screen()
screen.colormode(255)
t1.speed("fastest")

color_lis = [(133, 164, 202), (225, 150, 101), (30, 43, 64), (201, 136, 148), (163, 59, 49), (236, 212, 88), (44, 101, 147), (136, 181, 161), (148, 64, 72), (51, 41, 45), (161, 32, 29), (60, 115, 99), (59, 48, 45), (170, 29, 32), (215, 83, 73), (236, 167, 157), (230, 163, 168), (36, 61, 55), (15, 96, 71), (33, 60, 106), (172, 188, 219), (194, 99, 108), (106, 126, 158), (18, 83, 105), (175, 200, 188), (35, 150, 209)]
    
# ------ Function to draw dots ------ #
def draw_dots():
    t1.hideturtle() # Hiding the turtle cursor
    t1.penup()
    t1.setheading(270) # Pointing downwards
    t1.forward(250)
    t1.setheading(180)
    t1.forward(200)
    t1.setheading(0)
    
    # Drawing 10x10 grid of dots
    for i in range(1,101): # 100 dots
        t1.dot(30, random.choice(color_lis))
        t1.forward(50) # distance between dots
        if i % 10 == 0:
            t1.left(90)
            t1.forward(50)
            t1.left(90)
            t1.forward(500) # 10 dots * 50 distance
            t1.setheading(0)
    
draw_dots()
screen.mainloop()

# ------- To extract colors from an image using colorgram ------- #
# import colorgram
#colors = colorgram.extract("photo.jpg", 30)
#rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

    
