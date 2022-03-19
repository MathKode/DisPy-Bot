import importlib
import discord
import os

import fonction.Common.lock as lockchannel
import fonction.Common.getuserid as getuserid
import fonction.ED.EDget_notes as EDget_notes
import fonction.ED.EDget_work as EDget_work
import fonction.Common.dilemme as dilemme
import fonction.Aide.aide as aide
import fonction.Common.mute as mute
import fonction.Role.role_gestion as role_gestion
import fonction.Secure.secure_check2 as secure_check
import fonction.ED.EDget_schedule as EDget_schedule
import fonction.Common.ban as ban
import fonction.Common.kick as kick
import fonction.Profile.osuprofile as osuprofile
import fonction.Common.clear as clear
import fonction.Common.blague as blague
_2048 = importlib.import_module("fonction.Game.2048.2048")
_2038 = importlib.import_module("fonction.Game.2038.2038")
import fonction.VC.join as join
import fonction.Common.give_away.give_away as give_away
import fonction.Common.prefix as prefix


intents = discord.Intents.default() #https://stackoverflow.com/questions/64831017/how-do-i-get-the-discord-py-intents-to-work
intents.members = True #https://discordpy.readthedocs.io/en/stable/intents.html
client = discord.Client(intents=intents)

global serveur_on
serveur_on = [] #Liste des serveurs où le bot est présent

global command_dico #Liste de toutes les commandes du bot avec leurs permitions
command_dico={"get-user-id":[],
              "dilemme": [],
              "aide": [],
              "mute": ["administrator"],
              "newrole": ["administrator","manage_roles"],
              "deleterole": ["administrator","manage_roles"],
              "addrole": ["administrator","manage_roles"],
              "removerole": ["administrator","manage_roles"],
              "devoirs": [],
              "notes": [],
              "edt": [],
              "ban": ["ban_members"],
              "2048": [],
              "2038": [],
              "kick": ["kick_members"],
              "osuprofile": [],
              "clear": ["manage_messages"],
              "lock": ["manage_channels"],
              "unlock": ["manage_channels"],
              "blague": [],
              "join": [],
              "speak": [],
              "give_away" : [],
              "newprefix": []
              }


@tasks.loop(minutes=1)
async def give_away_loop():
    await give_away.init_(client)
    
   
@client.event
async def on_ready():
    print("Le Bot est Stat\nConnect At :")
    for serveur in client.guilds:
        serveur_on.append(serveur)
        print(f"   |-- {serveur.name}  {serveur.id}")
    print("   ---")
    
    global serveur_prefix
    serveur_prefix = await prefix.load_prefix(client)
    print(serveur_prefix)
    
    give_away_loop.start()
    
        

@client.event
async def on_message(message):
    global serveur_prefix
    try:
        prefix_serv=serveur_prefix[int(message.guild.id)]
        prefix_=str(message.content[0:len(prefix_serv)])
        content=str(message.content[len(prefix_serv):])
        #print(content.split(" ")[0])
        if str(prefix_) == str(prefix_serv):
            allow=True
            try :
                perm_ls=command_dico[str(content.split(" ")[0])]
                autorisation = await secure_check.check_perm_ls(message,perm_ls,2)
                if not autorisation:
                    allow=False
            except:
                print("Commande Non configuré dans command_dico")
            if not allow:
                await message.channel.send("Tu n'as pas la **permission** pour executer cette commande")
                exit("Pas les permissions")
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
            if content.split(" ")[0] == "deleterole":
                await role_gestion.deleterole(client,message)
            if content.split(" ")[0] == "addrole":
                await role_gestion.addrole(client,message)
            if content.split(" ")[0] == "removerole":
                await role_gestion.removerole(client,message)
            if content.split(" ")[0] == "check":
                await secure_check.check_perm(message,"speak")
            if content.split(" ")[0] == "devoirs":
                await EDget_work.DiscordMessageWork(client,message)        
            if content.split(" ")[0] == "notes":
                await EDget_notes.DiscordMessageNotes(client,message)
            if content.split(" ")[0] == "edt":
                await EDget_schedule.DiscordMessageSchedule(client,message)
            if content.split(" ")[0] == "2048":
                await _2048.main(client,message)
                path=f"fonction/Game/2048/{message.author.id}.png"
                os.remove(path)
            if content.split(" ")[0] == "2038":
                await _2038.main(client,message)
                path=f"fonction/Game/2038/{message.author.id}.png"
                os.remove(path)
            if content.split(" ")[0] == "ban":
                await ban.ban(client,message)
            if content.split(" ")[0] == "kick":
                await kick.kick(client,message)
            if content.split(" ")[0] == "osuprofile":
                await osuprofile.osu_profile(client,message)
            if content.split(" ")[0] == "clear":
                await clear.clear(client,message)
            if content.split(" ")[0] == "lock":
                await lockchannel.lock(client,message)
            if content.split(" ")[0] == "unlock":
                await lockchannel.unlock(client,message)
            if content.split(" ")[0] == "blague":
                await blague.joke(client,message)
            if content.split(" ")[0] == "join":
                await join.join(client,message)
            if content.split(" ")[0] == "speak":
                await join.speak(client,message)
            if content.split(" ")[0] == "give_away":
                await give_away.give_away(client,message)
            if content.split(" ")[0] == "newprefix":
                prefix.change_prefix(message)
                serveur_prefix = await prefix.load_prefix(client)
    except: pass
      
    
    

# Connection
token_file = open("../token.txt","r")
token = str(token_file.read())
token_file.close()
client.run(token)
