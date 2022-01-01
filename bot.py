# Gulkaran Singh
# Music Player Bot
# 2022-01-01

# import statements
import discord
from discord.ext import commands
from discord.flags import Intents
import music

cogs = [music]

# intializing JukeBot
client = commands.Bot(command_prefix = '!')

for i in range(len(cogs)):
    cogs[i].setup(client)

f = open("hidden.txt", "r")
TOKEN = f.read();
f.close()

client.run(TOKEN)
