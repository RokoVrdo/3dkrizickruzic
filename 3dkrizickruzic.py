plocaVelika= [[[None]*4, [None]*4, [None]*4, [None]*4], [[None]*4, [None]*4, [None]*4, [None]*4], [[None]*4, [None]*4, [None]*4, [None]*4], [[None]*4, [None]*4, [None]*4, [None]*4]]

pobjednik=None
izjednaceno= None
trenutni_igrac=None
broj_krugova=0
player1=None
player2=None

def pobjeda():
    global plocaVelika, pobjednik, izjednaceno, trenutni_igrac 
    for ploca in plocaVelika:
        for red in range(4):
            if ploca[red][0]==ploca[red][1]==ploca[red][2]==ploca[red][3] and ploca[red][0] is not None:
                pobjednik= trenutni_igrac #ploca[red][0]
                break
        for stupac in range(4):
            if ploca[0][stupac]==ploca[1][stupac]==ploca[2][stupac]==ploca[3][stupac] and ploca[0][stupac] is not None:
                pobjednik=trenutni_igrac #ploca[0][stupac]
                break
        if ploca[0][0]==ploca[1][1]==ploca[2][2]==ploca[3][3] and ploca[0][0] is not None:
            pobjednik=trenutni_igrac #ploca[0][0]
            break
        if ploca[0][3]==ploca[1][2]==ploca[2][1]==ploca[3][0] and ploca[0][3] is not None:
            pobjednik=trenutni_igrac #ploca[0][3]
            break
    for i in range(4):
        if plocaVelika[0][0][i]==plocaVelika[1][1][i]==plocaVelika[2][2][i]==plocaVelika[3][3][i] and plocaVelika[0][0][i] is not None:
            pobjednik= trenutni_igrac
            break
    for i in range(4):
        if plocaVelika[0][3][i]==plocaVelika[1][2][i]==plocaVelika[2][1][i]==plocaVelika[3][0][i] and plocaVelika[0][3][i] is not None:
            pobjednik= trenutni_igrac
            break
    for i in range(4):
        if plocaVelika[0][i][0]==plocaVelika[1][i][1]==plocaVelika[2][i][2]==plocaVelika[3][i][3] and plocaVelika[0][i][0] is not None:
            pobjednik= trenutni_igrac
            break
    for i in range(4):
        if plocaVelika[0][i][3]==plocaVelika[1][i][2]==plocaVelika[2][i][1]==plocaVelika[3][i][0] and plocaVelika[0][i][3] is not None:
            pobjednik= trenutni_igrac
            break
    for i in range(4):
        for j in range(4):
            if plocaVelika[0][i][j]==plocaVelika[1][i][j]==plocaVelika[2][i][j]==plocaVelika[3][i][j] and plocaVelika[0][i][j] is not None:
                pobjednik= trenutni_igrac
                break
    if plocaVelika[0][0][0]==plocaVelika[1][1][1]==plocaVelika[2][2][2]==plocaVelika[3][3][3] and plocaVelika[0][0][0] is not None:
        pobjednik= trenutni_igrac
    if plocaVelika[0][0][3]==plocaVelika[1][1][2]==plocaVelika[2][2][1]==plocaVelika[3][3][0] and plocaVelika[0][0][3] is not None:
        pobjednik= trenutni_igrac
    if plocaVelika[0][3][0]==plocaVelika[1][2][1]==plocaVelika[2][1][2]==plocaVelika[3][0][3] and plocaVelika[0][3][0] is not None:
        pobjednik= trenutni_igrac
    if plocaVelika[0][3][3]==plocaVelika[1][2][2]==plocaVelika[2][1][1]==plocaVelika[3][0][0] and plocaVelika[0][3][3] is not None:
        pobjednik= trenutni_igrac






        
    



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

def potez():
    #pesicev dio, ako je odabreno polje različito od None print da je polje zauzeto
    