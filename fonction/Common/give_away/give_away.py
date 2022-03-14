#Code de tirage au sort/give away
from dis import disco
import discord

async def __init(client):
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
    for event in c:
        l=event.split(":%$%:")

        name=str(l[0])
        time=str(l[1])
        channel_id=int(l[2])
        msg_id=int(l[3])
        author=str(l[4])

        channel= client.get_channel(channel_id)
        message=await channel.fetch_message(msg_id)
        await message.edit(content="okokokoko",embed=embed(name,time,author))
        await message.add_reaction("🎉")

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
        msg = await channel_bot.send("ok")
        try:
            file=open("fonction/Common/give_away/scheduling.txt","r")
            c=file.read().split("\n")
            file.close()
        except:
            c=[]
        c.append(f"{name}:%$%:{':'.join(time)}:%$%:{msg.channel.id}:%$%:{msg.id}:%$%:{str(message.author)}")
        
        file=open("fonction/Common/give_away/scheduling.txt","w")
        file.write("\n".join(c))
        file.close()
        
