from ast import In
from turtle import position
import pygame
import sys

pygame.init()
pygame.font.init()

ekran = pygame.display.set_mode((800, 800))
slika_polje = pygame.image.load("krizickruzic_template.png")
slika_x = pygame.image.load("x.png")
#slika_x_kopija = slika_x.copy()
slika_O = pygame.image.load("o.png")
#slika_O_kopija = slika_O.copy()
#slika_polje_kopija = slika_polje.copy()
slika_tabela = pygame.image.load("KRIZICKRUZIC.png")
font = pygame.font.SysFont("Constantia.ttf", 30)

tekst = ""
krivi_tekst = "Krivo područje si stisnuo"

krivo = font.render(krivi_tekst, True, "Purple")
krivo = pygame.transform.scale(krivo,(100,100))

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
            for i in range (0,4):               
                if pozicija[0] in range ((x + polje*i), (x+polje*(i+1))) and pozicija[1] in range (y, y+polje):
                    if promjena == 0:
                        tekst = "X" 
                        slika = slika_x                 
                        promjena = 1
                    else:
                        tekst = "O"  
                        slika = slika_O                 
                        promjena = 0
                    ploča1[0][i] = tekst
                    ekran.blit(slika, pozicija)

            for i in range (0,4):
                if pozicija[0] in range ((x + polje*i), (x+polje*(i+1))) and pozicija[1] in range (y + polje*1, y+polje*2):
                    if promjena == 0:
                        tekst = "X" 
                        slika = slika_x                 
                        promjena = 1
                    else:
                        tekst = "O"  
                        slika = slika_O                 
                        promjena = 0
                    ploča1[1][i] = tekst
                    ekran.blit(slika, pozicija)

            for i in range (0,4):
                if pozicija[0] in range ((x + polje*i), (x+polje*(i+1))) and pozicija[1] in range (y + polje*2, y+polje*3):
                    if promjena == 0:
                        tekst = "X" 
                        slika = slika_x                 
                        promjena = 1
                    else:
                        tekst = "O"  
                        slika = slika_O                 
                        promjena = 0
                    ploča1[2][i] = tekst
                    ekran.blit(slika, pozicija)
                    
            for i in range (0,4):
                if pozicija[0] in range ((x + polje*i), (x+polje*(i+1))) and pozicija[1] in range (y + polje*3, y+polje*4):
                    if promjena == 0:
                        tekst = "X" 
                        slika = slika_x                 
                        promjena = 1
                    else:
                        tekst = "O"  
                        slika = slika_O                 
                        promjena = 0
                    ploča1[3][i] = tekst
                    ekran.blit(slika, pozicija)
                    
            for i in range (0,4):
                if pozicija[0] in range ((x + polje*i), (x+polje*(i+1))) and pozicija[1] in range (y + polje*5, y+polje*6):
                    if promjena == 0:
                        tekst = "X" 
                        slika = slika_x                 
                        promjena = 1
                    else:
                        tekst = "O"  
                        slika = slika_O                 
                        promjena = 0
                    ploča2[0][i] = tekst
                    ekran.blit(slika, pozicija)
                    
            for i in range (0,4):
                if pozicija[0] in range ((x + polje*i), (x+polje*(i+1))) and pozicija[1] in range (y + polje*6, y+polje*7):
                    if promjena == 0:
                        tekst = "X" 
                        slika = slika_x                 
                        promjena = 1
                    else:
                        tekst = "O"  
                        slika = slika_O                 
                        promjena = 0
                    ploča2[1][i] = tekst
                    ekran.blit(slika, pozicija)
         
            for i in range (0,4):
                if pozicija[0] in range ((x + polje*i), (x+polje*(i+1))) and pozicija[1] in range (y + polje*7, y+polje*8):
                    if promjena == 0:
                        tekst = "X" 
                        slika = slika_x                 
                        promjena = 1
                    else:
                        tekst = "O"  
                        slika = slika_O                 
                        promjena = 0
                    ploča2[2][i] = tekst
                    ekran.blit(slika, pozicija)

            for i in range (0,4):
                if pozicija[0] in range ((x + polje*i), (x+polje*(i+1))) and pozicija[1] in range (y + polje*8, y+polje*9):
                    if promjena == 0:
                        tekst = "X" 
                        slika = slika_x                 
                    else:
                        tekst = "O"  
                        slika = slika_O                 
                        promjena = 0
                    ploča2[3][i] = tekst
                    ekran.blit(slika, pozicija)
                    
            for i in range (0,4):
                if pozicija[0] in range ((x + polje*i), (x+polje*(i+1))) and pozicija[1] in range (y + polje*10, y+polje*11):
                    if promjena == 0:
                        tekst = "X" 
                        slika = slika_x                 
                        promjena = 1
                    else:
                        tekst = "O"  
                        slika = slika_O                 
                        promjena = 0
                    ploča3[0][i] = tekst
                    ekran.blit(slika, pozicija)
                    
            for i in range (0,4):
                if pozicija[0] in range ((x + polje*i), (x+polje*(i+1))) and pozicija[1] in range (y + polje*11, y+polje*12):
                    if promjena == 0:
                        tekst = "X" 
                        slika = slika_x                 
                        promjena = 1
                    else:
                        tekst = "O"  
                        slika = slika_O                 
                        promjena = 0
                    ploča3[1][i] = tekst
                    ekran.blit(slika, pozicija)

            for i in range (0,4):
                if pozicija[0] in range ((x + polje*i), (x+polje*(i+1))) and pozicija[1] in range (y + polje*12, y+polje*13):
                    if promjena == 0:
                        tekst = "X" 
                        slika = slika_x                 
                        promjena = 1
                    else:
                        tekst = "O"  
                        slika = slika_O                 
                        promjena = 0
                    ploča3[2][i] = tekst
                    ekran.blit(slika, pozicija)

            for i in range (0,4):
                if pozicija[0] in range ((x + polje*i), (x+polje*(i+1))) and pozicija[1] in range (y + polje*13, y+polje*14):
                    if promjena == 0:
                        tekst = "X" 
                        slika = slika_x                 
                        promjena = 1
                    else:
                        tekst = "O"  
                        slika = slika_O                 
                        promjena = 0
                    ploča3[3][i] = tekst
                    ekran.blit(slika, pozicija)

            for i in range (0,4):
                if pozicija[0] in range ((x + polje*i), (x+polje*(i+1))) and pozicija[1] in range (y + polje*15, y+polje*16):
                    if promjena == 0:
                        tekst = "X" 
                        slika = slika_x                 
                        promjena = 1
                    else:
                        tekst = "O"  
                        slika = slika_O                 
                        promjena = 0
                    ploča4[0][i] = tekst
                    ekran.blit(slika, pozicija)

            for i in range (0,4):
                if pozicija[0] in range ((x + polje*i), (x+polje*(i+1))) and pozicija[1] in range (y + polje*16, y+polje*17):
                    if promjena == 0:
                        tekst = "X" 
                        slika = slika_x                 
                        promjena = 1
                    else:
                        tekst = "O"  
                        slika = slika_O                 
                        promjena = 0
                    ploča4[1][i] = tekst
                    ekran.blit(slika, pozicija)

            for i in range (0,4):
                if pozicija[0] in range ((x + polje*i), (x+polje*(i+1))) and pozicija[1] in range (y + polje*17, y+polje*18):
                    if promjena == 0:
                        tekst = "X" 
                        slika = slika_x                 
                        promjena = 1
                    else:
                        tekst = "O"  
                        slika = slika_O                 
                        promjena = 0
                    ploča4[2][i] = tekst
                    ekran.blit(slika, pozicija)
                    
            for i in range (0,4):
                if pozicija[0] in range ((x + polje*i), (x+polje*(i+1))) and pozicija[1] in range (y + polje*18, y+polje*19):
                    if promjena == 0:
                        tekst = "X" 
                        slika = slika_x                 
                        promjena = 1
                    else:
                        tekst = "O"  
                        slika = slika_O                 
                        promjena = 0
                    ploča4[3][i] = tekst
                    ekran.blit(slika, pozicija)
            if pozicija[0] not in range (x, x+polje*4) or pozicija[1] not in range (y, y+polje*19):
                ekran.blit(krivo, (400,400))
                
            print(f"{ploča1} \n \n {ploča2} \n \n {ploča3} \n \n {ploča4} \n \n")         
    
    ekran.blit(slika_tabela, (100, 75))
    
    pygame.display.update()    
