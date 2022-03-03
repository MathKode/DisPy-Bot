import discord #Pour les Embed

async def aide(client,message):
    embed=discord.Embed(title="Liste des Commandes :",
                #description="Celles-ci corresponent à l'ensemble des fonctions codées pour H3lper", 
                        description="",
                        color=discord.Color.red())
    try :
        url_ = str(message.guilds.icon_url)
    except:
        url_=""
    embed.set_author(name=f"{message.guilds}",
                    url="",
                    icon_url=f"{url_}")
    embed.add_field(name="$dilemme",
                    value="Commande qui permet de réaliser des sondages/dilemmes anonymes",
                    inline=False)
    embed.add_field(name="$get_channel_id",
                    value="Renvoit message.channel",
                    inline=True)
    embed.add_field(name="$get_user_id",
                    value="Renvoit message.author",
                    inline=True)
    embed.add_field(name="$aide",
                    value="Affiche l'ensemble des commandes disponnibles avec leur explication",
                    inline=False)
    embed.add_field(name="$notes trimestre_nb <USERNAME> <PASSWORD>",
                    value="Affiche les notes écoles directe",
                    inline=False)
    embed.add_field(name="$devoirs",
                    value="Affiche les devoirs écoles directe",
                    inline=False)
    embed.set_footer(text="Never forget 1+1=3")
    await message.author.send(embed=embed)
    await message.delete()