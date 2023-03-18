# import colorgram
#
# rgb_colors= []
# colors = colorgram.extract('image.jpg',30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.g
#     new_color= (r,g,b)
#
#     rgb_colors.append(new_color)
# print(rgb_colors)
import turtle as turtle_module
import random


turtle_module.colormode(255)
tim= turtle_module.Turtle()
color_list =[(77, 179, 179), (222, 138, 138), (167, 212, 212), (225, 76, 76), (44, 131, 131), (195, 54, 54), (227, 226, 226), (224, 228, 228), (228, 226, 226)]

tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots= 100
for dot_count in range(1, number_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()