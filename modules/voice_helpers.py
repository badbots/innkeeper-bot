import discord
import asyncio

async def play(vc, file):
    vc.play(discord.FFmpegPCMAudio(source=file))
    while vc.is_playing():
        await asyncio.sleep(1)
    