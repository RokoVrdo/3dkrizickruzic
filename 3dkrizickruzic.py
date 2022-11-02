plocaVelika= [[[None]*4, [None]*4, [None]*4, [None]*4], [[None]*4, [None]*4, [None]*4, [None]*4], [[None]*4, [None]*4, [None]*4, [None]*4], [[None]*4, [None]*4, [None]*4, [None]*4]]

pobjednik=None
izjednaceno= None
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



def promjena_igraca():
    global player1, player2, broj_krugova, trenutni_igrac
    broj_krugova+=1
    if broj_krugova%2!=0:
        trenutni_igrac=player1
    else:
        trenutni_igrac=player2

#def potez():
    #pesicev dio, ako je odabreno polje različito od None print da je polje zauzeto
    

def scoreboard():
    global player1, player2, player1_pobjede, player2_pobjede, lista_pobjeda
    if player1!=lista_pobjeda[0][0]:
        player1_pobjede=0
    if player2!=lista_pobjeda[1][0]:
        player2_pobjede=0
    
    lista_pobjeda={player1:player1_pobjede, player2:player2_pobjede}


def ako_izjednaceno():
    global izjednaceno
    if izjednaceno==True:
        print("Izjednaceno je!")

def vracanje_lobby():
    global izjednaceno, pobjednik, broj_krugova, trenutni_igrac, player1, player2
    if pobjednik!=None or izjednaceno==True:
        pobjednik=None
        broj_krugova=0
        trenutni_igrac=None
        player1=None
        player2=None

        


#display
#pesicev dio ako je resume
#elif scoreboard: scoreboard
#kad se pesicev dio unese: 1)promjena igraca 2)potez 3)pobjeda 4)ako_izjednaceno 5)vracanje u lobby






#while True:
 #   martin dio
  #  peskov dio 
   # 1)prmojena promjena_igraca
    #2)potez
    #3)pobjeda
    #4)izjednaceno
    #5)vracanje u lobby
    #scoreborad 
    #exit-->izlazak iz funckije (igre)
