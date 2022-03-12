import discord #Pour les Embed

async def aide(client,message):
   
    embed=discord.Embed(title="Liste des Commandes :",
                        description="Celles-ci correspondent à l'ensemble des fonctions codées pour H3lper", 
                        color=discord.Color.red())
    try :
        url_ = str(message.guilds.icon_url)
    except:
        url_=""
    
    embed.set_author(name=f"{message.guild}",
                    url="",
                    icon_url=f"{url_}")
    """
    embed.add_field(name="Commande populaire",
                    value="",
                    inline=True)
    """
    embed.add_field(name="$dilemme",
                    value="Commande qui permet de réaliser des sondages/dilemmes anonymes",
                    inline=True)
    embed.add_field(name="$aide",
                    value="Affiche l'ensemble des commandes disponnibles avec leur explication",
                    inline=True)
    embed.add_field(name="$osuprofile <nom d'utilisateur>",
                    value="Affiche les informations d'un joueur OSU!",
                    inline=True)
    embed.add_field(name="$ban",
                    value="$ban <USERNAME> <RAISON (facultatif)>, Banni l'utilisateur du serveur",
                    inline=True)
    # ------------------------------------

    embed_ED=discord.Embed(title="Ecole Directe :",
                        description="",
                        color=discord.Color.red())
    embed_ED.add_field(name="$notes trimestre_nb <USERNAME> <PASSWORD>",
                    value="Affiche les notes écoles directe",
                    inline=True)
    embed_ED.add_field(name="$devoirs année:mois:jour <USERNAME> <PASSWORD>",
                    value="Affiche les devoirs écoles directe",
                    inline=True)
    embed_ED.add_field(name="$edt année:mois:jour <USERNAME> <PASSWORD>",
                    value="Affiche l'agenda en fonction du jour choisis écoles directe",
                    inline=True)  
    # ------------------------------------
    
    embed_ROLE=discord.Embed(title="Gestion des Rôles :",
                        description="",
                        color=discord.Color.red())
    embed_ROLE.add_field(name="$newrole <NAME>",
                    value="Créer un nouveau rôle",
                    inline=True)
    embed_ROLE.add_field(name="$deleterole <NAME>",
                    value="Supprime le rôle",
                    inline=True)
    embed_ROLE.add_field(name="$addrole <ROLE-NAME> @<USER>",
                    value="Ajoute le *role* à l'utilisateur",
                    inline=True)
    embed_ROLE.add_field(name="$removerole <ROLE-NAME> @<USER>",
                    value="Enlève le *role* à l'utilisateur",
                    inline=True)
    
    # ------------------------------------

    embed_DEV=discord.Embed(title="Developpeur :",
                            description="",
                            color=discord.Color.red())            
    embed_DEV.add_field(name="$get_channel_id",
                    value="Renvoit message.channel",
                    inline=True)
    embed_DEV.add_field(name="$get_user_id",
                    value="Renvoit message.author",
                    inline=True)
    embed_DEV.set_footer(text="Never forget 1+1=3")

    await message.author.send(embed=embed)
    await message.author.send(embed=embed_ED)
    await message.author.send(embed=embed_ROLE)
    await message.author.send(embed=embed_DEV)
    await message.delete()
