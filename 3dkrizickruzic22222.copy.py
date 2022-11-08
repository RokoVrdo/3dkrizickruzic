from turtle import pos
from turtle import position
#from xxlimited import Str
import pygame
import sys
from pygame.locals import *



pygame.init()
pygame.font.init()



plocaVelika= [[[None]*4, [None]*4, [None]*4, [None]*4], [[None]*4, [None]*4, [None]*4, [None]*4], [[None]*4, [None]*4, [None]*4, [None]*4], [[None]*4, [None]*4, [None]*4, [None]*4]]

izjednaceno= False
broj_krugova=0
player1="Player 1"
player2="Player 2"
trenutni_igrac=None
player1_pobjede=0
player2_pobjede=0

igra=True
pobjednik= None



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
izjednaceno_tekst = "Nema pobjednika, izjednačeno je!" 





krivo = font.render(krivi_tekst, True, "Purple")
krivo2= font.render(krivi_tekst, True, "Black")
napominjanje = font.render(napomena, True, "Red")
pobjednik_1 = font.render(pobjednik_1, True, "Red")
pobjednik_2 = font.render(pobjednik_2, True, "Green")
izjednaceno_tekst = font.render(izjednaceno_tekst, True, "Red")
tekst_izmjene = font.render(tekst, True, "Red")

        
slika_tabela = pygame.transform.scale(slika_tabela, (300, 650))
pobjednik_1 = pygame.transform.scale(pobjednik_1, (650,200))
pobjednik_2 = pygame.transform.scale(pobjednik_2, (650,200))
izjednaceno_tekst = pygame.transform.scale(izjednaceno_tekst, (650,200))



polje = int((650/19))
x=int(500)
y=int(75)


promjena = 0
izmjena=1
text_surface= None

def get_font(size): 
    return pygame.font.Font("font2.otf", size)
def igrači_font(size): 
    return pygame.font.Font(None, size)
xo_font = pygame.font.SysFont("monospace",150)

clock = pygame.time.Clock()
    

def promjena_igraca():
    global broj_krugova, trenutni_igrac
    broj_krugova+=1
    if broj_krugova%2!=0:
        trenutni_igrac=player1
    else:
        trenutni_igrac=player2
    print(trenutni_igrac)



