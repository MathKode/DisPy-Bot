import discord
import getuserid
import EDget_notes 
import EDget_work
import dilemme
import aide

client = discord.Client()

@client.event
async def on_ready():
    print("Le Bot est Stat")

@client.event
async def on_message(message):
    prefix=str(message.content[0])
    content=str(message.content[1:])
    if prefix == "$":
        if content == "get-user-id":
            await getuserid.get_user_id(client,message)
        if content == "dilemme" or content == "dilemmes":
            await dilemme.dilemme(client,message)
        if content == "aide" or content == "aides":
            await aide.aide(client,message)   
    if message.content.startswith("$devoirs"):
        await EDget_work.DiscordMessageWork(client,message)
            
    if message.content.startswith("$notes"):
        await EDget_notes.DiscordMessageNotes(client,message)

      
    
    
    
    
            
           
  



# Connection
token_file = open("../token.txt","r")
token = str(token_file.read())
token_file.close()
client.run(token)
