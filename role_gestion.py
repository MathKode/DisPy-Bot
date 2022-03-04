import discord
from matplotlib.pyplot import title

async def newrole(client,message):
    #Creation d'un nouveau role
    """
        Etape 1 : Obtenir les infos serveurs, nom du futur role, liste role existant
        Etape 2 : Si Role exist alors exit
        Etape 3 : Demander les permissions
        Etape 4 : Créer le rôle
    """

    # --- ETAPE 1 ---
    serveur = message.guild
    try :
        role_name = message.content.split(" ")[1]
    except :
        await message.channel.send("Nom de Role requis : **$newrole <ROLENAME>**")
        exit(0)
    role_list = serveur.roles
    # ---------------
    # --- ETAPE 2 ---
    for role in role_list:
        if str(role.name) == role_name:
            await message.channel.send("Le role **existe** déjà...")
            exit(0)
    # ---------------
    # --- ETAPE 3 ---
    perm=discord.Permissions()
    def embed_creation(perm):
        embed=discord.Embed(title="Permission",
                            description="Ecrivez le numéro situé à côtè de la permission pour changer sa valeur (ex : '3' pour changer le ban_members en True. Valider en envoyant le message 'END'",
                            color=discord.Color.purple())
        t=1
        ls=[]
        for p in perm:
            ls.append(p)
            name = p[0]
            value = p[1]
            embed.add_field(name=f"{t}. {name}",
                            value=f"{value}",
                            inline=True)
            t+=1
        return embed, ls
    embed, ls = embed_creation(perm)
    bot_message = await message.channel.send(embed=embed)
    
    wait=True
    while wait:
        def check(m):
            return m.author == message.author and m.channel == message.channel
        response = await client.wait_for('message',check=check)
        
        if response.content == "END":
            wait=False
        if 0<int(response.content)<26:
            value=bool(ls[int(response.content)-1][1])
            name=str(ls[int(response.content)-1][0])
            print("From :",ls[int(response.content)-1])
            if value:
                ls[int(response.content)-1] = (name, False)
            else:
                ls[int(response.content)-1] = (name, True)
            print("To :",ls[int(response.content)-1])
            embed2, ls = embed_creation(perm)
            await bot_message.edit(embed=embed2)
            await message.channel.send(embed=embed2)
            print("EDIT")




    
    #await serveur.create_role(name=f"{role_name}",
     #                         color=discord.Color.blurple(),
      #                        permissions=permissions)



    