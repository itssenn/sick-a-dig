from setting import *

class Sprite(pygame.sprite.Sprite):
    def __init__(self, position, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = position)

class CollisionSprite(pygame.sprite.Sprite):
    def __init__(self, position, surf, groups, is_diggable=False):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = position)
        self.is_diggable = is_diggable 

class Digger(pygame.sprite.Sprite):
    def __init__(self, surf, pos, direction, groups):
        super().__init__(groups)
        self. image = surf
        self.rect = self.image.get_rect(center = pos)

class Dirt(pygame.sprite.Sprite):
    def __init__(self, pos, frames, groups, player, collision_sprites):
        super().__init__(groups)
        self.player = player

        self.frames, self.frame_index = frames, 0  

        self.rect = self.image.get_rect(center = pos)
        self.hitbox_rect = self.rect.inflate(-20, -40)
        self.colision_sprites = collision_sprites
        self.direction = pygame.Vector2()
