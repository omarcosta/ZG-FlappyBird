import pygame
import random
from obj import Obj, Pipe, Coin, Bird, Text

class Game:

    def __init__(self):
        
        # Grupos
        self.all_sprites = pygame.sprite.Group()
        self.coin_group = pygame.sprite.Group()
        self.pipe_group = pygame.sprite.Group()
        self.tick = 0
        self.gap = 635 # Min 500 , Max 635
        # Cenário
        self.bg = Obj("assets/sky.png", 0, 0, self.all_sprites)
        self.bg2 = Obj("assets/sky.png", 360, 0, self.all_sprites)
        self.ground = Obj("assets/ground.png", 0, 480, self.all_sprites)
        self.ground2 = Obj("assets/ground.png", 360, 480, self.all_sprites)
        # Personagem
        self.bird = Bird("assets/bird0.png", 150, 200, self.all_sprites)
        # Informações
        self.msg_game = Text(35,"Press ENTER to play again", (245,183,7))
        self.score = Text(100, "0")
        self.max_score = 0
        self.load_score()

        # Controlador de cenas
        self.change_scene = False        

    def draw(self, window): 
        self.all_sprites.draw(window) # Desenha todas as imagens/obj do grupo
        self.score.draw(window, 50, 20) 
        if self.bird.play == False:
            self.msg_game.draw(window, 30, 320)
    
    def events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.change_scene = True

    def update(self): 
        self.move_scenery() 
        self.all_sprites.update()
        if self.bird.play:
            self.spaw_pipe()
            self.bird.colision_coin(self.coin_group)
            self.bird.colision_pipes(self.pipe_group)
            self.score.update_text(str(self.bird.score))
        else:
            self.save_score()
            self.gameover()
            
        
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
        coin_position = value_pipe2+self.gap*(0.75+((635-self.gap)/135/10)) # Min 0,75, max 0,85
        if self.tick >= random.randrange(80,400): # minimo 60 max 150 
            self.tick = 0
            pipe_dowm = Pipe("assets/pipe1.png", 360, value_pipe1, self.all_sprites, self.pipe_group) # Y Min 290, max 435 
            pipe_up = Pipe("assets/pipe2.png", 360, value_pipe2, self.all_sprites, self.pipe_group) # Y max 355
            coin = Coin("assets/0.png", 384, coin_position, self.all_sprites, self.coin_group)  #value_pipe1 - 120
            # Controle de dificuldade
            if self.gap < 500:
                self.gap = 500
            if self.gap > 500: 
                self.gap -= 1

    def gameover(self):
        if self.bird.play == False:
            self.bird.image = pygame.image.load(f'assets/birdx.png')
            self.img_gameover = Obj("assets/gameover.png", 40, 150, self.all_sprites)

    def save_score(self): 
        if self.bird.score > self.max_score:
            self.max_score = self.bird.score
            with open("bin/score.txt", "w") as file:
                file.write(str(self.max_score))

    def load_score(self):
        file = open("bin/score.txt", "r")
        self.max_score = int(file.read())
        file.close()

    # def load_score(self):
    #     try:
    #         with open("bin/score.txt", "r", encoding = 'utf-8' ) as file:
    #             print(type(file.read()))
    #             x = file.read()
    #             print(x)
    #             if type(file.readline(0)) == int:
    #                 self.max_score = int(file.read())
    #                 print("Leu o arquivo : ", self.max_score)
    #             else:
    #                 self.max_score = 0
    #                 print("Erro ao ler")
    #     except FileNotFoundError:
    #         with open("bin/score.txt", "w", encoding = 'utf-8' ) as file:
    #             file.write(str(0))
    #             print("criou um novo pq nao leu")