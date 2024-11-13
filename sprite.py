from setting import *

class Sprite(pygame.sprite.Sprite):
    def __init__(self, position, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = position)
    def interactable(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_e]:
            print('interacted')

class CollisionSprite(pygame.sprite.Sprite):
    def __init__(self, position, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.is_diggable = False
        self.rect = self.image.get_rect(topleft = position)

class Block(pygame.sprite.Sprite):
    def __init__(self, position, surf, groups, ore_type, is_diggable=False):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = position)
        self.is_diggable = is_diggable

        self.Ore = {'glass':1, 'dirt':1, 'stone':3, 'coal':4, 'diamond':5, 'ruby':5}

        self.ore_type = ore_type

        self.block_health = self.Ore[self.ore_type]

    def take_damage(self,multiplier):
        if self.is_diggable:
            self.block_health -= 1 * multiplier

            if self.block_health <= 0:
                self.kill()
                return True
            
