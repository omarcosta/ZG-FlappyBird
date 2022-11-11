import pygame
import random
from obj import Obj, Pipe, Coin

class Game:

    def __init__(self):
        
        # Grupos
        self.all_sprites = pygame.sprite.Group()
        self.tick = 0
        self.gap = 635 # Min 450 , Max 635

        # Cenário
        self.bg = Obj("assets/sky.png", 0, 0, self.all_sprites)
        self.bg2 = Obj("assets/sky.png", 360, 0, self.all_sprites)
        
        self.ground = Obj("assets/ground.png", 0, 480, self.all_sprites)
        self.ground2 = Obj("assets/ground.png", 360, 480, self.all_sprites)

        # self.pipe_dowm = Pipe("assets/pipe1.png", 360, 300, self.all_sprites)
        # self.pipe_up = Pipe("assets/pipe2.png", 360, -150, self.all_sprites)

        # Enemy
        # self.spider = Obj("assets/spider1.png", random.randrange(0,280), -10)
        # self.speed_spider = 8

        # Personagem 
        # self.bee = Bee("assets/bee1.png", 150, 550)
        
        # Pontos
        # self.flower = Obj("assets/florwer1.png", random.randrange(0,330), -100)
        # self.speed_flower = 5

        # Score 
        # self.score = Text(80, str(self.bee.pts))
        # self.lifes = Text(25, f'Lifes: {str(self.bee.life)}')

        # Controlador de cenas
        # self.change_scene = False
        pass

    def draw(self, window): 
        self.all_sprites.draw(window) # Desenha todas as imagens/obj do grupo
        # self.bg.group.draw(window)
        # self.bg2.group.draw(window)
        # self.spider.group.draw(window)
        # self.flower.group.draw(window)
        # self.bee.group.draw(window)
        # self.score.draw(window, 160, 12)
        # self.lifes.draw(window, 8, 12)
    
    def events(self): pass

    def update(self): 
        self.move_scenery() 
        self.all_sprites.update()
        self.spaw_pipe()
        # self.spider.animation("spider",5)
        # self.bee.animation("bee",5, 2)
        # self.flower.animation("florwer", 3)
        # self.move_spider()
        # self.move_flower()
        # self.bee.colision(self.flower.group, "Flower")
        # self.bee.colision(self.spider.group, "Spider")
        # self.score.update_text(str(self.bee.pts))
        # self.lifes.update_text(f'Lifes: {str(self.bee.life)}')
        # self.gameover()
        
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

    def spaw_pipe(self):

        self.tick += 1
        
        value_pipe1 = random.randrange(290, 435)
        value_pipe2 = value_pipe1 - self.gap 
        coin_position = value_pipe2+self.gap*(0.75+((635-self.gap)/185/10)) # Min 0,75, max 0,85

        if self.tick >= random.randrange(80,400): # minimo 60 max 150 
            self.tick = 0
            pipe_dowm = Pipe("assets/pipe1.png", 360, value_pipe1, self.all_sprites) # Y Min 290, max 435 
            pipe_up = Pipe("assets/pipe2.png", 360, value_pipe2, self.all_sprites) # Y max 355
            coin = Coin("assets/0.png", 384, coin_position, self.all_sprites)  #value_pipe1 - 120
            # Controle de dificuldade
            if self.gap < 450:
                self.gap = 450
            if self.gap > 450: 
                self.gap -= 2

    

        

    

    def gameover(self): pass
        # if self.bee.life <= 0:
        #     self.change_scene = True
        
