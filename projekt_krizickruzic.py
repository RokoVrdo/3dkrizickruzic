from turtle import position
import pygame
import sys

pygame.init()
pygame.font.init()

ekran = pygame.display.set_mode((800, 800))
slika_x = pygame.image.load("x.png")
slika_O = pygame.image.load("o.png")
slika_polje = pygame.image.load("krizickruzic_template.png")
slika_tabela = pygame.image.load("KRIZICKRUZIC.png")
font = pygame.font.SysFont("Constantia.ttf", 30)

tekst = ""

text_surface = font.render(tekst, True, "Purple")
slika_tabela = pygame.transform.scale(slika_tabela, (300, 650))

polje = int((650/19))
x=int(500)
y=int(75)

promjena = 0

ploča1 = [[None]*4, [None]*4, [None]*4, [None]*4]
ploča2 = [[None]*4, [None]*4, [None]*4, [None]*4]
ploča3 = [[None]*4, [None]*4, [None]*4, [None]*4]
ploča4 = [[None]*4, [None]*4, [None]*4, [None]*4]



igra = True
while igra:
    
    for dogadjaj in pygame.event.get():
        if dogadjaj.type == pygame.QUIT:
            pygame.quit() 
            sys.exit()
        ekran.blit(slika_polje, (x,y))
        if dogadjaj.type == pygame.MOUSEBUTTONDOWN:            
            pozicija = pygame.mouse.get_pos()
            if promjena == 0:
                ekran.blit(slika_x, pozicija)
                promjena = 1
            else:
                ekran.blit( slika_O, pozicija)
                promjena = 0

            for i in range (0,4):
                if promjena == 0:
                    tekst = "X"
                    promjena = 1
                else:
                    tekst = "O"
                    promjena = 0
                if pozicija[0] in range ((x + polje*i), (x+polje*(i+1))) and pozicija[1] in range (y, y+polje):
                    ploča1[0][i] = tekst

            for i in range (0,4):
                if promjena == 0:
                    tekst = "X"
                    promjena = 1
                else:
                    tekst = "O"
                    promjena = 0
                if pozicija[0] in range ((x + polje*i), (x+polje*(i+1))) and pozicija[1] in range (y + polje*1, y+polje*2):
                    ploča1[1][i] = tekst
                    ekran.blit(text_surface, (x + polje*i + 5, y + polje*1 + 5)) 

            for i in range (0,4):
                if promjena == 0:
                    tekst = "X"
                    promjena = 1
                else:
                    tekst = "O"
                    promjena = 0
                if pozicija[0] in range ((x + polje*i), (x+polje*(i+1))) and pozicija[1] in range (y + polje*2, y+polje*3):
                    ploča1[2][i] = tekst
                    ekran.blit(text_surface, (x + polje*i + 5, y + polje*2 + 5))

            for i in range (0,4):
                if promjena == 0:
                    tekst = "X"
                    promjena = 1
                else:
                    tekst = "O"
                    promjena = 0
                if pozicija[0] in range ((x + polje*i), (x+polje*(i+1))) and pozicija[1] in range (y + polje*3, y+polje*4):
                    ploča1[3][i] = tekst
                    ekran.blit(text_surface, (x + polje*i + 5, y + polje*3 + 5))     

            for i in range (0,4):
                if promjena == 0:
                    tekst = "X"
                    promjena = 1
                else:
                    tekst = "O"
                    promjena = 0
                if pozicija[0] in range ((x + polje*i), (x+polje*(i+1))) and pozicija[1] in range (y + polje*5, y+polje*6):
                    ploča2[0][i] = tekst
                    ekran.blit(text_surface, (x + polje*i + 5, y + polje*5 + 5))

            for i in range (0,4):
                if promjena == 0:
                    tekst = "X"
                    promjena = 1
                else:
                    tekst = "O"
                    promjena = 0
                if pozicija[0] in range ((x + polje*i), (x+polje*(i+1))) and pozicija[1] in range (y + polje*6, y+polje*7):
                    ploča2[1][i] = tekst
                    ekran.blit(text_surface, (x + polje*i + 5, y + polje*6 + 5))  

            for i in range (0,4):
                if promjena == 0:
                    tekst = "X"
                    promjena = 1
                else:
                    tekst = "O"
                    promjena = 0
                if pozicija[0] in range ((x + polje*i), (x+polje*(i+1))) and pozicija[1] in range (y + polje*7, y+polje*8):
                    ploča2[2][i] = tekst
                    ekran.blit(text_surface, (x + polje*i + 5, y + polje*7 + 5))

            for i in range (0,4):
                if promjena == 0:
                    tekst = "X"
                    promjena = 1
                else:
                    tekst = "O"
                    promjena = 0
                if pozicija[0] in range ((x + polje*i), (x+polje*(i+1))) and pozicija[1] in range (y + polje*8, y+polje*9):
                    ploča2[3][i] = tekst
                    ekran.blit(text_surface, (x + polje*i + 5, y + polje*8 + 5)) 

            for i in range (0,4):
                if promjena == 0:
                    tekst = "X"
                    promjena = 1
                else:
                    tekst = "O"
                    promjena = 0
                if pozicija[0] in range ((x + polje*i), (x+polje*(i+1))) and pozicija[1] in range (y + polje*10, y+polje*11):
                    ploča3[0][i] = tekst
                    ekran.blit(text_surface, (x + polje*i + 5, y + polje*10 + 5))

            for i in range (0,4):
                if promjena == 0:
                    tekst = "X"
                    promjena = 1
                else:
                    tekst = "O"
                    promjena = 0
                if pozicija[0] in range ((x + polje*i), (x+polje*(i+1))) and pozicija[1] in range (y + polje*11, y+polje*12):
                    ploča3[1][i] = tekst
                    ekran.blit(text_surface, (x + polje*i + 5, y + polje*11 + 5))  

            for i in range (0,4):
                if promjena == 0:
                    tekst = "X"
                    promjena = 1
                else:
                    tekst = "O"
                    promjena = 0
                if pozicija[0] in range ((x + polje*i), (x+polje*(i+1))) and pozicija[1] in range (y + polje*12, y+polje*13):
                    ploča3[2][i] = tekst
                    ekran.blit(text_surface, (x + polje*i + 5, y + polje*12 + 5))

            for i in range (0,4):
                if promjena == 0:
                    tekst = "X"
                    promjena = 1
                else:
                    tekst = "O"
                    promjena = 0
                if pozicija[0] in range ((x + polje*i), (x+polje*(i+1))) and pozicija[1] in range (y + polje*13, y+polje*14):
                    ploča3[3][i] = tekst
                    ekran.blit(text_surface, (x + polje*i + 5, y + polje*13 + 5))  

            for i in range (0,4):
                if promjena == 0:
                    tekst = "X"
                    promjena = 1
                else:
                    tekst = "O"
                    promjena = 0
                if pozicija[0] in range ((x + polje*i), (x+polje*(i+1))) and pozicija[1] in range (y + polje*15, y+polje*16):
                    ploča4[0][i] = tekst
                    ekran.blit(text_surface, (x + polje*i + 5, y + polje*15 + 5))

            for i in range (0,4):
                if promjena == 0:
                    tekst = "X"
                    promjena = 1
                else:
                    tekst = "O"
                    promjena = 0
                if pozicija[0] in range ((x + polje*i), (x+polje*(i+1))) and pozicija[1] in range (y + polje*16, y+polje*17):
                    ploča4[1][i] = tekst
                    ekran.blit(text_surface, (x + polje*i + 5, y + polje*16 + 5)) 

            for i in range (0,4):
                if promjena == 0:
                    tekst = "X"
                    promjena = 1
                else:
                    tekst = "O"
                    promjena = 0
                if pozicija[0] in range ((x + polje*i), (x+polje*(i+1))) and pozicija[1] in range (y + polje*17, y+polje*18):
                    ploča4[2][i] = tekst
                    ekran.blit(text_surface, (x + polje*i + 5, y + polje*17 + 5))
                    
            for i in range (0,4):
                if promjena == 0:
                    tekst = "X"
                    promjena = 1
                else:
                    tekst = "O"
                    promjena = 0
                if pozicija[0] in range ((x + polje*i), (x+polje*(i+1))) and pozicija[1] in range (y + polje*18, y+polje*19):
                    ploča4[3][i] = tekst
                    ekran.blit(text_surface, (x + polje*i + 5, y + polje*18 + 5))                             

            print(f"{ploča1} \n \n {ploča2} \n \n {ploča3} \n \n {ploča4} \n \n")         

    ekran.blit(slika_tabela, (100, 75))
    
    pygame.display.update()    



