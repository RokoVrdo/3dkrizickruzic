
from turtle import pos
import pygame, sys


class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)





pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

SCREEN.fill((65,105,225))

def get_font(size): 
    return pygame.font.Font("font2.otf", size)
def igrači_font(size): 
    return pygame.font.Font(None, size)
xo_font = pygame.font.SysFont("monospace",150)


clock = pygame.time.Clock()



def play():
    while True:
        
        SCREEN.fill("black")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
    
def scoreboard():
    while True:
        SCOREBOARD_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        SCOREBOARD_NATRAG = Button(image=None, pos=(640, 500), 
                            text_input="Vrati se na Main Menu", font=get_font(36), base_color="Black", hovering_color="Green")

        SCOREBOARD_NATRAG.changeColor(SCOREBOARD_MOUSE_POS)
        SCOREBOARD_NATRAG.update(SCREEN)

        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SCOREBOARD_NATRAG.checkForInput(SCOREBOARD_MOUSE_POS):
                    main_menu()

        pygame.display.update()



def main_menu():
    while True:
        SCREEN.fill((65,105,225))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        
        IGRAČ1_TEKST =  Button(image=pygame.image.load("Play.png"), pos=(160, 250), 
                            text_input="Igrač 1", font=igrači_font(36), base_color="#d7fcd4", hovering_color="White")

        IGRAČ2_TEKST = Button(image=pygame.image.load("Play.png"), pos=(1120, 250), 
                            text_input="Igrač 2", font=igrači_font(36), base_color="#d7fcd4", hovering_color="White")


        PLAY_BUTTON = Button(image=pygame.image.load("Play.png"), pos=(640, 250), 
                            text_input="IGRAJ", font=get_font(60), base_color="#d7fcd4", hovering_color="White")
        SCOREBOARD_BUTTON = Button(image=pygame.image.load("Scoreboard.png"), pos=(640, 400), 
                            text_input="SCOREBOARD", font=get_font(60), base_color="#d7fcd4", hovering_color="White")
        IZLAZ_BUTTON = Button(image=pygame.image.load("Quit.png"), pos=(640, 550), 
                            text_input="IZLAZ", font=get_font(60), base_color="#d7fcd4", hovering_color="White")


        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, SCOREBOARD_BUTTON, IZLAZ_BUTTON, IGRAČ1_TEKST, IGRAČ2_TEKST]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        SCREEN.blit((xo_font.render("x", 1, (255, 255, 255))), (120, 300))
        SCREEN.blit((xo_font.render("o", 1, (255, 255, 255))), (1080, 300))

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if SCOREBOARD_BUTTON.checkForInput(MENU_MOUSE_POS):
                    scoreboard()

                if IZLAZ_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()

