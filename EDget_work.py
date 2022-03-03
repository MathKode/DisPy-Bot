import requests
import json 
from collections import defaultdict
from bs4 import BeautifulSoup as bs
import base64



def get_work(ladate, identifiant,mdp):

    #GETTING TOKEN AND ID
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    }

    data = {
    'data': '{"identifiant": '+'"'+identifiant+'"'+',"motdepasse": '+'"'+mdp+'"'+'}'
    }

    response = requests.post('https://api.ecoledirecte.com/v3/login.awp', headers=headers,data=data)

    json_object = json.loads(response.text)

    token = json_object["token"]
    ###########################################
    data = json_object['data']
    accounts=data["accounts"]
    accounts = accounts[0]
    Id = accounts["id"]



    ####################################

    headers = {
        'x-token': token,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    }
    params = (
        ('verbe', 'get'),
        ('v', '4.2.3'),
    )
    data = {
    'data': '{}'
    }




####################################         Récupération du contenu des devoirs





    global text
    global prof
    global matière
    global nbrDevoir

   
    response = requests.post('https://api.ecoledirecte.com/v3/Eleves/'+str(Id)+'/cahierdetexte/'+ladate+'.awp', headers=headers, params=params, data=data)
    json_work = json.loads(response.text)

    if json_work["code"] == 550:
      prof = ["Erreur"]
      text = ["Cette date n'existe pas !"]
      matière = ["Veuillez réessayer"]
      nbrDevoir = 1
      return

    json_work = json_work['data']
    json_work=json_work["matieres"]
    if json_work == []:
      prof = ["Bonne nouvelle !"]
      text = ["Profitez bien !"]
      matière = ["Aucun devoir prévus pour l'instant."]
      nbrDevoir = 1
      return

 

    nbrDevoir = len(json_work)
    contenu = []
    matière = []
    prof = []


    for x in range(nbrDevoir):
      données = json_work[x]
      
      x= json_work[x]
      x = x["aFaire"]

      contenu.append(x["contenu"]) 
      matière.append(données["matiere"]) 
      prof.append(données["nomProf"])
    


    lines=[]
    text=[]
    for x in range(len(contenu)):
      content = base64.b64decode(contenu[x])
      soup = bs(content, features="html.parser")
      text.append(soup.find_all(text=True))