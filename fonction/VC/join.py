import nacl
import discord
import gtts
from playsound import playsound
from discord.utils import *
from io import BytesIO
import pyttsx3
from tempfile import TemporaryFile

async def join(client,message):
    try:
        channel = message.author.voice.channel
        print(channel)
        await channel.connect()
        print("bot joined channel")
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=message.author.guild)
        #audio_source = discord.FFmpegPCMAudio("https://www.youtube.com/watch?v=xNN7iTA57jM")
        #voice_client.play(audio_source)
        if channel == None:
            await message.channel.send("Vous n'êtes connecté à un aucun salon vocal.")
    except Exception as err:
        print(err)

async def speak(client,message):
    try:
        
        commande = message.content.split(' ')
        tosay = commande[1:]

        #############################################################


        engine = pyttsx3.init()
        text = " ".join(tosay)
        engine.save_to_file(text, 'audio.mp3')
        engine.runAndWait()

        audio_source = discord.FFmpegPCMAudio("audio.mp3")
        print("speak command")
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=message.author.guild)
        voice_client.play(audio_source)
        print("ended command")
    except Exception as err: 
        print(str(err))
        if str(err) == "Already playing audio.":
            await message.channel.send("```Veuillez attendre que le bot finisse de parler```")
        
        if str(err) == "'NoneType' object has no attribute 'play'":
            await message.channel.send("```Veuillez vous connecter à un salon vocal et utiliser la commane $join```")



