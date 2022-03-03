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
            
            
            
            
            
            
            
##############################################################################COMMANDES ECOLEDIRECT####################################################################          
            
    if message.content.startswith("!devoirs"):
      
      if isinstance(message.channel, discord.DMChannel):

        while True:
            try:
                commande = message.content.split(' ')
                ladate = commande[1]
                identifiant=commande[2]
                mdp = commande[3]
            
                get_work(ladate,identifiant,mdp)
    
                i=0
                print(message.author.name+'#'+message.author.discriminator+" a utilisé la commande !devoirs à :",datetime.now().strftime("%H:%M:%S"))
                embed=discord.Embed(title=f"__📖 Devoirs pour le {ladate} __", description="", color=discord.Color.from_rgb(176, 223, 232))
                embed.set_footer(text=f"Bon travail {message.author.name} ! ❤️")
                
                embed.set_author(name=prof[i], icon_url=message.author.avatar_url)
                for x in range(nbrDevoir):
                    
                    embed.add_field(name=matière[i], value=''.join(text[i]), inline=False)
                    i+=1

                await message.channel.send(embed=embed)
                
            except Exception as err:
            

                await message.channel.send("Une erreur est survenue ! (mauvais identifiants ?, syntaxe incorrect) essayez ! aide")
                
                break
            break
    
      else:
          await message.delete()
          await message.channel.send("Merci d'utiliser cette commande en privée pour des raisons de sécurité")
          await message.author.send("Veuillez réessayez ici ! ")
        
    
            
    if message.content.startswith("!notes"):
        try:
            if isinstance(message.channel, discord.DMChannel):


                commande = message.content.split(' ')
                trimestre = int(commande[1])
                identifiant=commande[2]
                mdp = commande[3]
                get_notes(trimestre,identifiant,mdp)

                embed=discord.Embed(title=f"__Notes du {trimestre} trimestre : __", description="", color=discord.Color.from_rgb(111, 250, 100))
                embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                embed.set_footer(text=f"Donne toi à fond {message.author.name} ! ❤️")
                
                for k, v in Data.items():

                    embed.add_field(name=k, value='\n'.join(v), inline=True)
                await message.channel.send(embed=embed)
            else:
                await message.delete()
                await message.channel.send("Merci d'utiliser cette commande en privée pour des raisons de sécurité")
                await message.author.send("Veuillez réessayez ici ! ")
        except Exception as err:

            await message.channel.send("Une erreur est survenue ! (mauvais identifiants ?, syntaxe incorrect) essayez ! aide")
#################################################################################################################################################################                

    
      
    
    
    
    
            
           
  



# Connection
token_file = open("../token.txt","r")
token = str(token_file.read())
token_file.close()
client.run(token)
