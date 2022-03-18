import nacl
import discord
from gtts import gTTS
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

    
        text = " ".join(tosay)
        tts = gTTS(text,lang="fr",tld='ca')
        save_name = str(message.author.voice.channel.id) + ".mp3"
        print(save_name)
        tts.save(save_name)

        audio_source = discord.FFmpegPCMAudio(save_name)
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
        if str(err) == "Already connected to a voice channel.":
            await message.channel.send("```Le bot est déja connecté à un salon vocal !```")


