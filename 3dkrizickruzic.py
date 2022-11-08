plocaVelika= [[[None]*4, [None]*4, [None]*4, [None]*4], [[None]*4, [None]*4, [None]*4, [None]*4], [[None]*4, [None]*4, [None]*4, [None]*4], [[None]*4, [None]*4, [None]*4, [None]*4]]

pobjednik=None
izjednaceno= False
trenutni_igrac=None
broj_krugova=0
player1=None
player2=None
player1_pobjede=0
player2_pobjede=0
lista_pobjeda={}

def pobjeda():
    global plocaVelika, pobjednik, izjednaceno, trenutni_igrac, player1_pobjede, player2_pobjede 
    for ploca in plocaVelika:
        for red in range(4):
            if ploca[red][0]==ploca[red][1]==ploca[red][2]==ploca[red][3] and ploca[red][0] is not None:
                pobjednik= trenutni_igrac
                if trenutni_igrac==player1:
                    player1_pobjede+=1
                else:
                    player2_pobjede+=1

                break
        for stupac in range(4):
            if ploca[0][stupac]==ploca[1][stupac]==ploca[2][stupac]==ploca[3][stupac] and ploca[0][stupac] is not None:
                pobjednik=trenutni_igrac 
                if trenutni_igrac==player1:
                    player1_pobjede+=1
                else:
                    player2_pobjede+=1
                break
        if ploca[0][0]==ploca[1][1]==ploca[2][2]==ploca[3][3] and ploca[0][0] is not None:
            pobjednik=trenutni_igrac 
            if trenutni_igrac==player1:
                player1_pobjede+=1
            else:
                player2_pobjede+=1
            break
        if ploca[0][3]==ploca[1][2]==ploca[2][1]==ploca[3][0] and ploca[0][3] is not None:
            pobjednik=trenutni_igrac
            if trenutni_igrac==player1:
                player1_pobjede+=1
            else:
                player2_pobjede+=1
            break
    for i in range(4):
        if plocaVelika[0][0][i]==plocaVelika[1][1][i]==plocaVelika[2][2][i]==plocaVelika[3][3][i] and plocaVelika[0][0][i] is not None:
            pobjednik= trenutni_igrac
            if trenutni_igrac==player1:
                player1_pobjede+=1
            else:
                player2_pobjede+=1
            break
    for i in range(4):
        if plocaVelika[0][3][i]==plocaVelika[1][2][i]==plocaVelika[2][1][i]==plocaVelika[3][0][i] and plocaVelika[0][3][i] is not None:
            pobjednik= trenutni_igrac
            if trenutni_igrac==player1:
                player1_pobjede+=1
            else:
                player2_pobjede+=1
            break
    for i in range(4):
        if plocaVelika[0][i][0]==plocaVelika[1][i][1]==plocaVelika[2][i][2]==plocaVelika[3][i][3] and plocaVelika[0][i][0] is not None:
            pobjednik= trenutni_igrac
            if trenutni_igrac==player1:
                player1_pobjede+=1
            else:
                player2_pobjede+=1
            break
    for i in range(4):
        if plocaVelika[0][i][3]==plocaVelika[1][i][2]==plocaVelika[2][i][1]==plocaVelika[3][i][0] and plocaVelika[0][i][3] is not None:
            pobjednik= trenutni_igrac
            if trenutni_igrac==player1:
                player1_pobjede+=1
            else:
                player2_pobjede+=1
            break
    for i in range(4):
        for j in range(4):
            if plocaVelika[0][i][j]==plocaVelika[1][i][j]==plocaVelika[2][i][j]==plocaVelika[3][i][j] and plocaVelika[0][i][j] is not None:
                pobjednik= trenutni_igrac
                if trenutni_igrac==player1:
                    player1_pobjede+=1
                else:
                    player2_pobjede+=1
                break
    if plocaVelika[0][0][0]==plocaVelika[1][1][1]==plocaVelika[2][2][2]==plocaVelika[3][3][3] and plocaVelika[0][0][0] is not None:
        pobjednik= trenutni_igrac
        if trenutni_igrac==player1:
            player1_pobjede+=1
        else:
            player2_pobjede+=1
        
    if plocaVelika[0][0][3]==plocaVelika[1][1][2]==plocaVelika[2][2][1]==plocaVelika[3][3][0] and plocaVelika[0][0][3] is not None:
        pobjednik= trenutni_igrac
        if trenutni_igrac==player1:
            player1_pobjede+=1
        else:
            player2_pobjede+=1

    if plocaVelika[0][3][0]==plocaVelika[1][2][1]==plocaVelika[2][1][2]==plocaVelika[3][0][3] and plocaVelika[0][3][0] is not None:
        pobjednik= trenutni_igrac
        if trenutni_igrac==player1:
            player1_pobjede+=1
        else:
            player2_pobjede+=1
    if plocaVelika[0][3][3]==plocaVelika[1][2][2]==plocaVelika[2][1][1]==plocaVelika[3][0][0] and plocaVelika[0][3][3] is not None:
        pobjednik= trenutni_igrac
        if trenutni_igrac==player1:
            player1_pobjede+=1
        else:
            player2_pobjede+=1
        
        for i in plocaVelika:
            for j in range(4):
                for z in range(4):
                    if i[j][z]!=None:
                        if pobjednik==None:
                            izjednaceno=True