def potez():
    print("Def potez uspio")
    global plocaVelika, izmjena, ekran, promjena, tekst, text_surface, broj_krugova
    izlaz=False
    while True:  
        for dogadjaj in pygame.event.get():
            if dogadjaj.type == pygame.QUIT:
                pygame.quit() 
                sys.exit()
            
            if dogadjaj.type == pygame.MOUSEBUTTONDOWN:           
                pozicija = pygame.mouse.get_pos()
                for i in range (0,4):               
                    if pozicija[0] in range ((x + polje*i), (x+polje*(i+1))) and pozicija[1] in range (y, y+polje):
                        if plocaVelika[0][0][i]==None:
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
                            plocaVelika[0][0][i] = tekst
                            ekran.blit(slika, pozicija)
                            
                        else:
                            izmjena = 0
                            if izmjena == 0:
                                ekran.blit(krivo, (400,400))
                                izmjena = 1
                                broj_krugova+=1


                for i in range (0,4):
                    if pozicija[0] in range ((x + polje*i), (x+polje*(i+1))) and pozicija[1] in range (y + polje*1, y+polje*2):
                        if plocaVelika[0][1][i]==None:
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
                            plocaVelika[0][1][i] = tekst
                            ekran.blit(slika, pozicija)
                    
                        else:
                            izmjena = 0
                            if izmjena == 0:
                                ekran.blit(krivo, (400,400))
                                izmjena = 1
                                broj_krugova+=1


                for i in range (0,4):
                    if pozicija[0] in range ((x + polje*i), (x+polje*(i+1))) and pozicija[1] in range (y + polje*2, y+polje*3):
                        if plocaVelika[0][2][i]==None:
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
                            plocaVelika[0][2][i] = tekst
                            ekran.blit(slika, pozicija)
                        else:
                            izmjena = 0
                            if izmjena == 0:
                                ekran.blit(krivo, (400,400))
                                izmjena = 1
                                broj_krugova+=1
                    
                for i in range (0,4):
                    if pozicija[0] in range ((x + polje*i), (x+polje*(i+1))) and pozicija[1] in range (y + polje*3, y+polje*4):
                        if plocaVelika[0][3][i]==None:
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
                            plocaVelika[0][3][i] = tekst
                            ekran.blit(slika, pozicija)
                        else:
                            izmjena = 0
                            if izmjena == 0:
                                ekran.blit(krivo, (400,400))
                                izmjena = 1
                                broj_krugova+=1
                    
                for i in range (0,4):
                    if pozicija[0] in range ((x + polje*i), (x+polje*(i+1))) and pozicija[1] in range (y + polje*5, y+polje*6):
                        if plocaVelika[1][0][i]==None:
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
                            plocaVelika[1][0][i] = tekst
                            ekran.blit(slika, pozicija)
                        else:
                            izmjena = 0
                            if izmjena == 0:
                                ekran.blit(krivo, (400,400))
                                izmjena = 1
                                broj_krugova+=1
                    
                for i in range (0,4):
                    if pozicija[0] in range ((x + polje*i), (x+polje*(i+1))) and pozicija[1] in range (y + polje*6, y+polje*7):
                        if plocaVelika[1][1][i]==None:
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
                            plocaVelika[1][1][i] = tekst
                            ekran.blit(slika, pozicija)
                        else:
                            izmjena = 0
                            if izmjena == 0:
                                ekran.blit(krivo, (400,400))
                                izmjena = 1
                                broj_krugova+=1
         
                for i in range (0,4):
                    if pozicija[0] in range ((x + polje*i), (x+polje*(i+1))) and pozicija[1] in range (y + polje*7, y+polje*8):
                        if plocaVelika[1][2][i]==None:
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
                            plocaVelika[1][2][i] = tekst
                            ekran.blit(slika, pozicija)
                        else:
                            izmjena = 0
                            if izmjena == 0:
                                ekran.blit(krivo, (400,400))
                                izmjena = 1
                                broj_krugova+=1

                for i in range (0,4):
                    if pozicija[0] in range ((x + polje*i), (x+polje*(i+1))) and pozicija[1] in range (y + polje*8, y+polje*9):
                        if plocaVelika[1][3][i]==None:
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
                            plocaVelika[1][3][i] = tekst
                            ekran.blit(slika, pozicija)
                        else:
                            izmjena = 0
                            if izmjena == 0:
                                ekran.blit(krivo, (400,400))
                                izmjena = 1
                                broj_krugova+=1
                    
                for i in range (0,4):
                    if pozicija[0] in range ((x + polje*i), (x+polje*(i+1))) and pozicija[1] in range (y + polje*10, y+polje*11):
                        if plocaVelika[2][0][i]==None:
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
                            plocaVelika[2][0][i] = tekst
                            ekran.blit(slika, pozicija)
                        else:
                            izmjena = 0
                            if izmjena == 0:
                                ekran.blit(krivo, (400,400))
                                izmjena = 1
                                broj_krugova+=1
                    
                for i in range (0,4):
                    if pozicija[0] in range ((x + polje*i), (x+polje*(i+1))) and pozicija[1] in range (y + polje*11, y+polje*12):
                        if plocaVelika[2][1][i]==None:
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
                            plocaVelika[2][1][i] = tekst
                            ekran.blit(slika, pozicija)
                        else:
                            izmjena = 0
                            if izmjena == 0:
                                ekran.blit(krivo, (400,400))
                                izmjena = 1
                                broj_krugova+=1

                for i in range (0,4):
                    if pozicija[0] in range ((x + polje*i), (x+polje*(i+1))) and pozicija[1] in range (y + polje*12, y+polje*13):
                        if plocaVelika[2][2][i]==None:
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
                            plocaVelika[2][2][i] = tekst
                            ekran.blit(slika, pozicija)
                        else:
                            izmjena = 0
                            if izmjena == 0:
                                ekran.blit(krivo, (400,400))
                                izmjena = 1
                                broj_krugova+=1

                for i in range (0,4):
                    if pozicija[0] in range ((x + polje*i), (x+polje*(i+1))) and pozicija[1] in range (y + polje*13, y+polje*14):
                        if plocaVelika[2][3][i]==None:
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
                            plocaVelika[2][3][i] = tekst
                            ekran.blit(slika, pozicija)
                        else:
                            izmjena = 0
                            if izmjena == 0:
                                ekran.blit(krivo, (400,400))
                                izmjena = 1
                                broj_krugova+=1

                for i in range (0,4):
                    if pozicija[0] in range ((x + polje*i), (x+polje*(i+1))) and pozicija[1] in range (y + polje*15, y+polje*16):
                        if plocaVelika[3][0][i]==None:
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
                            plocaVelika[3][0][i] = tekst
                            ekran.blit(slika, pozicija)
                        else:
                            izmjena = 0
                            if izmjena == 0:
                                ekran.blit(krivo, (400,400))
                                izmjena = 1
                                broj_krugova+=1

                for i in range (0,4):
                    if pozicija[0] in range ((x + polje*i), (x+polje*(i+1))) and pozicija[1] in range (y + polje*16, y+polje*17):
                        if plocaVelika[3][1][i]==None:
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
                            plocaVelika[3][1][i] = tekst
                            ekran.blit(slika, pozicija)
                        else:
                            izmjena = 0
                            if izmjena == 0:
                                ekran.blit(krivo, (400,400))
                                izmjena = 1
                                broj_krugova+=1

                for i in range (0,4):
                    if pozicija[0] in range ((x + polje*i), (x+polje*(i+1))) and pozicija[1] in range (y + polje*17, y+polje*18):
                        if plocaVelika[3][2][i]==None:
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
                            plocaVelika[3][2][i] = tekst
                            ekran.blit(slika, pozicija)
                        else:
                            izmjena = 0
                            if izmjena == 0:
                                ekran.blit(krivo, (400,400))
                                izmjena = 1
                                broj_krugova+=1
                    
                for i in range (0,4):
                    if pozicija[0] in range ((x + polje*i), (x+polje*(i+1))) and pozicija[1] in range (y + polje*18, y+polje*19):
                        if plocaVelika[3][3][i]==None:
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
                            plocaVelika[3][3][i] = tekst
                            ekran.blit(slika, pozicija)
                        else:
                            izmjena = 0
                            if izmjena == 0:
                                ekran.blit(krivo, (400,400))
                                izmjena = 1
                                broj_krugova+=1
            
                izmjena = 1
                if pozicija[0] not in range (x, x+polje*4) or pozicija[1] not in range (y, y+polje*19):
                    text_surface = font.render(tekst, True, "Purple" )
                    izmjena = 0
                    if izmjena == 0:
                        ekran.blit(krivo, (400,400))
                        izmjena = 1
                        broj_krugova+=1

                izlaz=True
        if izlaz==True:
            break
                  
            
            



