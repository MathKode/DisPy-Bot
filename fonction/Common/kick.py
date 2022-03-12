import discord
from discord.ext import commands
from discord.ext.commands import Bot
import re
from discord.utils import get




async def kick(client, message):
    commande = message.content.split(' ')
    membre=commande[1]
  
    try:
      num = int(''.join(re.findall(r'\d+', membre)))

      user = await message.guild.query_members(user_ids=[num])
      user = user[0]
 

      embed=discord.Embed(title=f"__ Vous avez été explusé ! __", description="", color=discord.Color.from_rgb(51, 218, 255))
      embed.set_footer(text=f"Surveillez votre comportement {user.name} !")

      embed.set_author(name=user.name, icon_url=user.avatar_url)

      if len(commande)==2:
        embed.add_field(name="Informations : ",value=f"Expulsé de **{user.guild}**,\nRaison : Aucune raison fournie", inline=True)
        await user.send(embed=embed)
        await user.kick(reason=' '.join(commande[2:]))
      elif len(commande)>2:
        embed.add_field(name="Informations : ",value=f"Expulsé de **{user.guild}**,\nRaison : {' '.join(commande[2:])}", inline=True)
        await user.send(embed=embed)
        await user.kick(reason=' '.join(commande[2:]))

      
      print(f"{user} as been kicked")
      
      #print(f"Banned {member.display_name}!")
    except Exception as err:
      await user.send("Vous ne pouvez pas expulser un administrateur.")
    

    