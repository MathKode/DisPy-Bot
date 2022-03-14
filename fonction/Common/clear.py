import time

async def clear(client,message):
    try:
        commande = message.content.split(' ')
        if len(commande) == 1:
            await message.channel.send("```Vous n'avez pas spécifié le nombre de messages a supprimer```")
        elif len(commande) > 2:
            await message.channel.send("```Syntaxe incorrecte```")
        else:
            num=commande[1]
            print(num, type(num))


            async for msg in message.channel.history(limit=int(num)):

                #print(msg.id)

                await msg.delete()

            confirmed = await message.channel.send(f"```{num} messages supprimés !```")
       
            print(confirmed)
            time.sleep(3)
            await confirmed.delete()
            
    except Exception as err:
        await message.channel.send(f"```Erreur (nombre invalide ?)```")
                
