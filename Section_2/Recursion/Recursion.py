## Recursion_Code
from turtle import *

speed('fastest')
hideturtle()

def draw_snowflak_side(l, n):
    if n == 0:
        forward(l)
    else:
        draw_snowflak_side(l / 3, n - 1)
        left(60)
        draw_snowflak_side(l / 3, n - 1)
        right(120)
        draw_snowflak_side(l / 3, n - 1)
        left(60)
        draw_snowflak_side(l / 3, n - 1)

def draw_snowflake(l, n):
    for _ in range(3):
        draw_snowflak_side(l, n)
        right(120)

draw_snowflake(300, 3)
done()

