import discord

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
    # --- ETAPE 3 ---
    perm=discord.Permissions()
    def embed_creation(perm):
        embed=discord.Embed(title="Permission",
                            description="Ecrivez le numéro situé à côtè de la permission pour changer sa valeur (ex : '3' pour changer le ban_members en True. Valider en envoyant le message 'END'",
                            color=discord.Color.purple())
        embed2=discord.Embed(title="",
                            description="",
                            color=discord.Color.purple())
        t=1
        ls=[]
        for p in perm:
            ls.append(p)
            name = p[0]
            value = p[1]
            if t<=25:
                embed.add_field(name=f"{t}. {name}",
                                value=f"{value}",
                                inline=True)
            else:
                embed2.add_field(name=f"{t}. {name}",
                                value=f"{value}",
                                inline=True)
            t+=1
        return embed, embed2, ls
    embed, embed2, ls = embed_creation(perm)
    bot_message = await message.channel.send(embed=embed)
    bot_message2 = await message.channel.send(embed=embed2)

    def ls_to_dico(ls):
        dico={}
        for i in ls:
            dico[str(i[0])]=bool(i[1])
        return dico

    wait=True
    while wait:
        def check(m):
            return m.author == message.author and m.channel == message.channel
        response = await client.wait_for('message',check=check)
        if str(response.content) == "END":
            wait=False
        elif 0<int(response.content)<len(ls)+2:
            value=bool(ls[int(response.content)-1][1])
            name=str(ls[int(response.content)-1][0])
            #print("From :",ls[int(response.content)-1])
            if value:
                ls[int(response.content)-1] = (name, False)
            else:
                ls[int(response.content)-1] = (name, True)
            dic_perm=ls_to_dico(ls)
            #print("To :",ls[int(response.content)-1])
            #print(dic_perm)
            perm.update(**dic_perm)
            #print("ok")
            embed, embed2, ls = embed_creation(perm)
           
            await bot_message.edit(embed=embed)
            await bot_message2.edit(embed=embed2)
            await response.delete()
            #await message.channel.send(embed=embed2)
    # ---------------
    # --- ETAPE 4 ---
    await serveur.create_role(name=f"{role_name}",
                              color=discord.Color.blurple(),
                              permissions=perm)
    await bot_message.delete()
    await bot_message2.delete()
    await response.delete()
    await message.channel.send(f"Création du rôle **{role_name}** terminée")
    # ---------------

async def deleterole(client,message):
    #Supprime un rôle
    """
        Etape1 : Recherche du rôle
        Etape2 : Demande de Vérification
        Etape3 : Suppression
    """
    # --- INIT.. ---
    role_target=str(message.content).split(" ")[1]
    role_name=[]
    role_final=[]
    for role in message.guild.roles:
        role_name.append(role.name)
        if str(role.name)==role_target:
            role_final=role
    # ---------------

    # --- ETAPE 1 ---
    if role_target not in role_name:
        await message.channel.send(f"Le rôle **n'existe pas**...")
        exit(0)
    # ---------------

    # --- ETAPE 2 ---
    embed=discord.Embed(title="Etes vous sûr de vouloir supprimer ce rôle",
                        description="Write 'YES' to confirm",
                        color=discord.Color.red())
    conf = await message.channel.send(embed=embed)
    def check(m):
        return m.author == message.author and m.channel == message.channel
    response = await client.wait_for('message',check=check)
    if str(response.content).lower() != "yes":
        await conf.delete()
        await response.delete()
        await message.channel.send(f"Action Canceled")
        exit(0)
    # ---------------

    # --- ETAPE 3 ---
    await role_final.delete()
    await conf.delete()
    await response.delete()
    embed=discord.Embed(title=f"Le rôle {role_target} à été correctement supprimé",
                        description=f"By {message.author}",
                        color=discord.Color.green())
    await message.channel.send(embed=embed)
    await message.delete()
    # ---------------

