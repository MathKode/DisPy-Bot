import discord
from discord.ext import commands
from discord.ext.commands import Bot
import re
from discord.utils import get





async def ban(client, message):
    commande = message.content.split(' ')
    membre=commande[1]
  
    try:
      num = int(''.join(re.findall(r'\d+', membre)))

      user = await message.guild.query_members(user_ids=[num]) 
      user = user[0]
 

      embed=discord.Embed(title=f"__ Vous avez été banni ! __", description="", color=discord.Color.from_rgb(51, 218, 255))
      embed.set_footer(text=f"Surveillez votre comportement {user.name} !")

      embed.set_author(name=user.name, icon_url=user.avatar_url)

      if len(commande)==2:
        reason_ = "Aucune raison fournie"
        embed.add_field(name="Informations : ",value=f"banni de **{user.guild}**,\nRaison : Aucune raison fournie", inline=True)
        await user.send(embed=embed)
        await user.ban(delete_message_days=7)
      elif len(commande)>2:
        reason_ = f"{' '.join(commande[2:])}"
        embed.add_field(name="Informations : ",value=f"banni de **{user.guild}**,\nRaison : {' '.join(commande[2:])}", inline=True)
        await user.send(embed=embed)
        await user.ban(reason=' '.join(commande[2:]), delete_message_days=7)


      validation_embed=discord.Embed(title=f"__ {user} a été banni ! __", description="", color=discord.Color.from_rgb(42, 255, 0))
      validation_embed.add_field(name="Raison : ",value=reason_, inline=True)
      validation_embed.set_author(name=user.name, icon_url=user.avatar_url)
      validation_embed.set_footer(text=f"Expulsé par {message.author.name} !")

      await message.channel.send(embed=validation_embed)

      
      print(f"{user} as been banned")
      
      #print(f"Banned {member.display_name}!")
    except Exception as err:
      await user.send("Vous ne pouvez pas bannir un administrateur.")
    

    
