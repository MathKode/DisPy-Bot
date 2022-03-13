#Test Update image
import discord

client = discord.Client()

global msg_
global tour
tour=0

async def send(client,message):
    embed = discord.Embed(title="2048", description="", color=0x00ff00) #creates embed
    file = discord.File("fonction/Game/2048/image.png", filename="image.png")
    salon = await client.fetch_user(int(451723477813166083))
    m=await salon.send(file=file)
    url=m.attachments[0].url
    embed.set_image(url=url)
    msg = await message.channel.send(embed=embed)
    return msg

async def update(original):
    embed = discord.Embed(title="2048", description="", color=0x00ff00) #creates embed
    file = discord.File("fonction/Game/2048/2.png", filename="image.png")
    salon = await client.fetch_user(int(451723477813166083))
    m=await salon.send(file=file)
    url=m.attachments[0].url
    embed.set_image(url=url)
    await original.edit(embed=embed)

@client.event
async def on_message(message):
    global tour
    global msg_
    if tour == 0:
        tour=1
        msg_=await send(client,message)
    else:
        print("deux")
        await update(msg_)



token_file = open("../token.txt","r")
token = str(token_file.read())
token_file.close()
client.run(token)