import requests
import json 
from collections import defaultdict
from bs4 import BeautifulSoup as bs
import base64
import discord
from datetime import *



def get_work(ladate, identifiant,mdp):

    #GETTING TOKEN AND ID
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    }

    data = {
    'data': '{"identifiant": '+'"'+identifiant+'"'+',"motdepasse": '+'"'+mdp+'"'+'}'
    }

    response = requests.post('https://api.ecoledirecte.com/v3/login.awp', headers=headers,data=data)

    json_object = json.loads(response.text)

    token = json_object["token"]
    ###########################################
    data = json_object['data']
    accounts=data["accounts"]
    accounts = accounts[0]
    Id = accounts["id"]



    ####################################

    headers = {
        'x-token': token,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    }
    params = (
        ('verbe', 'get'),
        ('v', '4.2.3'),
    )
    data = {
    'data': '{}'
    }




####################################         Récupération du contenu des devoirs





    global text
    global prof
    global matière
    global nbrDevoir

   
    response = requests.post('https://api.ecoledirecte.com/v3/Eleves/'+str(Id)+'/cahierdetexte/'+ladate+'.awp', headers=headers, params=params, data=data)
    json_work = json.loads(response.text)

    if json_work["code"] == 550:
      prof = ["Erreur"]
      text = ["Cette date n'existe pas !"]
      matière = ["Veuillez réessayer"]
      nbrDevoir = 1
      return

    json_work = json_work['data']
    json_work=json_work["matieres"]
    if json_work == []:
      prof = ["Bonne nouvelle !"]
      text = ["Profitez bien !"]
      matière = ["Aucun devoir prévus pour l'instant."]
      nbrDevoir = 1
      return

 

    nbrDevoir = len(json_work)
    contenu = []
    matière = []
    prof = []


    for x in range(nbrDevoir):
      données = json_work[x]
      
      x= json_work[x]
      x = x["aFaire"]

      contenu.append(x["contenu"]) 
      matière.append(données["matiere"]) 
      prof.append(données["nomProf"])
    


    lines=[]
    text=[]
    for x in range(len(contenu)):
      content = base64.b64decode(contenu[x])
      soup = bs(content, features="html.parser")
      text.append(soup.find_all(text=True))

async def DiscordMessageWork(client,message):
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
        
    
            
