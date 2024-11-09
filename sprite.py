from setting import *

class Sprite(pygame.sprite.Sprite):
    def __init__(self, position, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = position)

class CollisionSprite(pygame.sprite.Sprite):
    def __init__(self, position, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = position)

class Block(pygame.sprite.Sprite):
    def __init__(self, position, surf, groups, block_name, is_diggable=False):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = position)
        self.is_diggable = is_diggable

        self.Ore = {'dirt':1, 'stone':3, 'ore':4}

        self.block_health = self.Ore[block_name]

    def take_damage(self):
        if self.is_diggable:
            self.block_health -= 1
            
            if self.block_health <= 0:
                self.kill()