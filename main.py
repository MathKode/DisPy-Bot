import discord
from getuserid import *
from EDget_notes import get_notes
from EDget_work import get_work



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
            
  



# Connection
token_file = open("../token.txt","r")
token = str(token_file.read())
token_file.close()
client.run(token)
