"""
Made by: xenArtemis, xenJudas
disclaimer: We're not that good at Aiohttp :(
"""

# imports #

import aiohttp
import discord
from discord.ext import commands

penny = "" # token here
headers = {'authorization': f'Bot {penny}', "Content-Type": "application/json"} # sets headers and sets content type to json

nexus = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@nexus.event
async def on_ready():
    nexus.session = aiohttp.ClientSession() # initializes aiohttp session
    print("diddy the diddle nigga")

@nexus.command()
async def delchan(ctx):
    for channel in ctx.guild.channels:
        delurl = f"https://discord.com/api/v9/channels/{channel.id}" # channel endpoint
        async with nexus.session.delete(delurl, headers=headers): # sends a delete request to delete the channels thingy
            print(f"deleted {channel.id}")

@nexus.command()
async def createchan(ctx):
    for i in range(100):
        channelname = "test"
        createurl = f"https://discord.com/api/v9/guilds/{ctx.guild.id}/channels" # channel endpoint
        setup = {"name": channelname, "type": 0} # setup for the channel creation request
        async with nexus.session.post(createurl, headers=headers, json=setup): # sends a post request to create the channels
            print(f"created {channelname}")

# adding more later :) #

nexus.run(penny)
