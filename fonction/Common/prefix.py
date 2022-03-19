#Set the prefix of a discord

async def __set_serveur(client,dico_prefix):
    #Ajouste la liste des serveurs présents
    #Ajoute les nouveau serveur à ls
    #Supprime les ancients serveurs
    result={}
    for serveur in client.guilds:
        try:
            prefix=dico_prefix[int(serveur.id)]
            result[int(serveur.id)]=str(prefix)
        except:
            result[int(serveur.id)]="$"
    return result

def __turn_to_dic(ls):
    #After reading the file
    #   Turn ["2836:$"]      <ID_GUILD>:<PREFIX>
    #   Into { 2836: "$"}        
    result={}
    for line in ls:
        if line != '':
            content=line.split(":")
            result[int(content[0])]=str(content[1])
    return result

def __file_actualize(prefix_dico):
    #Actualise le fichier prefix.txt
    # <SERVEUR_ID>:<PREFIX>\n
    ls=[]
    for serveur_id in prefix_dico:
        prefix=prefix_dico[int(serveur_id)]
        ls.append(f"{serveur_id}:{prefix}")
    file=open("fonction/Common/prefix.txt",'w')
    file.write("\n".join(ls))
    file.close()

async def load_prefix(client):
    try :
        file=open("fonction/Common/prefix.txt",'r')
        c=file.read().split('\n')
        file.close()
    except:
        c=[]
    prefix_dico=__turn_to_dic(c)
    prefix_dico=await __set_serveur(client,prefix_dico)
    __file_actualize(prefix_dico)
    return prefix_dico

def change_prefix(message):
    try :
        file=open("fonction/Common/prefix.txt",'r')
        c=file.read().split('\n')
        file.close()
    except:
        c=[]
    prefix_dico=__turn_to_dic(c)
    new_prefix=str(message.content).split(" ")[1]
    prefix_dico[int(message.guild.id)]=f"{new_prefix}"
    __file_actualize(prefix_dico)

    