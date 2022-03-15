import time


async def unlock(client,message):

    try:
        commande = message.content.split(' ')
        chan = commande[1]
        
        chan = int(chan.replace(">","").replace("<","").replace("#",""))
        
        for role in message.guild.roles:
            if role.name == "@everyone":
                
                await message.guild.get_channel(chan).set_permissions(role, read_messages=True,send_messages=True)

                break

        confirmed = await message.channel.send(f"{commande[1]} ```le salon a bien été déverrouillé.```")
        time.sleep(5)
        await confirmed.delete()
    except Exception as err: 
        confirmed = await message.channel.send(f"Une erreur est survenue.```")
        time.sleep(5)
        await confirmed.delete()
        


async def lock(client,message):

    try:
        commande = message.content.split(' ')
        chan = commande[1]
        
        chan = int(chan.replace(">","").replace("<","").replace("#",""))
        
        for role in message.guild.roles:
            if role.name == "@everyone":
                
                await message.guild.get_channel(chan).set_permissions(role, read_messages=True,send_messages=False,attach_files=False)

                break

        confirmed = await message.channel.send(f"{commande[1]}```le salon a bien été verrouillé.```")
        time.sleep(5)
        await confirmed.delete()
    except Exception as err: 
        confirmed = await message.channel.send(f"```Une erreur est survenue.```")
        time.sleep(5)
        await confirmed.delete()
        
