import pygame
from random import randint
import pickle

class Pixel:
    def __init__(self, x, y, size, color = None):
        self.x = x
        self.y = y
        self.size = size
        if color is None:
            self.color = (0, 0, 0)
        else:
            self.color = color
        self.rect = pygame.Rect(x + .5, y + .5, size - 1, size - 1)

    def draw(self, scr):
        pygame.draw.rect(scr, self.color, self.rect)

class Screen:
    def __init__(self, rows, cols, pixel_size):
        pygame.display.set_caption("Pixel Art")
        self.scr = pygame.display.set_mode((cols * pixel_size, rows * pixel_size))
        self.clock = pygame.time.Clock()
        self.pixel_size = pixel_size
        self.pixels = []
        self.pen_color = (255, 255, 255)
        for i in range(rows):
            self.pixels.append([])
            for j in range(cols):
                y = i * pixel_size
                x = j * pixel_size
                self.pixels[i].append(Pixel(x, y, pixel_size))
        


    def run(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        print("red")
                        self.pen_color = (255, 0, 0)
                    if event.key == pygame.K_2:
                        print("green")
                        self.pen_color = (0, 255, 0)
                    if event.key == pygame.K_3:
                        print("blue")
                        self.pen_color = (0, 0, 255)
                    if event.key == pygame.K_4:
                        print("magenta")
                        self.pen_color = (255, 0, 255)
                    if event.key == pygame.K_5:
                        print("yellow")
                        self.pen_color = (255, 255, 0)
                    if event.key == pygame.K_6:
                        print("cyan")
                        self.pen_color = (0, 255, 255)
                    if event.key == pygame.K_c:
                        col = []
                        col.append(int(input("Red value: ")))
                        col.append(int(input("Green value: ")))
                        col.append(int(input("Blue value: ")))
                        self.pen_color = tuple(col)
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for i in self.pixels:
                        for j in i:
                            if j.rect.collidepoint(event.pos):
                                j.color = self.pen_color
            
            
            self.scr.fill((128, 128, 128))
            for r in self.pixels:
                for c in r:
                    c.draw(self.scr)

            pygame.display.update()
            self.clock.tick(60)
        pygame.image.save(self.scr, "screenshot.jpeg")
        pygame.quit()


s = Screen(32, 32, 20)
s.run()

