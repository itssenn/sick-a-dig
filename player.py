from setting import *

class Player(pygame.sprite.Sprite):
    def __init__(self, position, groups, collision_sprites):
        super().__init__(groups)
        self.image = pygame.image.load("pics/drill.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect(center = position)
        self.hitbox_rect = self.rect.inflate(-20,0)

        #movement
        self.direction = pygame.Vector2()
        self.speed = 500
        self.collision_sprites = collision_sprites

        self.dig_cooldown = 500
        self.press = True
        self.level = 1

        self.fuel = 100
        self.fuel_rate = 5 - self.level

        self.inventory = {}

    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction

        if keys[pygame.K_SPACE] and self.press:
            self.dig()
            self.press = False
        elif not keys[pygame.K_SPACE]:
            self.press = True

    def dig(self):
        self.stack = 0
        for sprite in self.collision_sprites:
            if (
                sprite.is_diggable 
                and  
                sprite.rect.colliderect(self.hitbox_rect.inflate(5, 20)) 
            ):
                if sprite.ore_type:
                    if sum(list(self.inventory.values())) <= 30:
                        if sprite.take_damage():
                            if sprite.ore_type in self.inventory:
                                self.inventory[sprite.ore_type] += 1
                            else:
                                self.inventory[sprite.ore_type] = 1

                        print(self.inventory)
                    else:
                        print('Inventory is full!')


                # if self.fuel > 0:
                #     sprite.take_damage()
                #     self.fuel -= 1
                #     print(self.fuel)
                    
    def move(self, dt):
        self.hitbox_rect.x += self.direction.x * self.speed * dt
        self.collision('horizontal')
        self.hitbox_rect.y += self.direction.y * self.speed * dt
        self.collision('vertical')
        self.rect.center = self.hitbox_rect.center

    def collision(self, direction):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.hitbox_rect):
                if direction == 'horizontal':
                    if self.direction.x > 0: self.hitbox_rect.right = sprite.rect.left
                    if self.direction.x < 0: self.hitbox_rect.left = sprite.rect.right
                else:
                    if self.direction.y < 0: self.hitbox_rect.top = sprite.rect.bottom
                    if self.direction.y > 0: self.hitbox_rect.bottom = sprite.rect.top

    def update(self, dt):
        self.input()
        self.move(dt)

