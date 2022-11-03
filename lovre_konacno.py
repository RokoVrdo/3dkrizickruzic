from turtle import position
import pygame
import sys
from pygame.locals import *

pygame.init()
pygame.font.init()

ekran = pygame.display.set_mode((800, 800))
slika_polje_okomito = pygame.image.load("krizickruzic_template_okomito.png")
slika_polje_vodoravno = pygame.image.load("krizickruzic_template_vodoravno.png")
slika_x = pygame.image.load("x.png")
slika_O = pygame.image.load("o.png")
slika_tabela = pygame.image.load("KRIZICKRUZIC.png")

font = pygame.font.SysFont("Constantia.ttf", 30)

tekst = ""
krivi_tekst = "Krivo područje si stisnuo"
napomena = "NAPOMENA: klikaj u gornji lijevi kut kvadratića!!!"
pobjednik_1 = "Pobjednik je player 1"
pobjednik_2 = "Pobjednik je player 2"
izjednaceno = "Nema pobjednika, izjednaceno je"

krivo = font.render(krivi_tekst, True, "Purple")
krivo2 = font.render(krivi_tekst, True, "Black")
napominjanje = font.render(napomena, True, "Red")
pobjednik_1 = font.render(pobjednik_1, True, "Green")
pobjednik_2 = font.render(pobjednik_2, True, "Green")
izjednaceno = font.render(izjednaceno, True, "Red")
tekst_izmjene = font.render(tekst, True, "Red")



slika_tabela = pygame.transform.scale(slika_tabela, (300, 650))

polje = int((650/19))
x=int(500)
y=int(75)
izmjena = 1
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
        ekran.blit(napominjanje, (100, 25))

        ekran.blit(slika_tabela, (100, 75))

        for i in range(1,4):
            ekran.blit(slika_polje_okomito, (x+polje*i,y))

        for i in range(1,4):
            ekran.blit(slika_polje_vodoravno, (x,y+polje*i)) 
        for i in range(1,4):
            ekran.blit(slika_polje_vodoravno, (x, (y+polje*5)+polje*i))
        for i in range(1,4):
            ekran.blit(slika_polje_vodoravno, (x,(y+polje*10)+polje*i)) 
        for i in range(1,4):
            ekran.blit(slika_polje_vodoravno, (x, (y+polje*15)+polje*i))   

        if dogadjaj.type == pygame.MOUSEBUTTONDOWN:
            pozicija = pygame.mouse.get_pos()
            for i in range (0,4):               
                if pozicija[0] in range ((x + polje*i), (x+polje*(i+1))) and pozicija[1] in range (y, y+polje):
                    if izmjena == 1:
                        ekran.blit(krivo2, (400,400))   
                        izmjena = 0
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
                    if izmjena == 1:
                        ekran.blit(krivo2, (400,400))   
                        izmjena = 0
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
                    if izmjena == 1:
                        ekran.blit(krivo2, (400,400))   
                        izmjena = 0
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
                    if izmjena == 1:
                        ekran.blit(krivo2, (400,400))   
                        izmjena = 0
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
                    if izmjena == 1:
                        ekran.blit(krivo2, (400,400))   
                        izmjena = 0
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
                    if izmjena == 1:
                        ekran.blit(krivo2, (400,400))   
                        izmjena = 0
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
                    if izmjena == 1:
                        ekran.blit(krivo2, (400,400))   
                        izmjena = 0
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
                    if izmjena == 1:
                        ekran.blit(krivo2, (400,400))   
                        izmjena = 0
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
                    if izmjena == 1:
                        ekran.blit(krivo2, (400,400))   
                        izmjena = 0
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
                    if izmjena == 1:
                        ekran.blit(krivo2, (400,400))   
                        izmjena = 0
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
                    if izmjena == 1:
                        ekran.blit(krivo2, (400,400))   
                        izmjena = 0
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
                    if izmjena == 1:
                        ekran.blit(krivo2, (400,400))   
                        izmjena = 0
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
                    if izmjena == 1:
                        ekran.blit(krivo2, (400,400))   
                        izmjena = 0
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
                    if izmjena == 1:
                        ekran.blit(krivo2, (400,400))   
                        izmjena = 0                    
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
                    if izmjena == 1:
                        ekran.blit(krivo2, (400,400))   
                        izmjena = 0                    
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
                    if izmjena == 1:
                        ekran.blit(krivo2, (400,400))   
                        izmjena = 0
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
                
            print(f"{ploča1} \n \n {ploča2} \n \n {ploča3} \n \n {ploča4} \n \n")         
            izmjena = 1
            if pozicija[0] not in range (x, x+polje*4) or pozicija[1] not in range (y, y+polje*19):
                text_surface = font.render(tekst, True, "Purple" )
                izmjena = 0
                if izmjena == 0:
                    ekran.blit(krivo, (400,400))
                    izmjena = 1
              
            #ekran.blit(pobjednik_1, (400,400))
            #ekran.blit(pobjednik_2, (400,400))
            #ekran.blit(izjednaceno, (400,400))
    
    pygame.display.update()    
