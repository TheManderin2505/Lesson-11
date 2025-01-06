import pgzrun

WIDTH = 1200
HEIGHT = 600
TITLE = 'Game'

ship = Actor('warthog')
ship.pos = (600,500)

score = 0
speed = 5
bullets = []
enemies = []
direction = 1
ship.dead = False
ship.countdown = 90
lives = 3

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
    screen.draw.text("Game Over\ntry again",(250,300),color = "black")


def update():
    global score, direction, lives
    moveDown = False 
    if ship.dead == False:
        if keyboard.A:
            ship.x-= speed
            if ship.x <= 0:
                ship.x = 0
        elif keyboard.D:
            ship.x+=speed
            if ship.x >= 1200:
                ship.x = 1200
    for bullet in bullets:
        if bullet.y <= 0:
            bullets.remove(bullet)
        else:
            bullet.y -= 10
    if len(enemies)>0 and (enemies[-1].x > WIDTH - 80 or enemies[0].x < 80):
        moveDown = True
        direction = direction*-1
    for enemy in enemies:
        enemy.x += 2*direction
        if moveDown == True:
            enemy.y += 100
        if enemy.y > HEIGHT:
            enemies.remove(enemy)
        for bullet in bullets:
            if enemy.colliderect(bullet):
                score += 100
                bullets.remove(bullet)
                enemies.remove(enemy)
                if len(enemies) == 0:
                    game_over()
        if enemy.colliderect(ship):
            ship.dead = True
    if ship.dead:
        ship.countdown -=1
        

    if ship.countdown == 0:
        ship.dead = False
        ship.countdown = 90
        lives = lives - 1




def draw():
    screen.clear()
    screen.fill('beige')
    if ship.dead == False:
        ship.draw()
    for i in enemies:
        i.draw()
    for j in bullets:
        j.draw()
    screen.draw.text("score = "+str(score), (20,20),color = 'black')
    screen.draw.text("Lives = "+str(lives), (20,40),color = 'red')
    if lives == 0:
        game_over()
    if len(enemies) == 0:
        game_over()







pgzrun.go()
