# This example requires the 'message_content' privileged intents

import os
import discord
from discord.ext import commands
from jobs import Get_Jobs
import time
import datetime as dt


client = discord.Client(intents=discord.Intents.default())


#print(os.environ.get('TOKEN'))

@client.event
async def on_ready():
    channel = client.get_channel(1071975520385904720)
    i = 0
    #send 5 jobs every 3 days
    while i < 5:
        await channel.send(Get_Jobs[i])
        i += 1
        time.sleep(259200)
    
    
    

client.run(os.environ["DISCORD_TOKEN"])

