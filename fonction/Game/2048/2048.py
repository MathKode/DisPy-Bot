import discord
import generate_img
import random

def __init():
    grille=[]
    choix=random.randint(0,15)
    t=0
    for i in range(4):
        l=[]
        for i in range(4):
            if t==choix:
                l.append(1)
            else:
                l.append(0)
            t+=1
        grille.append(l)
    return grille

def __move(ls,sens):
    """
    Sens: 
        -1 Droite
        -2 Gauche
        -3 Haut
        -4 Bas
    """
    r=[]
    if int(sens) == 1:
        for line in ls:
            r.append(__line_droite(line))
    elif int(sens) == 2:
        for line in ls:
            r.append(__line_gauche(line))
    elif int(sens) == 3:
        t=0
        for line in ls:
            l=__line_vertical(ls,t)
            r.append(__line_gauche(l))
            t+=1
    elif int(sens) == 4:
        t=0
        for line in ls:
            l=__line_vertical(ls,t)
            r.append(__line_droite(l))
            t+=1
    return r

def __line_vertical(ls,x):
    # Input : [.... ls]
    # Output : lingen verticale (colonne x)
    return [ ls[0][x], ls[1][x], ls[2][x], ls[3][x]]



def __line_gauche(line):
    # Input : [ 1; 0; 0; 1]
    # Return : [ 0; 0; 0; 2]
    r1=[]
    for i in line:
        if i != 0:
            r1.append(i)
    r2=[]
    p=0
    while p<len(r1):
        nb=r1[p]
        if p == len(r1)-1: #Dernière nombre
            r2.append(nb)
            p+=1
        else:
            nb_next=r1[p+1]
            print("NB:",nb,nb_next)
            if nb == nb_next:
                r2.append(nb+1)
                p+=2
            else:
                r2.append(nb)
                p+=1
    while len(r2) < 4:
        r2.append(0)
    return r2

def __line_droite(line):
    # Input : [ 1; 0; 0; 1]
    # Return : [ 0; 0; 0; 2]
    line=line[::-1]
    r1=[]
    for i in line:
        if i != 0:
            r1.append(i)
    r2=[]
    p=0
    while p<len(r1):
        nb=r1[p]
        if p == len(r1)-1: #Dernière nombre
            r2.append(nb)
            p+=1
        else:
            nb_next=r1[p+1]
            print("NB:",nb,nb_next)
            if nb == nb_next:
                r2.append(nb+1)
                p+=2
            else:
                r2.append(nb)
                p+=1
    while len(r2) < 4:
        r2.append(0)
    return r2[::-1]

async def main(client, message):
    grille=__init()
    player_id=message.author.id


__line_gauche([3,1,1,1])

print(__line_droite([3,1,1,1]))