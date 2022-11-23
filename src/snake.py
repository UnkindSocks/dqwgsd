#import game modules
from curses import KEY_LEFT, KEY_RIGHT, KEY_UP
from glob import glob
from this import d
from time import time
from turtle import pos, up
import pgzrun
from random import randint

#create the game window
WIDTH = 600
HEIGHT = 600


#create variables
score = 0
game_over = False
direction = 1 


#create the actors and starting postitions

coin = Actor('coin')
coin.pos = 200, 200

snake_head = Actor('snake_head')
snake_head.pos = 160, 160
snake_head.direction = 1

snake_body = Actor('snake_body')
snake_body.pos = 160, 200


speed = 2 
#draw the game
def draw():
    screen.fill('black')
    coin.draw() 
    snake_head.draw()
    snake_body.draw()

    #draws the score
    screen.draw.text('score: ' + str(score), topleft=(10, 10), fontsize=38)


    if game_over:
        screen.fill('blue')
        screen.draw.text(' Final Score: ' + str(score), center=(300, 300), fontsize=100)


#places the coin in random locations
def place_coin():
    coin.x = randint (50, (WIDTH - 50))
    coin.y = randint (50, (HEIGHT - 50))

#runs when time is out
def time_up():
    global game_over
    game_over = True

#checking for left and right
def on_key_up(key, mod):
    global direction
    if key == keys.RIGHT:
        snake_head.direction += 1
        snake_head.angle -= 90

    if key == keys.LEFT:
        snake_head.direction -= 1    
        snake_head.angle += 90

    if snake_head.direction == 0:
        snake_head.direction = 4
    
    if snake_head.direction == 5:
        snake_head.direction = 1 

#loops the actors
def loop(actor):
     if actor.x < 0:
        actor.x = WIDTH

     if actor.x > WIDTH:
        actor.x = 0

     if actor.y > HEIGHT:
        actor.y = 0
    
     if actor.y < 0:
        actor.y = HEIGHT
 
#moving the actors
def move_actor(actor):
     if actor.direction == 1:
        actor.y -= speed  

     if actor.direction == 2:
        actor.x += speed

     if actor.direction == 3:
        actor.y += speed

     if actor.direction == 4:
        actor.x -= speed

#constantly updates the game
def update(delta):
    global score
    global direction


    #checks if snake colides with coin
    if snake_head.colliderect(coin):
        score += 10
        place_coin()
    
    #move and loops the snake head
    move_actor(snake_head)

    loop(snake_head)
    #makes the body follow the head
    if snake_body.x < snake_head.x:
       snake_body.x += speed

    if snake_body.x > snake_head.x:
       snake_body.x -= speed

    if snake_body.y < snake_head.y:
       snake_body.y += speed

    if snake_body.y > snake_head.y:
       snake_body.y -= speed


    loop(snake_body)

#random placement of coin at start of game
place_coin()

pgzrun.go()