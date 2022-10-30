#import game modules
from glob import glob
from time import time
from turtle import pos
import pgzrun
from random import randint

#create the game window
WIDTH = 600
HEIGHT = 600


#create variables
score = 0
game_over = False


#create the actors and starting postitions
player = Actor('player')
player.pos = 100, 100

coin = Actor('coin')
coin.pos = 200, 200

enemy = Actor('enemy')
enemy.pos = 500, 500

snake_head = Actor('snake_head')
snake_head.pos = 160, 160

snake_body = Actor('snake_body')
snake_body.pos = 160, 200


#draw the game
def draw():
    screen.fill('black')
    player.draw()
    coin.draw() 
    enemy.draw()
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
    


#constantly updates the game
def update(delta):
    global score


    #checks if player colides with coin
    if snake_head.colliderect(coin):
        score += 10
        place_coin()

    #checks if player colides with enemy
    if snake_head.colliderect(enemy):
        time_up()   
    

    #snake head movement
    if keyboard.left:
     snake_head.x -= 4

    if snake_head.x < 0:
     snake_head.x = WIDTH

    if keyboard.right:
     snake_head.x += 4

    if snake_head.x > WIDTH:
     snake_head.x = 0

    if keyboard.up:
     snake_head.y -= 4

    if snake_head.y > HEIGHT:
     snake_head.y = 0

    if keyboard.down:
     snake_head.y += 4
    
    if snake_head.y < 0:
     snake_head.y = HEIGHT

    #makes the enemy follow the player
    if snake_body.x < snake_head.x:
       snake_body.x +=4

    if snake_body.x > snake_head.x:
       snake_body.x -=4

    if snake_body.y < snake_head.y:
       snake_body.y += 4

    if snake_body.y > snake_head.y:
       snake_body.y -= 4



#random placement of coin at start of game
place_coin()

pgzrun.go()