async def addrole(client,message):
    #Ajoute 1 role à une personne
    #Syntax $addrole <ROLE> <PERSONNE>
    """
        Etape 1 : Vérifier que les infos sont donnés
        Etape 2 : Trouve l'objet role et l'objet user à partir de leur nom
        Etape 2 : Ajouter le rôle
    """
    # --- ETAPE 1 ---
    try:
        role_name=str(message.content).split(" ")[1]
        user_id_brut=str(message.content).split(" ")[2] #<!108324>
    except:
        await message.channel.send("Veuillez respecter la syntax :\n$addrole **<ROLE>** **@<USER>**")
        exit(0)
    # ---------------

    # --- ETAPE 2 ---
    role_final=0
    for role in message.guild.roles:
        if str(role.name).lower() == str(role_name).lower():
            role_final=role
    if role_final==0:
        await message.channel.send("Le rôle **n'existe pas**")
        exit(0)
    member_final=0
    #print(message.guild.members)
    for members in message.guild.members:
        if str(members.id) == str(user_id_brut)[3:-1]:
            member_final=members
    if member_final==0:
        await message.channel.send("L'utilisateur **n'existe pas** sur ce serveur")
        exit(0)
    # ---------------

    # --- ETAPE 3 ---
    await member_final.add_roles(role_final)
    embed=discord.Embed(title=f"Le rôle {role_name} à été ajouté à l'utilisateur {member_final.name}",
                        description=f"By {message.author}",
                        color=discord.Color.green())
    await message.channel.send(embed=embed)
    await message.delete()
    # ---------------

async def removerole(client,message):
    #Ajoute 1 role à une personne
    #Syntax $addrole <ROLE> <PERSONNE>
    """
        Etape 1 : Vérifier que les infos sont donnés
        Etape 2 : Trouve l'objet role et l'objet user à partir de leur nom
        Etape 2 : Ajouter le rôle
    """
    # --- ETAPE 1 ---
    try:
        role_name=str(message.content).split(" ")[1]
        user_id_brut=str(message.content).split(" ")[2] #<!108324>
    except:
        await message.channel.send("Veuillez respecter la syntax :\n$addrole **<ROLE>** **@<USER>**")
        exit(0)
    # ---------------

    # --- ETAPE 2 ---
    role_final=0
    for role in message.guild.roles:
        if str(role.name).lower() == str(role_name).lower():
            role_final=role
    if role_final==0:
        await message.channel.send("Le rôle **n'existe pas**")
        exit(0)
    member_final=0
    #print(message.guild.members)
    for members in message.guild.members:
        if str(members.id) == str(user_id_brut)[3:-1]:
            member_final=members
    if member_final==0:
        await message.channel.send("L'utilisateur **n'existe pas** sur ce serveur")
        exit(0)
    # ---------------

    # --- ETAPE 3 ---
    await member_final.remove_roles(role_final)
    embed=discord.Embed(title=f"Le rôle {role_name} à été supprimé à l'utilisateur {member_final.name}",
                        description=f"By {message.author}",
                        color=discord.Color.green())
    await message.channel.send(embed=embed)
    await message.delete()
    # ---------------
def __get_all_role():
    all_perm={"add_reactions":False,
              "administrator":False,
              "attach_files":False,
              "ban_members":False,
              "change_nickname":False,
              "connect":False,
              "create_instant_invite":False,
              "deafen_members":False,
              "embed_links":False,
              "external_emokis":False,
              "kick_members":False,
              "manage_channels":False,
              "manage_guild":False,
              "manage_messages":False,
              "manage_nicknames":False,
              "manage_permissions":False,
              "manage_roles":False,
              "manage_webhooks":False,
              "mention_everyone":False,
              "move_members":False,
              "mute_members":False,
              "priority_speaker":False,
              "read_message_history":False,
              "read_messages":False,
              "request_to_speak":False,
              "send_messages":False,
              "send_tts_messages":False,
              "speak":False,
              "stream":False,
              "use_external_emojis":False,
              "use_slash_commands":False,
              "use_voice_activation":False,
              "view_audit_log":False,
              "view_channel":False,
              "view_guild_insights":False}
    return all_perm