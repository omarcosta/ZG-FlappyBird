import pygame
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

#     def drawing(self, window):
#         self.group.draw(window)
    
#     def animation(self, obj, frames, tick = 8, extension = "png"):
#         self.tick += 1

#         if self.tick >= tick: # A cada 8 frames (padrão) vai trocar a imagem
#             self.tick = 0
#             self.frame += 1

#         if self.frame >= frames:
#             self.frame = 1

#         # O nome das imagens devem seguir o padrão img1, img2, img3 ...
#         self.sprite.image = pygame.image.load(f'assets/sprites/{obj}{self.frame}.{extension}') 

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


# # class Bee(Obj):

#     def __init__(self, image, x, y):
#         super().__init__(image, x, y)

#         self.sound_pts = pygame.mixer.Sound("assets/sounds/score.ogg")
#         self.sound_colision = pygame.mixer.Sound("assets/sounds/bateu.ogg")
#         self.life = 3
#         self.pts = 0
    
#     def move_bee(self, event):
#         if event.type == pygame.MOUSEMOTION:
#             self.sprite.rect[0] = pygame.mouse.get_pos()[0] - 35 # Metade da largura da imagem
#             self.sprite.rect[1] = pygame.mouse.get_pos()[1] - 29 # Metade da altura da imagem

#     def colision(self, group, name):
#         colison = pygame.sprite.spritecollide(self.sprite, group, True)

#         if name == "Flower" and colison:
#             self.pts += 1
#             self.sound_pts.play()
            
#         elif name == "Spider" and colison:
#             self.life -= 1
#             self.sound_colision.play()

# class Text: 
    
#     def __init__(self, size, text, color = (255,255,255), fontfamily = "Arial bold"):
#         self.font = pygame.font.SysFont(fontfamily, size)
#         self.render = self.font.render(text, True,color)

#     def draw(self, window, x, y): 
#         window.blit(self.render, (x,y))
    
#     def update_text(self, text, color = (255,255,255)):
#         self.render = self.font.render(text, True, color)

    

