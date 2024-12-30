import pgzrun

WIDTH = 1200
HEIGHT = 600
TITLE = 'Galaga Game'

ship = Actor('ship')
ship.pos = (600,540)

score = 0
speed = 5
bullets = []
enemies = []
direction = 1
ship.dead = False
ship.countdown = 90

for x in range(8):
    for y in range(4):
        enemies.append(Actor('bug'))
        enemies[-1].x = 100 + 50* x #150,200,250
        enemies[-1].y = 80 + 50* y

def on_key_down(key):
    if ship.dead == False:
        if key == keys.SPACE:
            bullets.append(Actor('bullet'))
            bullets[-1].x = ship.x
            bullets[-1].y = ship.y - 50

def game_over():
    screen.draw.text("Game Over\ntry again",(250,300))





def draw():
    screen.clear()
    screen.fill('light blue')
    if ship.dead == False:
        ship.draw()
    for i in enemies:
        i.draw()
    for j in bullets:
        j.draw()
    screen.draw.text("score = "+str(score), (20,20),color = 'black')
    if len(enemies) == 0:
        game_over()







pgzrun.go()