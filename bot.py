import discord
import asyncio
import settings
from typing             import Optional
import transform

client = settings.discord_init("(PubNEO) ")

@client.command()
async def teste(ctx):
        
    await ctx.send(f"{neo}\n" for neo in transform.list_neos())

@client.event
async def on_ready():
    
    settings.message("Iniciado", "green", client.user.name, client.user.id)

client.run(settings.token)
