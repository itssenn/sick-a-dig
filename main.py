import pygame
from setting import *
from player import Player
from sprite import *
from pytmx.util_pygame import load_pygame
from groups import Allsprites

from random import randint

pygame.init()

running = True
display_surface = pygame.display.set_mode((sc_w, sc_h))
pygame.display.set_caption("Dig")
clock = pygame.time.Clock()

#groups
collision_sprites = pygame.sprite.Group()
all_sprites = Allsprites()

def setup():
    map = load_pygame("maps/map.tmx")

    for x, y, image in map.get_layer_by_name("sky").tiles():
        Sprite((x * TILE_SIZE ,y * TILE_SIZE),image, all_sprites)
    for x, y, image in map.get_layer_by_name("ground").tiles():
        CollisionSprite((x * TILE_SIZE ,y * TILE_SIZE),image, (all_sprites, collision_sprites), is_diggable=True)
    
    # for x, y, image in map.get_layer_by_name("ground").tiles():
    #     CollisionSprite((x * TILE_SIZE ,y * TILE_SIZE),image, (all_sprites, collision_sprites))

        

setup()

#Sprite
player = Player((sc_w/2,sc_h/3), all_sprites, collision_sprites)


while running:
    
    #Data
    dt = clock.tick()/1000

    #Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Update
    all_sprites.update(dt)

    #Draw
    display_surface.fill('black')
    all_sprites.draw(player.rect.center)
    pygame.display.update()

pygame.quit()