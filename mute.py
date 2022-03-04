import discord

async def __add_role(message,member,role_name):
    print(message.guild.roles)
    #discord.utils.get(message.guild.roles)
    #await member.add_roles()
async def mute(client,message):
    await __add_role(message,message.author,"mute")