import profile
from ssl import SSLSyscallError
from traceback import print_exc
from tracemalloc import start
import requests
import json
from collections import defaultdict
import discord
from datetime import *



def get_schedule(date,identifiant, mdp):
    global Data
   
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
        "dateDebut": "2022-02-28",
        "dateFin": "2022-03-06",
        
    }
    params = (
        ('verbe', 'get'),
        ('v', '4.2.3'),
    )
    data = {
    'data': '{\n    "dateDebut": "'+date+'",\n    "dateFin": "'+date+'",\n    "avecTrous": true\n}'
    
    }


   
    response = requests.post('https://api.ecoledirecte.com/v3/E/'+str(Id)+'/emploidutemps.awp?verbe=get&v=4.5.1', headers=headers, data=data,params=params)
    json_data = json.loads(response.content)
    json_data= json_data["data"]
    



    Data = defaultdict(list)

    for x in range(len(json_data)):
        fetch_sched = json_data[x]

        start_date = fetch_sched["start_date"].split(" ")
        start_date=start_date[1]

        end_date = fetch_sched["end_date"].split(" ")
        end_date=end_date[1]
        if fetch_sched["matiere"] == ' ':
            #\u200
            Data[start_date].append("\n")
            Data[start_date].append("")
            Data[start_date].append(start_date)
            Data[start_date].append(end_date)
            Data[start_date].append(fetch_sched["isAnnule"])
            Data[start_date].append("")

        else:
            Data[start_date].append(fetch_sched["matiere"])
            Data[start_date].append(fetch_sched["prof"])
            Data[start_date].append(start_date)
            Data[start_date].append(end_date)
            Data[start_date].append(fetch_sched["isAnnule"])
            Data[start_date].append(fetch_sched["salle"])

    Data = sorted(Data.items())    




##############################################################


async def DiscordMessageSchedule(client,message):
    
  
        if isinstance(message.channel, discord.DMChannel):

            while True:
                try:
                    commande = message.content.split(' ')
                    date_ = commande[1]
                    identifiant=commande[2]
                    mdp = commande[3]
                
                    get_schedule(date_,identifiant,mdp)

                    i=0
                    print(message.author.name+'#'+message.author.discriminator+" a utilisé la commande !edt à :",datetime.now().strftime("%H:%M:%S"))
                    embed=discord.Embed(title=f"__ Emploi du temps pour le {date_} __", description="", color=discord.Color.from_rgb(176, 223, 232))
                    embed.set_footer(text=f"N'arrives pas en retard {message.author.name} ! ❤️")

                    embed.set_author(name=date_, icon_url=message.author.avatar_url)
                    for k,v in Data:


                        if v[0] == "\n":
                            Name = v[2] + "\n" + "  "+v[0] + ' \n'
                            Field = "\n" +"> *PAUSE*\n"+ "**"+v[3]+"**"
                            
                            embed.add_field(name=Name,value=Field, inline=False)
                        
                        
                              
                        if v[4] == True and v[0] != "\n":
                                Name = v[2]+"\n"+"   "+v[0] +" \n" 
                                Field = "> **ANNULE**"+"\n**"+ v[3] + "**"
                                embed.add_field(name=Name, value=Field, inline=True)
                                
                        if v[4] == False and v[0] != "\n":
                                Name = v[2]+"\n"+"   "+v[0]+" \n"
                                Field = "      >      "+v[1]+"  "+v[5] + "\n**"+ v[3] + "**"
                        
                                embed.add_field(name=Name, value=Field, inline=True)

                    await message.channel.send(embed=embed)
                    break


                except Exception as err:
    
                    await message.channel.send("Une erreur est survenue ! (mauvais identifiants ?, syntaxe incorrect) essayez ! aide")
                    
                    break
                break
        
        else:
            await message.delete()
            await message.channel.send("Merci d'utiliser cette commande en privée pour des raisons de sécurité")
            await message.author.send("Veuillez réessayez ici ! ")
