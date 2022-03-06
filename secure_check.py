#Fichier servant de controlleur (vérifie si un membre à le rôle nécessaire pour une action)
import discord

async def init(client,command_ls,serveur_on):
    #Initialise le fichier serveur.txt
    """
    Ce fichier contient les autorisations de chaques serveurs
        Syntax : 
                {SERVEUR.NAME}:{commande}/{RoleID}${state}%{RoleID}$State:{commande}/...
                {SERVEUR.NAME}:
                ...
    Ces informations seront stockées dans la variable dico_perm :
        Syntax :
                dico_perm[Serveur][commande][Role] = state
                dico_perm = {
                    "BiMathAx-SERV" : {
                        "get-user-id" : {
                            "1234241" : True
                            "8467263" : False
                        }
                        "newrole" : {
                            "1234241" : False
                            "8467263" : False
                        }
                    }
                    "Lunar-SERV" : {
                        "get-user-id" : {
                            "1234241" : True
                            "8467263" : True
                        }
                        "newrole" : {
                            "1234241" : True
                            "8467263" : True
                        }
                    }
                }
    """
    try:
        file=open("serveur.txt","r")
        c=file.read().split("\n")
        file.close()
        dico_perm={}
        for line in c:
            cut=line.split(":")
            serveur_name = cut[0]
            del cut[0]
            dic_command={}
            for commande in cut:
                commande_name = str(commande.split("/")[0])
                dic_role={}
                for role in commande.split("/")[1]:
                    role_name = str(role.split("$")[0])
                    role_state = bool(role.split("$")[1])
                    dic_role[role_name]=role_state
                dic_command[commande_name] = dic_role
            dico_perm[serveur_name] = dic_command
    except:
        dico_perm={}
    
    ### Vérifie que tous les serveurs sont présents
    serv_name=[]
    for serveur in serveur_on:
        serv_name.append(serveur.name)
    for serv in dico_perm:
        if serv not in dico_perm:

