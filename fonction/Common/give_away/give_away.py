#Code de tirage au sort/give away
import discord
import random


def __time(r):
    minute=r[2]
    heure=r[1]
    jour=r[0]
    minute-=1
    if minute < 0:
        if heure > 0:
            heure-=1
            minute=59
        else:
            if jour > 0:
                heure=24
                jour-=1
                minute=59
    return [jour,heure,minute]

async def __end(client,message,name):
    #Mesage = message concours
    for react in message.reactions:
        if react.emoji == "🎉" :
            users = await react.users().flatten()
            break
    for j in range(len(users)):
        if users[j].bot:
            del users[j]
            break
    win = random.choice(users)
    await message.edit(content=f"Un grand **GG** à @{win.mention} qui remporte le tirage !!!")

def __text_to_ascii(txt):
    #Retourne un texte ASCII
    caractere_ascii=['\x00', '\x01', '\x02', '\x03', '\x04', '\x05', '\x06', '\x07', '\x08', '\t', '\n', '\x0b', '\x0c', '\r', '\x0e', '\x0f', '\x10', '\x11', '\x12', '\x13', '\x14', '\x15', '\x16', '\x17', '\x18', '\x19', '\x1a', '\x1b', '\x1c', '\x1d', '\x1e', '\x1f', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', '\x7f', '\x80', '\x81', '\x82', '\x83', '\x84', '\x85', '\x86', '\x87', '\x88', '\x89', '\x8a', '\x8b', '\x8c', '\x8d', '\x8e', '\x8f', '\x90', '\x91', '\x92', '\x93', '\x94', '\x95', '\x96', '\x97', '\x98', '\x99', '\x9a', '\x9b', '\x9c', '\x9d', '\x9e', '\x9f', '\xa0', '¡', '¢', '£', '¤', '¥', '¦', '§', '¨', '©', 'ª', '«', '¬', '\xad', '®', '¯', '°', '±', '²', '³', '´', 'µ', '¶', '·', '¸', '¹', 'º', '»', '¼', '½', '¾', '¿', 'À', 'Á', 'Â', 'Ã', 'Ä', 'Å', 'Æ', 'Ç', 'È', 'É', 'Ê', 'Ë', 'Ì', 'Í', 'Î', 'Ï', 'Ð', 'Ñ', 'Ò', 'Ó', 'Ô', 'Õ', 'Ö', '×', 'Ø', 'Ù', 'Ú', 'Û', 'Ü', 'Ý', 'Þ', 'ß', 'à', 'á', 'â', 'ã', 'ä', 'å', 'æ', 'ç', 'è', 'é', 'ê', 'ë', 'ì', 'í', 'î', 'ï', 'ð', 'ñ', 'ò', 'ó', 'ô', 'õ', 'ö', '÷', 'ø', 'ù', 'ú', 'û', 'ü', 'ý', 'þ','Ā']
    r=""
    for i in txt:
        if i in caractere_ascii:
            r+=i
    return r

async def init_(client):
    """
        <Event-Name>:%$%:<Time-code>:%$%:<Guild-ID>:%$%:<Message-id>
    """
    def embed(name, time, author):
        m=discord.Embed(title=f"🎉  GIVE AWAY  🎉",
                        description=f"**Prix :** {name}\n**Temps restant :** {time} \n**Hosted by :** {author}",
                        color=discord.Color.blurple())
        m.set_footer(text="Participe avec une réaction 🎉")
        return m
    path="fonction/Common/give_away/scheduling.txt"
    file=open(f"{path}","r")
    c=file.read().split("\n")
    file.close()
    new_ls=[]
    for event in c:
        l=event.split(":%$%:")
        if len(l) > 2:
            name=str(l[0])
            time=str(l[1])
            channel_id=int(l[2])
            msg_id=int(l[3])
            author=str(l[4])

            channel= client.get_channel(channel_id)
            message=await channel.fetch_message(msg_id)
            await message.edit(embed=embed(name,str(time),author))
            await message.add_reaction("🎉")
            
            #Enlève 1 minute
            ls=time.split(":")
            r=[]
            for i in ls:
                r.append(int(i))
            re=__time(r)
            find=False
            for i in re:
                if i!=0:find=True
            if not find:
                await __end(client,message,name)
                await message.edit(embed=embed(name,"END",author))
            else:
                r=[]
                for i in re:
                    r.append(str(i))
                time=":".join(r)
                new_ls.append(f"{name}:%$%:{time}:%$%:{channel_id}:%$%:{msg_id}:%$%:{author}")
    file=open("fonction/Common/give_away/scheduling.txt","w")
    file.write("\n".join(new_ls))
    file.close()


    

async def give_away(client, message):
    #Fonction
    salon=message.guild.channels
    embed = lambda name, description: discord.Embed(title=f"{name} :",description=f"{description}",color=discord.Color.blurple())
    def check1(m):
        if m.author == message.author and m.channel == message.channel:
            if len(str(m.content).split(":"))==3:
                return True
        return False
    def check2(m):
        if m.author == message.author and m.channel == message.channel:
            name_=str(m.content)
            #print(name_[0:2])
            if name_[0:2]=="<#":        
                return True
        return False
    #---------
    
    name=" ".join(str(message.content).split(" ")[1:])
    if name == "":
        await message.channel.send("Syntax à respecter : **$give_away <NAME>**")
        exit("Sans Nom")

    name=__text_to_ascii(name)
    question=await message.channel.send(embed=embed("Time-out","Le format de réponse obligatoire **jour:heure:minutes**\n*Exemple fin dans 3heures : 0:3:0*"))
    response=await client.wait_for("message",check=check1)
    time=str(response.content).split(":")
    await question.delete()
    await response.delete()

    question=await message.channel.send(embed=embed("Channel","Mettre le salon avec son **#<SALON>**"))
    response=await client.wait_for("message",check=check2)
    id_ = str(response.content)[2:-1]
    channel_bot=None
    for channel in salon:
        if str(channel.id) == str(id_):
            channel_bot=channel
    if channel_bot != None:
        msg = await channel_bot.send("Give Away init...")
        try:
            file=open("fonction/Common/give_away/scheduling.txt","r")
            c=file.read().split("\n")
            file.close()
        except:
            c=[]
        c.append(f"{name}:%$%:{':'.join(time)}:%$%:{msg.channel.id}:%$%:{msg.id}:%$%:{str(message.author)}")
        c2=[]
        for i in c:
            if i!='':
                c2.append(i)
        try:
            file=open("fonction/Common/give_away/scheduling.txt","w")
            file.write("\n".join(c2))
            file.close()
            def embed(name, time, author):
                m=discord.Embed(title=f"🎉  GIVE AWAY  🎉",
                                description=f"**Prix :** {name}\n**Temps restant :** {time} \n**Hosted by :** {author}",
                                color=discord.Color.blurple())
                m.set_footer(text="Participe avec une réaction 🎉")
                return m
            await msg.edit(content="",embed=embed(name,":".join(time),message.author))
            await msg.add_reaction("🎉")
        except Exception as e:
            print(e)
        await question.delete()
        await response.delete()
        await message.delete()
        


#__time([3,4,23])
