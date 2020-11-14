import pygame

pygame.init()

WIDTH, HEIGHT = 1920, 1080
pygame.display.set_caption("Online Xylophone")

BLACK = (0, 0, 0)
RED = (255, 0, 0)
UNSATRED = (255, 128, 128)
DARKRED = (128, 0, 0)
ORANGE = (255, 165, 0)
UNSATORANGE = (255, 255, 128)
DARKORANGE = (128, 37, 0)
YELLOW = (255, 255, 0)
UNSATYELLOW = (255, 255, 128)
DARKYELLOW = (128, 128, 0)
GREEN = (0, 255, 0)
UNSATGREEN = (128, 255, 128)
DARK_GREEN = (0, 128, 0)
DARKGREEN = (124, 252, 0)
UNSATDARKGREEN = (252, 255, 128)
DARKDARKGREEN = (0, 124, 0)
CYAN = (0, 255, 255)
UNSATCYAN = (128, 255, 255)
DARKCYAN = (0, 128, 128)
PURPLE = (160, 32, 240)
UNSATPURPLE = (255, 160, 255)
DARKPURPLE = (32, 0, 112)
WHITE = (255, 255, 255)

STDFONT = pygame.font.SysFont("comicsans", 100)

class Block:
    WIDTH = 125
    def __init__(self, x, y, height, note, color, hoveredColor, clickedColor, font, text, textCol):
        self.x = x
        self.y = y
        self.height = height
        self.note = note
        self.color = color
        self.hoveredColor = hoveredColor
        self.clickedColor = clickedColor
        self.font = font
        self.textCol = textCol
        self.text = self.font.render(text, 1, self.textCol)
        self.pos = (self.x - self.text.get_width() // 2, self.y - self.text.get_height() // 2)
        self.temp = self.color

    def Draw(self, display):
        pygame.draw.rect(display, self.color, (self.x - self.WIDTH // 2, self.y - self.height // 2, self.WIDTH, self.height), 0)
        display.blit(self.text, self.pos)

    def PlayBlock(self, mousePos, events):
        if mousePos[0] >= self.x - self.WIDTH // 2 and mousePos[0] <= self.x + self.WIDTH // 2 and mousePos[1] >= self.y - self.height // 2 and mousePos[1] <= self.y + self.height // 2:
            self.color = self.hoveredColor
        else:
            self.color = self.temp
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mousePos[0] >= self.x - self.WIDTH // 2 and mousePos[0] <= self.x + self.WIDTH // 2 and mousePos[1] >= self.y - self.height // 2 and mousePos[1] <= self.y + self.height // 2:
                    pygame.mixer.music.load(".\\mp3-files\\" + (self.note) + ".mp3")#For some reason, python's .\foldername\file.filetype doesn't work, so I have to hard code it.
                    #But, I can't give you my real path, so I just put it like that.
                    pygame.mixer.music.set_volume(0.5)
                    self.color = self.clickedColor
                    self.color = self.temp
                    pygame.mixer.music.play()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    if self.note == "C":
                        pygame.mixer.music.load(".\\mp3-files\\" + (self.note) + ".mp3")#For some reason, python's .\foldername\file.filetype doesn't work, so I have to hard code it.
                        #But, I can't give you my real path, so I just put it like that.
                        pygame.mixer.music.set_volume(0.5)
                        self.color = self.clickedColor
                        pygame.display.update()
                        pygame.mixer.music.play()
                if event.key == pygame.K_s or event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    if self.note == "D":
                        pygame.mixer.music.load(".\\mp3-files\\" + (self.note) + ".mp3")#For some reason, python's .\foldername\file.filetype doesn't work, so I have to hard code it.
                        #But, I can't give you my real path, so I just put it like that.
                        pygame.mixer.music.set_volume(0.5)
                        self.color = self.clickedColor
                        pygame.display.update()
                        pygame.mixer.music.play()
                if event.key == pygame.K_d or event.key == pygame.K_3 or event.key == pygame.K_KP3:
                    if self.note == "E":
                        pygame.mixer.music.load(".\\mp3-files\\" + (self.note) + ".mp3")#For some reason, python's .\foldername\file.filetype doesn't work, so I have to hard code it.
                        #But, I can't give you my real path, so I just put it like that.
                        pygame.mixer.music.set_volume(0.5)
                        self.color = self.clickedColor
                        pygame.display.update()
                        pygame.mixer.music.play()
                if event.key == pygame.K_f or event.key == pygame.K_4 or event.key == pygame.K_KP4:
                    if self.note == "F":
                        pygame.mixer.music.load(".\\mp3-files\\" + (self.note) + ".mp3")#For some reason, python's .\foldername\file.filetype doesn't work, so I have to hard code it.
                        #But, I can't give you my real path, so I just put it like that.
                        pygame.mixer.music.set_volume(0.5)
                        self.color = self.clickedColor
                        pygame.display.update()
                        pygame.mixer.music.play()
                if event.key == pygame.K_g or event.key == pygame.K_5 or event.key == pygame.K_KP5:
                    if self.note == "G":
                        pygame.mixer.music.load(".\\mp3-files\\" + (self.note) + ".mp3")#For some reason, python's .\foldername\file.filetype doesn't work, so I have to hard code it.
                        #But, I can't give you my real path, so I just put it like that.
                        pygame.mixer.music.set_volume(0.5)
                        self.color = self.clickedColor
                        pygame.display.update()
                        pygame.mixer.music.play()
                if event.key == pygame.K_h or event.key == pygame.K_6 or event.key == pygame.K_KP6:
                    if self.note == "A":
                        pygame.mixer.music.load(".\\mp3-files\\" + (self.note) + ".mp3")#For some reason, python's .\foldername\file.filetype doesn't work, so I have to hard code it.
                        #But, I can't give you my real path, so I just put it like that.
                        pygame.mixer.music.set_volume(0.5)
                        self.color = self.clickedColor
                        pygame.display.update()
                        pygame.mixer.music.play()
                if event.key == pygame.K_j or event.key == pygame.K_7 or event.key == pygame.K_KP7:
                    if self.note == "B":
                        pygame.mixer.music.load(".\\mp3-files\\" + (self.note) + ".mp3")#For some reason, python's .\foldername\file.filetype doesn't work, so I have to hard code it.
                        #But, I can't give you my real path, so I just put it like that.
                        pygame.mixer.music.set_volume(0.5)
                        self.color = self.clickedColor
                        pygame.display.update()
                        pygame.mixer.music.play()
                if event.key == pygame.K_k or event.key == pygame.K_8 or event.key == pygame.K_KP8:
                    if self.note == "C\'":
                        pygame.mixer.music.load(".\\mp3-files\\" + (self.note) + ".mp3")#For some reason, python's .\foldername\file.filetype doesn't work, so I have to hard code it.
                        #But, I can't give you my real path, so I just put it like that.
                        pygame.mixer.music.set_volume(0.5)
                        self.color = self.clickedColor
                        pygame.display.update()
                        pygame.mixer.music.play()


def Main():
    DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    FPS = 60
    clock = pygame.time.Clock()
    c = Block(175, HEIGHT // 2, 750, "C", RED, UNSATRED, DARKRED, STDFONT, "C", BLACK)
    d = Block(400, HEIGHT // 2, 700, "D", ORANGE, UNSATORANGE, DARKORANGE, STDFONT, "D", BLACK)
    e = Block(625, HEIGHT // 2, 650, "E", YELLOW, UNSATYELLOW, DARKYELLOW, STDFONT, "E", BLACK)
    f = Block(850, HEIGHT // 2, 600, "F", GREEN, UNSATGREEN, DARK_GREEN, STDFONT, "F", BLACK)
    g = Block(1075, HEIGHT // 2, 550, "G", DARKGREEN, UNSATDARKGREEN, DARKDARKGREEN, STDFONT, "G", BLACK)
    a = Block(1300, HEIGHT // 2, 500, "A", CYAN, UNSATCYAN, DARKCYAN, STDFONT, "A", BLACK)
    b = Block(1525, HEIGHT // 2, 450, "B", PURPLE, UNSATPURPLE, DARKPURPLE, STDFONT, "B", BLACK)
    upperC = Block(1750, HEIGHT // 2, 400, "C\'", RED, UNSATRED, DARKRED, STDFONT, "C\'", BLACK)

    while True:
        clock.tick(FPS)
        mousePos = pygame.mouse.get_pos()
        DISPLAY.fill(WHITE)
        c.Draw(DISPLAY)
        d.Draw(DISPLAY)
        e.Draw(DISPLAY)
        f.Draw(DISPLAY)
        g.Draw(DISPLAY)
        a.Draw(DISPLAY)
        b.Draw(DISPLAY)
        upperC.Draw(DISPLAY)
        events = pygame.event.get()
        c.PlayBlock(mousePos, events)
        d.PlayBlock(mousePos, events)
        e.PlayBlock(mousePos, events)
        f.PlayBlock(mousePos, events)
        g.PlayBlock(mousePos, events)
        a.PlayBlock(mousePos, events)
        b.PlayBlock(mousePos, events)
        upperC.PlayBlock(mousePos, events)

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.VIDEORESIZE:
                DISPLAY = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
        pygame.display.update()

Main()