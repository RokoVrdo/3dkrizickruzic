import pygame
import sys

pygame.font.init()
pygame.init()

font = pygame.font.SysFont("Constantia.ttf", 30)
ekran = pygame.display.set_mode((1200,800))
pygame.display.set_caption("Križić kružić")


krizickruzic_slika = pygame.image.load("KRIZICKRUZIC.png")
polje = pygame.image.load("polje.jpeg")
x = 920
y = 100
y2 = 250
y3 = 400
y4 = 550

text_input = "x"
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.x_pos = x
        self.y_pos = y
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
    def update(self):
        ekran.blit(self.image, self.rect)
    def checkForInput(self, position):
        if dogadjaj.type == pygame.MOUSEBUTTONDOWN:
		        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			        print("Button Press!")


button_surface = pygame.image.load("polje.jpeg")
button_surface = pygame.transform.scale(button_surface, (20, 20))



while True:

    for dogadjaj in pygame.event.get():
        if dogadjaj.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        for i in range(0,4):
            for j in range(0,4):
                gumb = Button(x + i*25, y + j*25, button_surface)
                gumb.checkForInput(pygame.mouse.get_pos())
                gumb.update()
        
        for i in range(0,4):
            for j in range(0,4):
                gumb2 = Button(x + i*25, y2 + j*25, button_surface)
                gumb2.checkForInput(pygame.mouse.get_pos())
                gumb2.update()

        for i in range(0,4):
            for j in range(0,4):
                gumb3 = Button(x + i*25, y3 + j*25, button_surface)
                gumb3.checkForInput(pygame.mouse.get_pos())
                gumb3.update()

        for i in range(0,4):
            for j in range(0,4):
                gumb4 = Button(x + i*25, y4 + j*25, button_surface)
                gumb4.checkForInput(pygame.mouse.get_pos())
                gumb4.update()

    ekran.blit(krizickruzic_slika,(200, 100) )               

    pygame.display.update()







