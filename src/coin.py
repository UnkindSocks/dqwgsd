#import game modules
from glob import glob
from time import time
import pgzrun
from random import randint

#create the game window
WIDTH = 600
HEIGHT = 600


#create variables
score = 0
timer = 10
game_over = False

#create the actors and starting postitions
player = Actor('player')
player.pos = 100, 100

coin = Actor('coin')
coin.pos = 200, 200

enemy = Actor('enemy')
enemy.pos = 500, 500

#draw the game
def draw():
    screen.fill('black')
    player.draw()
    coin.draw() 
    enemy.draw()

    #draws the score
    screen.draw.text('score: ' + str(score), topleft=(10, 10), fontsize=38)

    #draws the timer
    screen.draw.text('timer: ' + str(round(timer)), topright=(275, 10), fontsize=38)

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
    global timer

    #updates the timer
    timer -= delta
    if timer <= 0:
        time_up()

    #checks if player colides with coin
    if player.colliderect(coin):
        score += 10
        timer += 2
        place_coin()

    #checks if player colides with enemy
    if player.colliderect(enemy):
        time_up()   
    

    #player movement
    if keyboard.left and player.x > 0:
        player.x -= 4

    if keyboard.right and player.x < WIDTH:
        player.x += 4

    if keyboard.up and player.y > 0:
        player.y -= 4

    if keyboard.down and player.y < HEIGHT:
        player.y += 4


    #makes the enemy follow the player
    if enemy.x < player.x:
        enemy.x +=1.3

    if enemy.x > player.x:
        enemy.x -=1.3

    if enemy.y < player.y:
        enemy.y += 1.3

    if enemy.y > player.y:
        enemy.y -= 1.3


#random placement of coin at start of game
place_coin()

pgzrun.go()