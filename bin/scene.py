import pygame
from obj import Obj, Text

class Start():

    def __init__(self): 
        self.change_scene = False
        self.all_sprites = pygame.sprite.Group()
        self.bg = Obj("assets/sky.png", 0, 0, self.all_sprites)
        self.bg2 = Obj("assets/sky.png", 360, 0, self.all_sprites)
        self.ground = Obj("assets/ground.png", 0, 480, self.all_sprites)
        self.ground2 = Obj("assets/ground.png", 360, 480, self.all_sprites)
        self.ready = Obj("assets/getready.png", 60,100, self.all_sprites)
        self.table = Obj("assets/score.png", 20, 250, self.all_sprites)
        self.button = Obj("assets/go.png", 100 , 530, self.all_sprites)
        self.txt_score = Text(80,"0") 

    def draw(self, window):
        self.all_sprites.draw(window)
        self.move_scenery()
        self.txt_score.draw(window, 140, 320)

    def events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                self.change_scene = True
        if event.type == pygame.MOUSEBUTTONUP:
            if self.button.rect.collidepoint(pygame.mouse.get_pos()): # 2 eventos, clique do mouse na sprite que representa o botão
                self.change_scene = True

    def update(self, text = 0):
        self.txt_score.update_text(str(text))

    def move_scenery(self): 

        self.bg.rect[0] -= 1
        self.bg2.rect[0] -= 1
        self.ground.rect[0] -= 2
        self.ground2.rect[0] -= 2
        if self.bg.rect[0] <= -359: 
            self.bg.rect[0] = 0
        if self.ground.rect[0] <= -360:
            self.ground.rect[0] = 0
        if self.bg2.rect[0] <= 0:
            self.bg2.rect[0] = 359
        if self.ground2.rect[0] <= 0:
            self.ground2.rect[0] = 360