#funkcija pobjeda provjerava sve moguće slučajeve pobjede, ukupno ih je 76 (10 na svakoj ploči, to je ukupno 40, 
#prostorne dijagonale kojih je 4, dijagonale između ploča kojih je 8 u jednom smjeru i 8 u drugom i još stupci između ploča kojih je 16)



def promjena_igraca():
    global player1, player2, broj_krugova, trenutni_igrac
    broj_krugova+=1
    if broj_krugova%2!=0:
        trenutni_igrac=player1
    else:
        trenutni_igrac=player2

#funkciji promjena igrača je cilj nakon svakog odigranog kruga (kada jedan igrač napravi potez) promjeniti igrača koji je na redu

#def potez():
    #pesicev dio, ako je odabreno polje različito od None print da je polje zauzeto

#potez je u biti pesicev dio u kojem se na polje stavljaju križić i kuzić, moj je jedini 
#zadatak u tom dijelu bilo dodati da ako se klikne na polje koje je već zauzeto da javi to igraču i da mu da opet bira polje
    





#ova funkcija scoreboard je napravljena u slučaju da će se moći mijenjati ime igrača nakon svake partije, pa da ako ime ostane 
#isto nastavi brojat pobjede, a ako se ime promijeni da počne od 0, no nakraju funkcija nije trebala u samom kodu jer smo se zbog 
#jednostavnosti dogovorili da će biti samo player 1 i player 2

#def scoreboard():
#    global player1_pobjede, player2_pobjede, lista_pobjeda
#    if player1!=lista_pobjeda[0][0]:
#        player1_pobjede=0
#    if player2!=lista_pobjeda[1][0]:
#        player2_pobjede=0
    
#    lista_pobjeda={player1:player1_pobjede, player2:player2_pobjede}




def ako_izjednaceno():
    if izjednaceno==True:
        print("Izjednaceno je!")

#funkcija ako izjednaceno provjerava je li izjednačen rezultat, tu sam sad stavio print 
#jer nisam imo ništa drugo, ali u samom programu je drugačije pošto je sučelje grafičko


def vracanje_lobby():
    global izjednaceno, pobjednik, broj_krugova, trenutni_igrac, player1, player2
    if pobjednik!=None or izjednaceno==True:
        pobjednik=None
        broj_krugova=0
        trenutni_igrac=None
        player1=None
        player2=None
        izjednaceno=False

#ovoj funkciji je zadatak zapravo bio nakon završetka partije vratiti igru u lobby, odnosno na main menu, 
#tu još ne dostaje dio u kojem vraća u main menu, budući da je to marta radila





#moj dio zadatka je bio, kao što smo Vam već i rekli logika same igrice, tako da sam ja smišljao način kako to sve zajedno povezati
#ovih nekoliko funkcija je nužno za funkcioniranje same igrice, naravno uz martin i lovrin dio, kada su njih dvoje dostavili svoje dijeove
#okvirna ideja mi je izgledala ovako:

#while True:
#martin dio
#if play:
#while True:
#iscrtavanje ploče za igru (pešićev dio)
#promjena igrača
#potez
#pobjeda
#ako izjednačeno
#povratak u lobby


#tako je otprilike i izgledao kod, možda malo drugačije s obzirom na neke preinake koje smo morali napravit, 
#ali je princip sa petljom u petlji ostao isti

#što se tiče ovog drugog filea (word dokumenta) to sam si ja skicirao neke stvari, neuredno je pa mislim da neće biti od pomoći ali svejedno sam ga stavio

        



