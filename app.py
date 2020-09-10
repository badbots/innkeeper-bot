import discord
import random
import os 
import asyncio
import time
from modules.voice_helpers import play
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('TOKEN')

client = discord.Client()

@client.event
async def on_message(message):
    channel = message.channel
    args = message.content.split()

    if message.author == client.user:
        return

    if message.content.startswith('🚪'):
        voice_channel = message.author.voice.channel
        vc = await voice_channel.connect() 

        with open("voice_lines/Greetings.txt", encoding="utf8") as f:
            lines = f.readlines()
            lines = [x.rstrip('\n') for x in lines] 
            line = random.choice(lines)
            await play(vc, 'voice_lines/' + line) 

        with open("voice_lines/Rares.txt", encoding="utf8") as f:
            lines = f.readlines()
            lines = [x.rstrip('\n') for x in lines] 
            line = random.choice(lines) 
            await play(vc, 'voice_lines/' + line) 
            await vc.disconnect()
    
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)