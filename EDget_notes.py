import requests
import json 
from collections import defaultdict
import discord

def get_notes(periode,identifiant,mdp):

    global Data

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

  
    response = requests.post('https://api.ecoledirecte.com/v3/Eleves/'+str(Id)+'/notes.awp', headers=headers, params=params, data=data)
    json_work = json.loads(response.text)



    json_work = json_work['data']
    json_work = json_work['notes']
    periode = str(periode)


    Data = defaultdict(list)

    for x in range(len(json_work)):

        infoNote = json_work[x]
       
        Short_note = infoNote["codePeriode"].replace("A001","1").replace("A002","2").replace("A003","3"),infoNote["libelleMatiere"],str(infoNote["valeur"]).replace(",",'.'),infoNote["noteSur"]
        
        if Short_note[2] == 'Disp\xa0':
            Data[Short_note[1]].append(Short_note[2])
        elif Short_note[2] == 'Abs\xa0':
            Data[Short_note[1]].append(Short_note[2])

        
        # 
        #Short_note=infoNote["codePeriode"].replace("A001","1").replace("A002","2").replace("A003","3"),infoNote["libelleMatiere"],int(Short_note[2]*Short_note[3])
        elif Short_note[0] == periode:
            Short_note=infoNote["codePeriode"].replace("A001","1").replace("A002","2").replace("A003","3"),infoNote["libelleMatiere"],float(float(Short_note[2])*20/float(Short_note[3]))

            Data[Short_note[1]].append(str(Short_note[2]).replace(".0",""))

async def DiscordMessageNotes(client,message):            
    
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
                print(err) 
                
                await message.channel.send("Une erreur est survenue ! (mauvais identifiants ?, syntaxe incorrect) essayez ! aide")
