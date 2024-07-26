import turtle
import random

def draw_line(t, x1, y1, x2, y2, color):

  t.penup()
  t.goto(x1, y1)
  t.pendown()
  t.pencolor(color)
  t.goto(x2, y2)

def draw_constellation(t, screen_width, screen_height, num_lines):
  
  colors = ["white", "lightblue", "yellow", "orange", "pink"]  
  for _ in range(num_lines):
    start_x = random.randint(-screen_width // 2, screen_width // 2)
    start_y = random.randint(-screen_height // 2, screen_height // 2)
    end_x = random.randint(-screen_width // 2, screen_width // 2)
    end_y = random.randint(-screen_height // 2, screen_height // 2)
    color = random.choice(colors)
    draw_line(t, start_x, start_y, end_x, end_y, color)

t = turtle.Turtle()

t.speed(0)  

screen = turtle.Screen()
screen.bgcolor("black")

t.pensize(1)

t.hideturtle()

screen_width = screen.window_width()
screen_height = screen.window_height()

draw_constellation(t, screen_width, screen_height, 50)

turtle.done()


