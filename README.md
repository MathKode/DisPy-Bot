# DisPy-Bot
A Discord Bot coded using Python. Open to collaboration

La syntax pour intégrer le bot (imaginons la fonction lol_reponse dans le fichier autrecode.py) :
> Main.py
```py
import discord
from autrecode import *

@client.event
async def on_message(message):
    if message.content == "LOL":
        await lol_reponse(client,message)
```
> Autrecode.py
```py
async def lol_reponse(client,message):
    salon = message.channel
    await salon.send("Au t'es trop drole")
```

ATTENTION : il faut que ces deux options soient autorisée pour le lancement du bot...

<img src="presentation1.png">
