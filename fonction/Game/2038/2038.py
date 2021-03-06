import importlib
import discord
import random
try:
    generate_img = importlib.import_module("fonction.Game.2038.generate_img")
except:
    import generate_img

def __init():
    grille=[]
    choix=random.randint(0,9)
    t=0
    for i in range(3):
        l=[]
        for i in range(3):
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
    sc=0
    if int(sens) == 1:
        for line in ls:
            l,sc_=__line_droite(line)
            sc+=sc_
            r.append(l)
    elif int(sens) == 2:
        for line in ls:
            l,sc_=__line_gauche(line)
            sc+=sc_
            r.append(l)
    elif int(sens) == 3:
        r,sc=__move_vertical(ls,1)
    elif int(sens) == 4:
        r,sc=__move_vertical(ls,2)
    result=__append_random(r)
    #print(sc) SC -> Score en plus
    return result, sc

def __append_random(ls):
    # Ajoute un nouveau cube
    #print(ls)
    place_libre=0
    for i in ls:
        for j in i:
            if j==0:
                place_libre+=1
    nb=random.randint(0,(place_libre-1))
    t=0
    r=[]
    for i in ls:
        l=[]
        for j in i:
            if t == nb and j==0:
                #print("OK:",j)
                l.append(1)
                t+=1
            else :
                if j == 0:
                    t+=1
                l.append(j)
        r.append(l)
    #print(r)
    return r
        

def __move_vertical(ls,mode):
    ## MODE 1 : UP
    ## MODE 2 : DOWN
    new=[[],[],[]]
    sc=0
    for x in range(3):
        colonne = []
        for y in range(3): 
            colonne.append(ls[y][x])
        
        if int(mode)==1:
            r,sc_=__line_gauche(colonne)
        else:
            r,sc_=__line_droite(colonne)
        sc+=sc_
        for y in range(3):
            new[y].append(r[y])
    return new,sc

def __line_gauche(line):
    # Input : [ 1; 0; 0; 1]
    # Return : [ 0; 0; 0; 2]
    score_under=0
    r1=[]
    for i in line:
        if i != 0:
            r1.append(i)
    r2=[]
    p=0
    while p<len(r1):
        nb=r1[p]
        if p == len(r1)-1: #Derni??re nombre
            r2.append(nb)
            p+=1
        else:
            nb_next=r1[p+1]
            #print("NB:",nb,nb_next)
            if nb == nb_next: #Les deux sont parreil
                r2.append(nb+1)
                score_under+=2**(nb+1)
                p+=2
            else:
                r2.append(nb)
                p+=1
    while len(r2) < 3:
        r2.append(0)
    return r2, score_under

def __line_droite(line):
    # Input : [ 1; 0; 0; 1]
    # Return : [ 0; 0; 0; 2]
    line=line[::-1]
    score_under=0
    r1=[]
    for i in line:
        if i != 0:
            r1.append(i)
    r2=[]
    p=0
    while p<len(r1):
        nb=r1[p]
        if p == len(r1)-1: #Derni??re nombre
            r2.append(nb)
            p+=1
        else:
            nb_next=r1[p+1]
            if nb == nb_next:
                r2.append(nb+1)
                score_under+=2**(nb+1)
                p+=2
            else:
                r2.append(nb)
                p+=1
    while len(r2) < 3:
        r2.append(0)
    return r2[::-1], score_under


async def __send_grille(client,grille,message,mode,old,score):
    #MODE 1 : NEW
    #MODE 2 : MODIF/EDIT
    embed=discord.Embed(title="2038 :",
                        description=f"{score}", 
                        color=0x00ff00)
    generate_img.generate(grille,400,str(message.author.id))
    file=discord.File(f"fonction/Game/2038/{str(message.author.id)}.png", filename="image.png")
    user_id=882590616138182726 #FaiBash
    salon = await client.fetch_user(int(user_id))
    m=await salon.send(file=file)
    url=m.attachments[0].url
    embed.set_image(url=url)
    if int(mode)==1:
        msg = await message.channel.send(embed=embed)
        #?????? ?????? ?????? ?????? ????
        await msg.add_reaction("??????")
        await msg.add_reaction("??????")
        await msg.add_reaction("??????")
        await msg.add_reaction("??????")
        await msg.add_reaction("????")
    else:
        msg = await old.edit(embed=embed)
    await m.delete()
    return msg

async def __high_score(message):
    """
    high.txt
    USERNAME:/!:USERPICTURELINK:/!:SCORE
    """
    try:
        file=open("fonction/Game/2038/high.txt","r")
        c=file.read().split(":/!:")
        file.close()
        embed=discord.Embed(title="Worl 2038 High-Score :",
                            description=f"{c[2]}",
                            color=discord.Color.purple())
        embed.set_author(name=f"{c[0]}",
                        url="",
                        icon_url=f"{c[1]}")
        await message.channel.send(embed=embed)
        max_=int(c[2])
    except:
        max_=0
    return max_

async def main(client, message):
    grille=__init()
    score=0
    game=True
    max_ = await __high_score(message)
    game_message = await __send_grille(client,grille,message,1,None,score)
    while game:
        
        #Get reaction add
        def check_react(reaction,user):
            #Check message
            if reaction.message.id == game_message.id:
                #Check Auteur
                if int(user.id) == int(message.author.id):
                    #Check Reaction is allow
                    if reaction.emoji in ["??????", "??????", "??????", "??????", "????"]:   
                        return True
            return False
        try :
            reaction_=await client.wait_for("reaction_add",check=check_react,timeout=30.0)
        except :
            print("TimeOut")
            game=False

        #reaction_ = tupple (<REACTION>,<USER>)
        reaction=reaction_[0]
        if reaction.emoji == "??????":
            grille,sc=__move(grille,1)
        if reaction.emoji == "??????":
            grille,sc=__move(grille,2)
        if reaction.emoji == "??????":
            grille,sc=__move(grille,3)
        if reaction.emoji == "??????":
            grille,sc=__move(grille,4)
        if reaction.emoji == "????":
            game=False
        else:
            score+=sc
        #Modif Message
        if game:
            await __send_grille(client,grille,message,2,game_message,score)
        
        #Enl??ve la r??action <REACTION>.remove(<USER>)
        await reaction.remove(reaction_[1])
    if int(score) > max_:
        file=open("fonction/Game/2038/high.txt","w")
        m=f"{message.author}:/!:{message.author.avatar_url}:/!:{score}"
        file.write(m)
        file.close()
    await message.channel.send(f"Fin du 2038 !\nTon score est de {score} : **GG**")

#__line_gauche([3,1,1,1])

#print(__line_droite([3,1,1,1]))


game=[  [0,1,0],
        [3,1,2],
        [0,1,0]]
#print(__move_vertical(game,2))