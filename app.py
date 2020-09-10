import discord
import random
import os 
import asyncio
import time
from voice_helpers import play

TOKEN = ''

client = discord.Client()

@client.event
async def on_message(message):
    channel = message.channel
    args = message.content.split()
    if message.author == client.user:
        return

    if message.content.startswith('🎤'):
        voice_channel = message.author.voice.channel
        vc = await voice_channel.connect() 

        with open("voiceLines/Greetings.txt",encoding="utf8") as f:
            lines = f.readlines()
            lines = [x.rstrip('\n') for x in lines] 
            line = random.choice(lines)
            await play(vc,'voiceLines/' + line) 

        with open("voiceLines/Rares.txt",encoding="utf8") as f:
            lines = f.readlines()
            lines = [x.rstrip('\n') for x in lines] 
            line = random.choice(lines) 
            await play(vc,'voiceLines/' + line) 
            await vc.disconnect()

    if message.content.startswith('💰'):
        voice_channel = message.author.voice.channel
        vc = await voice_channel.connect() 
        await play(vc, 'voiceLines/Hand_of_Midas.mp3')
        await vc.disconnect()


    if message.content.startswith('🤠'):
        voice_channel = message.author.voice.channel
        vc = await voice_channel.connect() 
        await play(vc, 'country_boy_i_love_you_ahh_mmmmmmm.mp3')
        await vc.disconnect()
        pyvoicechanger.
    
    if message.content.startswith('⚡'):
        voice_channel = message.author.voice.channel
        vc = await voice_channel.connect() 
        await play(vc, 'BazingaPunk.mp3')
        await vc.disconnect()
    
    if message.content.startswith('😎'):
        voice_channel = message.author.voice.channel
        vc = await voice_channel.connect() 
        await play(vc, 'rimshot.mp3')
        await vc.disconnect()

    if message.content.startswith('💨'):
        voice_channel = message.author.voice.channel
        vc = await voice_channel.connect() 
        await play(vc, 'perfectFart.mp3')
        await vc.disconnect()

    if message.content.startswith('🔫'):
        voice_channel = message.author.voice.channel
        vc = await voice_channel.connect() 
        await play(vc, 'mom.mp3')
        await vc.disconnect()
    

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)