import pygame
from colors import Color # Optional import
from scene import Start
from game import Game

class Main:

    def __init__(self, sizex, sizey, title):

        pygame.init()
        pygame.mixer.init()

        self.window = pygame.display.set_mode([sizex, sizey])
        self.title = pygame.display.set_caption(title)
        self.icon = pygame.image.load('assets/ico.png')
        pygame.display.set_icon(self.icon)
        self.menu = Start()
        self.game = Game()
        self.height = sizey
        self.width = sizex 
        self.fps = pygame.time.Clock()
        self.loop = True

        # Cores
        self.color = Color()

    # Cenas / Telas
    def draw(self):
        self.window.fill(self.color.lavender)
        # Tela do Menu / Press Start 
        if not self.menu.change_scene:
            self.menu.draw(self.window)
            self.menu.update(self.game.max_score)
        # O jogo   
        elif not self.game.change_scene:
            self.game.draw(self.window)
            self.game.update()
            
        # Reset game
        else: 
            self.loop = False 

    def events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.loop = False
                pygame.QUIT()
            if not self.menu.change_scene:
                self.menu.events(events)
            else: 
                if self.game.bird.play == True:
                    self.game.bird.events(events)
                else:
                    self.game.events(events)

    def update(self):
        while self.loop:
            self.fps.tick(30) 
            self.events()
            pygame.display.update()
            self.draw()

# Set these variables
x = 360
y = 640
company = "Zodia Games"
gamename = "Flappy Bird"

# Not change 
run = True
while run:
    play = Main(x, y, f'{company} | {gamename}')
    play.update()
