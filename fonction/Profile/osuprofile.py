import requests
import json
import discord



def get_token():
    headers = {
        'Accept': 'application/json',
    }

    json_data = {
        'client_id': 13295,
        'client_secret': 'JYG0YJ97tBiYkSVE7RUtS4zj48aFNKAdqjbliNdx',
        'grant_type': 'client_credentials',
        'scope': 'public',
    }

    response = requests.post('https://osu.ppy.sh/oauth/token', headers=headers, json=json_data)

    return json.loads(response.text)["access_token"]


def get_stat(username):

    global avatar
    global level
    global play_count 
    global pp
    global country_rank
    global global_rank
    global totalscore
    global accuracy
    global levelup

    token=get_token()



    headers={
        "Content-type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {token}"
    }
    
    response = requests.get("https://osu.ppy.sh/api/v2/users/"+username, headers=headers)
    #print(json.loads(response.text))

        
    elements = json.loads(response.text)
    try:
        if elements["error"] == None:

            return "Invalid"
    except:
        
        avatar = elements["avatar_url"]
        #print(elements.keys())


        stat = json.loads(response.text)["statistics"]
        

        accuracy = stat["hit_accuracy"]
        totalscore=stat["total_score"]
        level = stat["level"]["current"]
        levelup = stat["level"]["progress"]
        play_count = stat["play_count"]
        pp = stat["pp"]
        country_rank = stat["country_rank"]
        global_rank = stat["global_rank"]
  

    #print(avatar, level, play_count, pp,country_rank,global_rank, totalscore, accuracy)






async def osu_profile(client,message):

        commande = message.content.split(' ')
        username = commande[1]
        get_stat(username)

        if get_stat(username) == "Invalid":

            embed=discord.Embed(title=f"__ Profile de {username} __", description="", color=discord.Color.from_rgb(247, 99, 166))
            embed.set_footer(text=f"Play for fun, stop farming pp !")

            embed.set_author(name=username, icon_url=message.author.avatar_url)
            embed.add_field(name="Erreur : ",value="Ce profil n'existe pas", inline=True)
            await message.channel.send(embed=embed)

        else:
####################### embed (relou)
            embed=discord.Embed(title=f"__ Profile de {username} __", description="", color=discord.Color.from_rgb(247, 99, 166))
            embed.set_footer(text=f"Play for fun, stop farming pp !")

            embed.set_author(name=username, icon_url=avatar)


            embed.add_field(name="Classement Global :",value=global_rank, inline=True)
            embed.add_field(name="Classement Pays :",value=country_rank, inline=True)
            embed.add_field(name="Perfomance Point :",value=pp, inline=True)
            embed.add_field(name="Précision :",value=accuracy, inline=True)
            embed.add_field(name="Score total :",value=totalscore, inline=True)
            embed.add_field(name="Nombre de parties :",value=play_count, inline=True)
            
            progress_bar = ["0 "]
            #progress = int(list(str(level))[0])
            progress = int(level)//2
            #print("\n",progress,"\n")
            for x in range(progress//2):
                progress_bar.append("▮")
            for x in range((50-progress)//2):
                progress_bar.append("▯")
            progress_bar.append(" 100") 
            valuelevel = "> **"+str(level)+"**"+ "\n"+"".join(progress_bar)
            embed.add_field(name="Niveau :",value=valuelevel, inline=False)

            


            progress_bar_actual_rankup = [str(level)+" "]

            for x in range(int(levelup)//4):
                progress_bar_actual_rankup.append("▮")
            for x in range((100-int(levelup))//4):
                progress_bar_actual_rankup.append("▯")

            levelplus1 = int(level)+1
            progress_bar_actual_rankup.append(" "+str(levelplus1))

        
            
            valuerankup = "".join(progress_bar_actual_rankup)

            embed.add_field(name="Progression jusqu'au prochain niveau :",value=valuerankup, inline=False)


            
            await message.channel.send(embed=embed)



############################################