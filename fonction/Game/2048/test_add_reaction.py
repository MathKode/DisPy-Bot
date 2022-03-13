#Test wait for Reaction add
import discord

client = discord.Client()


@client.event
async def on_ready():
    print("Start")

@client.event
async def on_message(message):
    if int(message.author.id) != 943555605434630154 :
        print("ok",message.content)
        msg = await message.channel.send("Add react")
        await msg.add_reaction("⬇️")

        def check_react(reaction,user):
            #Check message
            if reaction.message.id == msg.id:
                #Check Auteur
                if int(user.id) == int(message.author.id):
                    #Check Reaction is allow
                    if reaction.emoji in ["⬆️", "⬇️", "⬅️", "➡️", "🛑"]:    
                        return True
            return False
        response= await client.wait_for("reaction_add",check=check_react)
        await msg.channel.send("ok")

token_file = open("../token.txt","r")
token = str(token_file.read())
token_file.close()
client.run(token)