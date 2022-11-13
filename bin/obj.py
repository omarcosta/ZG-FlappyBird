import pygame
# from colors import Color
speed_obj = 2

class Obj(pygame.sprite.Sprite): # Criar objetos sprites com imagens

    def __init__(self, img, x, y, *groups):
        super().__init__(*groups)
        
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect[0] = x
        self.rect[1] = y
        self.frame = 1
        self.tick = 0

class Pipe(Obj):

    def __init__(self, img, x, y, *groups):
        super().__init__(img, x, y, *groups)

    def update(self):
        self.move()

    def move(self):
        self.rect[0] -= speed_obj 
        if self.rect[0] <= -100:
            self.kill()

class Coin(Obj):
    def __init__(self, img, x, y, *groups):
        super().__init__(img, x, y, *groups)

        self.tick = 0

    def update(self, *args):
        self.move()
        self.anim()

    def move(self):
        self.rect[0] -= speed_obj
        if self.rect[0] <= -100:
            self.kill()

    def anim(self, repete = 6): 
        self.tick = (self.tick + 1) % repete
        self.image = pygame.image.load(f'assets/{str(self.tick)}.png')     

class Bird(Obj):

    def __init__(self, img, x, y, *groups):
        super().__init__(img, x, y, *groups)

        self.tick = 0
        self.speed = 4
        self.gravity = 1
        self.score = 0
        self.wing = pygame.mixer.Sound("assets/sounds/wing.ogg")
        self.point = pygame.mixer.Sound("assets/sounds/point.ogg")
        self.hit = pygame.mixer.Sound("assets/sounds/hit.ogg")
        self.play = True

    def update(self, *args):
        self.move()
        self.anim()
    
    def move(self):
 
        self.speed += self.gravity
        self.rect[1] += self.speed

        if self.speed >= 10:
            self.speed = 10        

        if self.rect[1] >= 430:
            self.rect[1] = 430
            
        elif self.rect[1] <= 0:
            self.rect[1] = 0
            self.speed = 4       

    def anim(self, repete = 4): 
        self.tick = (self.tick + 1) % repete
        self.image = pygame.image.load(f'assets/bird{str(self.tick)}.png')

    def colision_pipes(self, group): 
        col = pygame.sprite.spritecollide(self, group, False)
        if col:
            self.play = False
            self.hit.play()

    def colision_coin(self, group): 
        col = pygame.sprite.spritecollide(self, group, True)
        if col:
            self.score += 1
            self.point.play()
    
    def events(self, event):
        self.touch = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and self.touch == False:
                    self.speed -= 20
                    self.wing.play()
                    self.touch = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                self.touch = False

class Text: 
    
    def __init__(self, size, text, color = (255,255,255)):
        self.font = pygame.font.Font("assets/font/font.ttf", size)
        self.render = self.font.render(text, True, color)

    def draw(self, window, x, y): 
        window.blit(self.render, (x,y))
    
    def update_text(self, text, color = (255,255,255)):
        self.render = self.font.render(text, True, color)

    