def pobjeda():
    global pobjednik, trenutni_igrac, player1_pobjede, player2_pobjede, izjednaceno, pobjednik_1, pobjednik_2
    print("Def pobjeda uspjela")
    for ploca in plocaVelika:
        for red in range(4):
            if ploca[red][0]==ploca[red][1]==ploca[red][2]==ploca[red][3] and ploca[red][0] is not None:
                pobjednik= trenutni_igrac
                if trenutni_igrac==player1:
                    player1_pobjede+=1
                    ekran.blit(pobjednik_1, (400,400))
                    
                else:
                    player2_pobjede+=1
                    ekran.blit(pobjednik_2, (400,400))

                break
        for stupac in range(4):
            if ploca[0][stupac]==ploca[1][stupac]==ploca[2][stupac]==ploca[3][stupac] and ploca[0][stupac] is not None:
                pobjednik=trenutni_igrac 
                if trenutni_igrac==player1:
                    player1_pobjede+=1
                    ekran.blit(pobjednik_1, (400,400))
                else:
                    player2_pobjede+=1
                    ekran.blit(pobjednik_2, (400,400))
                break
        if ploca[0][0]==ploca[1][1]==ploca[2][2]==ploca[3][3] and ploca[0][0] is not None:
            pobjednik=trenutni_igrac 
            if trenutni_igrac==player1:
                player1_pobjede+=1
                ekran.blit(pobjednik_1, (400,400))
            else:
                player2_pobjede+=1
                ekran.blit(pobjednik_2, (400,400))
            break
        if ploca[0][3]==ploca[1][2]==ploca[2][1]==ploca[3][0] and ploca[0][3] is not None:
            pobjednik=trenutni_igrac
            if trenutni_igrac==player1:
                player1_pobjede+=1
                ekran.blit(pobjednik_1, (400,400))
            else:
                player2_pobjede+=1
                ekran.blit(pobjednik_2, (400,400))
            break
    for i in range(4):
        if plocaVelika[0][0][i]==plocaVelika[1][1][i]==plocaVelika[2][2][i]==plocaVelika[3][3][i] and plocaVelika[0][0][i] is not None:
            pobjednik= trenutni_igrac
            if trenutni_igrac==player1:
                player1_pobjede+=1
                ekran.blit(pobjednik_1, (400,400))
            else:
                player2_pobjede+=1
                ekran.blit(pobjednik_2, (400,400))
            break
    for i in range(4):
        if plocaVelika[0][3][i]==plocaVelika[1][2][i]==plocaVelika[2][1][i]==plocaVelika[3][0][i] and plocaVelika[0][3][i] is not None:
            pobjednik= trenutni_igrac
            if trenutni_igrac==player1:
                player1_pobjede+=1
                ekran.blit(pobjednik_1, (400,400))
            else:
                player2_pobjede+=1
                ekran.blit(pobjednik_2, (400,400))
            break
    for i in range(4):
        if plocaVelika[0][i][0]==plocaVelika[1][i][1]==plocaVelika[2][i][2]==plocaVelika[3][i][3] and plocaVelika[0][i][0] is not None:
            pobjednik= trenutni_igrac
            if trenutni_igrac==player1:
                player1_pobjede+=1
                ekran.blit(pobjednik_1, (400,400))
            else:
                player2_pobjede+=1
                ekran.blit(pobjednik_2, (400,400))
            break
    for i in range(4):
        if plocaVelika[0][i][3]==plocaVelika[1][i][2]==plocaVelika[2][i][1]==plocaVelika[3][i][0] and plocaVelika[0][i][3] is not None:
            pobjednik= trenutni_igrac
            if trenutni_igrac==player1:
                player1_pobjede+=1
                ekran.blit(pobjednik_1, (400,400))
            else:
                player2_pobjede+=1
                ekran.blit(pobjednik_2, (400,400))
            break
    for i in range(4):
        for j in range(4):
            if plocaVelika[0][i][j]==plocaVelika[1][i][j]==plocaVelika[2][i][j]==plocaVelika[3][i][j] and plocaVelika[0][i][j] is not None:
                pobjednik= trenutni_igrac
                if trenutni_igrac==player1:
                    player1_pobjede+=1
                    ekran.blit(pobjednik_1, (400,400))
                else:
                    player2_pobjede+=1
                    ekran.blit(pobjednik_2, (400,400))
                break
    if plocaVelika[0][0][0]==plocaVelika[1][1][1]==plocaVelika[2][2][2]==plocaVelika[3][3][3] and plocaVelika[0][0][0] is not None:
        pobjednik= trenutni_igrac
        if trenutni_igrac==player1:
            player1_pobjede+=1
            ekran.blit(pobjednik_1, (400,400))
        else:
            player2_pobjede+=1
            ekran.blit(pobjednik_2, (400,400))
        
    if plocaVelika[0][0][3]==plocaVelika[1][1][2]==plocaVelika[2][2][1]==plocaVelika[3][3][0] and plocaVelika[0][0][3] is not None:
        pobjednik= trenutni_igrac
        if trenutni_igrac==player1:
            player1_pobjede+=1
            ekran.blit(pobjednik_1, (400,400))
        else:
            player2_pobjede+=1
            ekran.blit(pobjednik_2, (400,400))

    if plocaVelika[0][3][0]==plocaVelika[1][2][1]==plocaVelika[2][1][2]==plocaVelika[3][0][3] and plocaVelika[0][3][0] is not None:
        pobjednik= trenutni_igrac
        if trenutni_igrac==player1:
            player1_pobjede+=1
            ekran.blit(pobjednik_1, (400,400))
        else:
            player2_pobjede+=1
            ekran.blit(pobjednik_2, (400,400))
    if plocaVelika[0][3][3]==plocaVelika[1][2][2]==plocaVelika[2][1][1]==plocaVelika[3][0][0] and plocaVelika[0][3][3] is not None:
        pobjednik= trenutni_igrac
        if trenutni_igrac==player1:
            player1_pobjede+=1
            ekran.blit(pobjednik_1, (400,400))
        else:
            player2_pobjede+=1
            ekran.blit(pobjednik_2, (400,400))
        
        for i in plocaVelika:
            for j in range(4):
                for z in range(4):
                    if i[j][z]!=None:
                        if pobjednik==None:
                            izjednaceno=True
   



