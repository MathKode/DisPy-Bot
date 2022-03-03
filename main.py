import discord
from getuserid import *
import EDget_notes 
import EDget_work
import time
from datetime import *

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
            await get_user_id(client,message)
            
                
    if message.content.startswith("!devoirs"):
        await EDget_work.DiscordMessageWork(client,message)
            
    if message.content.startswith("!notes"):
        await EDget_notes.DiscordMessageNotes(client,message)

      
    
    
    
    
            
           
  



# Connection
token_file = open("token.txt","r")
token = str(token_file.read())
token_file.close()
client.run(token)
