from turtle import *
import random
import time


def playing_area():
    pen = Turtle()
    pen.ht()
    pen.speed(0)
    pen.color('brown')
    
    pen.up()
    pen.goto(-320,245)
    pen.down()
    pen.goto(325,245)
    pen.goto(325,-245)
    pen.goto(-325,-245)
    pen.goto(-325,245)
    pen.end_fill()
    
class Head(Turtle):
  def __init__(self, screen):
    super().__init__()
    self.shape("square")
    self.shapesize()
    self.penup()
    self.hideturtle()

    self.alive = True
    
    self.direction = "left"
    self.ticks = 0
    self.turn_tick = 0
    self.directions = {"left": 180, "right" : 0, "up":90, "down" :270}
    self.opposite_direction = {"left":"right", "up": "down", "right": "left", "down": "up"}
    self.processingdirections = []


    screen.onkeypress( self.up,"w")
    screen.onkeypress( self.down,"s")
    screen.onkeypress( self.left,"a")
    screen.onkeypress( self.right, "d")
    

  def up(self):
    if self.direction != "down"  and self.ticks == self.turn_tick:
      self.processingdirections.append("up")
      
      self.turn_tick = self.ticks + 1
    elif self.direction != "down"  and self.ticks != self.turn_tick:
      self.direction = "up"
      self.turn_tick = self.ticks
    
  def down(self):
    if self.direction != "up"  and self.ticks == self.turn_tick:
      self.processingdirections.append("down")
      
      self.turn_tick = self.ticks + 1
    elif self.direction != "up"  and self.ticks != self.turn_tick:
      self.direction = "down"
      self.turn_tick = self.ticks

  def left(self):
    if self.direction != "right"  and self.ticks == self.turn_tick:
      self.processingdirections.append("left")
      
      self.turn_tick = self.ticks + 1
    elif self.direction != "right"  and self.ticks != self.turn_tick:
      self.direction = "left"
      self.turn_tick = self.ticks

  def right(self):
    if self.direction != "left"  and self.ticks == self.turn_tick:
      self.processingdirections.append("right")
      
      self.turn_tick = self.ticks + 1
    elif self.direction != "left"  and self.ticks != self.turn_tick:
      self.direction = "right"
      self.turn_tick = self.ticks
    
  def move(self, apple, body):

    self.clear()
    previous_positions = [(segment.xcor(), segment.ycor()) for segment in body]
    if self.processingdirections:
      next_direction = self.processingdirections[-1]
      if next_direction != self.direction and next_direction != self.opposite_direction[self.direction]:
        self.direction = next_direction
      self.processingdirections = []
    self.setheading(self.directions.get(self.direction))
    self.forward(20)

    if self.xcor() == 320 or self.xcor() == -320 or self.ycor() == 320 or self.ycor() == -320:
      self.die()

    for i in range(len(body) - 1, 0, -1):
      body[i].move(previous_positions[i - 1])

    for segment in body[1:]:
      if self.distance(segment) < 20:
        self.die()
       

    if self.distance(apple) <= 10:
        apple.relocate()
        body.append(Segment(previous_positions[-1]))
    self.ticks += 1
    self.stamp()
    return body
    
  def die(self):

    self.alive = False
    
    


class Segment(Turtle):
  def __init__(self, poition):
    super().__init__()
    self.shape("square")
    self.color("brown")
    self.up()
    self.ht()
    self.goto(poition)

  def move(self, position):
    self.clear()
    self.goto(position)
    self.stamp()
    

class Apple(Turtle):
  def __init__(self):
    super().__init__()
    self.hideturtle()
    self.penup()
    self.color("red")
    self.shape("square")
    self.goto(random.randint(-32,32) * 10, random.randint(-24,24) * 10)
    self.stamp()



  def relocate(self):
    self.clear()
    self.goto(random.randint(-32,32) * 10, random.randint(-24,24) * 10)
    self.stamp()
screen = Screen()

screen.bgcolor("light green")
screen.setup(700,600)
# Key Binding. Connects key presses and mouse clicks with function calls
screen.listen()
head = Head(screen )

body = [head, Segment([20,0]), Segment([40,0])]
apple = Apple()
playing_area()


print(head.direction)
head.stamp()


screen.tracer(0)
while head.alive:
  
  body = head.move(apple, body)
  screen.update()
  time.sleep(0.33)


print("dead")
screen.mainloop()


screen.exitonclick()


