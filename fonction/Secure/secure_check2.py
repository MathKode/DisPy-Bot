import discord

async def check_perm_ls(message,perm_ls,mode):
    #Vérifie si l'auteur a les permitions nécessaires
    """
        Input : messsage ["speak", "administrator"] 1
        Return : True or False
        
        MODE 1 : Vérifie si l'utilisateur a TOUTES les perms
        MODE 2 : Vérifie si l'utilisateur a AU MOINS 1 perms
    """
    if perm_ls == []: #Veut dire que tout est autorisé
        return True
    if str(message.author.id) == str(message.guild.owner_id):
        return True
    result=[]
    for perm in perm_ls:
        r=await check_perm(message,perm)
        result.append(r)
    if int(mode) == 1:
        find=True
        for i in result:
            if i == False:
                find=False
    elif int(mode) == 2:
        find=False
        for i in result:
            if i==True:
                find=True
    return find

async def check_perm(message,perm_name):
    #Dis si l'auteur du message à une permission
    """
        Input : message "seak"
        Return : True or False
    """
    role_ls=__get_role(message)
    find=False
    for role in role_ls:
        for perm in role.permissions:
            #perm = ('attach_files', False)
            if str(perm[0]) == str(perm_name) and bool(perm[1]) == True:
                find=True
    return find


def __get_role(message):
    """
        Input : message
        Output : [<Role1>, <Role2>, <Role3>]
    """
    author_id = message.author.id
    dico_membre = __dico_membre(message)
    try:
        membre = dico_membre[str(author_id)]
    except:
        print("Erreur Fonction secure_check/__get_role :",NameError,TypeError)
    role_ls=[]
    for role in membre.roles:
        role_ls.append(role)
    return role_ls

def __dico_membre(message):
    #Retourne le dico des membres d'un serveur
    """
        Input : message
        Output : {"ID" : <MEMBRE>, "ID" : <MEMBRE>}
    """
    dico={}
    for member in message.guild.members:
        dico[str(member.id)]=member
    return dico
