from blagues_api import BlaguesAPI
import discord



async def joke(client,message):
    commande = message.content.split(' ')
    if len(commande) == 1:
    

        try:
            blagues = BlaguesAPI("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNDUxNzgxNjM3OTQwOTY5NDczIiwibGltaXQiOjEwMCwia2V5IjoiY2hVSWV2R1N5TGhqTkpOQk5UY2pGd0ROcDZ6T3ZRazlhUE84MjZlTFdBTGlxUVNiM1kiLCJjcmVhdGVkX2F0IjoiMjAyMi0wMy0xNFQyMDowMToxNyswMDowMCIsImlhdCI6MTY0NzI4ODA3N30.xvOy4BxYn0hF9Q8h3lYSqn5dXnja1-HbY12M0x91-W4")
            Blague = await blagues.random()

            embed=discord.Embed(title=f"__ Et voici pour vous une blague de la meilleure des qualités ! __", description="", color=discord.Color.from_rgb(51, 218, 255))
            embed.set_footer(text=f"Si c'est une blague raciste, nous ne sommes pas responsables !")
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)


            embed.add_field(name=f"{Blague.joke}",value=f"{Blague.answer}", inline=False)
            await message.channel.send(embed=embed)
            
        except Exception as err:
            print(err)
        
    else:
        JokeType = commande[1]
        if JokeType == "dark":
            try:
                blagues = BlaguesAPI("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNDUxNzgxNjM3OTQwOTY5NDczIiwibGltaXQiOjEwMCwia2V5IjoiY2hVSWV2R1N5TGhqTkpOQk5UY2pGd0ROcDZ6T3ZRazlhUE84MjZlTFdBTGlxUVNiM1kiLCJjcmVhdGVkX2F0IjoiMjAyMi0wMy0xNFQyMDowMToxNyswMDowMCIsImlhdCI6MTY0NzI4ODA3N30.xvOy4BxYn0hF9Q8h3lYSqn5dXnja1-HbY12M0x91-W4")
                Blague = await blagues.random_categorized('dark')

                embed=discord.Embed(title=f"__ ATTENTION HUMOUR NOIR ! __", description="", color=discord.Color.from_rgb(255, 0, 0))
                embed.set_footer(text=f"Si c'est une blague raciste, nous ne sommes pas responsables !")
                embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)


                embed.add_field(name=f"{Blague.joke}",value=f"|| {Blague.answer} ||", inline=False)
                await message.channel.send(embed=embed)
                
            except Exception as err:
                print(err)
        if JokeType == "beauf":
            try:
                blagues = BlaguesAPI("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNDUxNzgxNjM3OTQwOTY5NDczIiwibGltaXQiOjEwMCwia2V5IjoiY2hVSWV2R1N5TGhqTkpOQk5UY2pGd0ROcDZ6T3ZRazlhUE84MjZlTFdBTGlxUVNiM1kiLCJjcmVhdGVkX2F0IjoiMjAyMi0wMy0xNFQyMDowMToxNyswMDowMCIsImlhdCI6MTY0NzI4ODA3N30.xvOy4BxYn0hF9Q8h3lYSqn5dXnja1-HbY12M0x91-W4")
                Blague = await blagues.random_categorized('beauf')

                embed=discord.Embed(title=f"__ ATTENTION HUMOUR BEAUF ! __", description="", color=discord.Color.from_rgb(255, 0, 0))
                embed.set_footer(text=f"Si c'est une blague raciste, nous ne sommes pas responsables !")
                embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)


                embed.add_field(name=f"{Blague.joke}",value=f"|| {Blague.answer} ||", inline=False)
                await message.channel.send(embed=embed)
                
            except Exception as err:
                print(err)
        if JokeType == "limit":
            try:
                blagues = BlaguesAPI("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNDUxNzgxNjM3OTQwOTY5NDczIiwibGltaXQiOjEwMCwia2V5IjoiY2hVSWV2R1N5TGhqTkpOQk5UY2pGd0ROcDZ6T3ZRazlhUE84MjZlTFdBTGlxUVNiM1kiLCJjcmVhdGVkX2F0IjoiMjAyMi0wMy0xNFQyMDowMToxNyswMDowMCIsImlhdCI6MTY0NzI4ODA3N30.xvOy4BxYn0hF9Q8h3lYSqn5dXnja1-HbY12M0x91-W4")
                Blague = await blagues.random_categorized('limit')

                embed=discord.Embed(title=f"__ ATTENTION HUMOUR LIMITE ! __", description="", color=discord.Color.from_rgb(255, 0, 0))
                embed.set_footer(text=f"Si c'est une blague raciste, nous ne sommes pas responsables !")
                embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)


                embed.add_field(name=f"{Blague.joke}",value=f"|| {Blague.answer} ||", inline=False)
                await message.channel.send(embed=embed)
                
            except Exception as err:
                print(err)