def ako_izjednaceno_pobjeda():
    print("Ako izjednačeno uspjelo")
    if izjednaceno==True:
        ekran.fill("Black")
        ekran.blit(izjednaceno_tekst, (75,300))
        pygame.display.update()
        pygame.time.delay(4000)
    elif pobjednik != None:
        ekran.fill("Black")
        if pobjednik == player1:
            ekran.blit(pobjednik_1, (75,300))
            pygame.display.update()
            pygame.time.delay(4000)
        elif pobjednik == player2:
            ekran.blit(pobjednik_2, (75,300))
            pygame.display.update()
            pygame.time.delay(4000)

    


        




def vracanje_lobby():
    global pobjednik, izjednaceno, trenutni_igrac, plocaVelika, igra, promjena, izmjena, broj_krugova
    print("Vracanje lobby uspjelo")
    if pobjednik!=None or izjednaceno==True:
        pobjednik=None
        broj_krugova=0
        izjednaceno= False
        trenutni_igrac=None
        igra=False
        promjena=0
        izmjena=1
        plocaVelika= [[[None]*4, [None]*4, [None]*4, [None]*4], [[None]*4, [None]*4, [None]*4, [None]*4], [[None]*4, [None]*4, [None]*4, [None]*4], [[None]*4, [None]*4, [None]*4, [None]*4]]
        main_menu()

        





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




def play():
    global ekran
    ekran = pygame.display.set_mode((800, 800))
        
    while igra==True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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
        

        pygame.display.update()
                



    
        promjena_igraca()
        potez()
        pobjeda()
        ako_izjednaceno_pobjeda()
        vracanje_lobby()

        
         


        
          
                 

        
    
def scoreboard():
    while True:
        SCOREBOARD_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("blue")

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
        jedan_igrac=str(player1+"-"+str(player1_pobjede)+"pobjeda")
        drugi_igrac=str(player2+"-"+str(player2_pobjede)+"pobjeda")
        jedan_igrac = xo_font.render(jedan_igrac, True , (250, 250, 250))
        drugi_igrac = xo_font.render(drugi_igrac, True , (250, 250, 250))
        jedan_igrac=pygame.transform.scale(jedan_igrac, (1000, 150))
        drugi_igrac=pygame.transform.scale(drugi_igrac, (1000, 150))
        SCREEN.blit(jedan_igrac, (150, 50))
        SCREEN.blit(drugi_igrac, (150, 200))

        pygame.display.update()



def main_menu():
    global SCREEN, igra
    igra=True
    SCREEN = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Menu")

    SCREEN.fill((65,105,225))

    
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


