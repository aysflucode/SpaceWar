import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1200,800))
clock = pygame.time.Clock()
running = True
player_color = (150, 255, 150)

score = 0

game_over_font = pygame.font.Font(pygame.font.get_default_font(), 80)
score_font = pygame.font.Font(pygame.font.get_default_font(), 20)

bullet_img = pygame.image.load("laserGreen.png")
player_img = pygame.image.load("player.png")
obstacle_img = pygame.image.load("meteorBig.png")
space_png = pygame.image.load("space.jpg")

obstacle_pos_list = [(300,200),(450,200),(600,200),(750,200),
                 (300,320),(450,320),(600,320),(750,320)
                 ]

bullet_list =[]

def create_bullet():
    new_bullet_pos = (player.position.x + 45 , player.position.y )
    new_bullet = Bullet(new_bullet_pos)
    bullet_list.append(new_bullet)

class Bullet:
    def __init__(self, position):
        self.position = pygame.Vector2(position)

    def update(self):
        new_pos = pygame.Vector2(self.position[0], self.position[1] - 20)
        self.position = new_pos


class Player:
    def __init__(self, position):
        self.position = pygame.Vector2(position)
    

player = Player((550,600))

class Obstacle:
    def __init__(self, position):
        self.position = pygame.Vector2(position)

obstacle_list = []

def create_obstacles():
    for pos in obstacle_pos_list:
        new_obstacle = Obstacle(pos)
        obstacle_list.append(new_obstacle)



create_obstacles()

while running:

    screen.blit(space_png, (0,0))

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                create_bullet()

  

    text_surface = score_font.render('Score: ' + str(score), True, "red")
    screen.blit(text_surface, dest=(10,10))

    pygame.display.set_caption("Deneme Oyunu")

    screen.blit(player_img, player.position)



    for obsticle in obstacle_list:
        screen.blit(obstacle_img, obsticle.position)
    
    for bullet in bullet_list:
        screen.blit(bullet_img, bullet.position)
        bullet.update()
        if bullet.position.y <= 0:
            bullet_list.remove(bullet)
        for obsticle in obstacle_list:
            if bullet.position.x   >= obsticle.position.x  and bullet.position.x <= obsticle.position.x+ 136 and bullet.position.y >= obsticle.position.y and bullet.position.y <= obsticle.position.y + 111:
                obstacle_list.remove(obsticle)
                bullet_list.remove(bullet)
                score += 1


    keys = pygame.key.get_pressed()
    if keys [pygame.K_UP]:
        player.position.y -= 300 * dt
    if keys [pygame.K_DOWN]:
        player.position.y += 300 * dt
    if keys [pygame.K_LEFT]:
        player.position.x -= 300 * dt
    if keys [pygame.K_RIGHT]:
        player.position.x += 300 * dt

    if len(obstacle_list) == 0:
        text_surface = game_over_font.render('Oyun Bitti', True, "red")
        screen.blit(text_surface, dest=(400,350))


    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()