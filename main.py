import discord
import getuserid
import EDget_notes 
import EDget_work
import dilemme
import aide
import mute
import role_gestion

client = discord.Client()

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
