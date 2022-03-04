import discord
import getuserid
import EDget_notes 
import EDget_work
import dilemme
import aide
import mute
import role_gestion

intents = discord.Intents.default() #https://stackoverflow.com/questions/64831017/how-do-i-get-the-discord-py-intents-to-work
intents.members = True #https://discordpy.readthedocs.io/en/stable/intents.html
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Le Bot est Stat")

@client.event
async def on_message(message):
    try:
        prefix=str(message.content[0])
        content=str(message.content[1:])
        #print(content.split(" ")[0])
        if prefix == "$":
            if content == "get-user-id":
                await getuserid.get_user_id(client,message)
            if content == "dilemme" or content == "dilemmes":
                await dilemme.dilemme(client,message)
            if content == "aide" or content == "aides" or content == "help":
                await aide.aide(client,message)
            if content.split(" ")[0] == "mute":
                await mute.mute(client,message)
            if content.split(" ")[0] == "newrole":
                await role_gestion.newrole(client,message)
            if content.split(" ")[0] == "deleterole":
                await role_gestion.deleterole(client,message)
            if content.split(" ")[0] == "addrole":
                await role_gestion.addrole(client,message)
            if content.split(" ")[0] == "removerole":
                await role_gestion.removerole(client,message)
        if message.content.startswith("$devoirs"):
            await EDget_work.DiscordMessageWork(client,message)
                
        if message.content.startswith("$notes"):
            await EDget_notes.DiscordMessageNotes(client,message)
    except: pass
      
    
    

# Connection
token_file = open("../token.txt","r")
token = str(token_file.read())
token_file.close()
client.run(token)
