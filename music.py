# import statements
import discord
from discord.ext import commands
import youtube_dl

# creating our music class
class music(commands.Cog):
    def __init__(self, client):
        self.client = client


    # join command
    @commands.command()
    async def join(self, ctx):

        # voice channel of the user who sent the command
        channel = ctx.message.author.voice.channel

        # if the user is not in a voice channel
        if ctx.author.voice == None:
            await ctx.send("Please join a voice channel")

        # if the bot is not in a voice channel
        if ctx.voice_client is None:
            await channel.connect()
        
        # if the bot is already in a voice channel but needs to move over
        else:
            await ctx.voice_client.move_to(channel)

    # disconnect command
    @commands.command()
    async def disconnect(self, ctx):
        await ctx.voice_client.disconnect()


    # play command
    @commands.command()
    async def play(self, ctx, url):
        
        # if the bot is already playing a song, it'll stop the previous song and play the requested one
        ctx.voice_client.stop()

        # ffmpeg and ydl options
        FFMPEG = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL = {'format':"bestaudio"}
        
        voice_channel = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL) as ydl:
            information = ydl.extract_info(url, download=False)
            url_new = information['formats'][0]['url']

            # creates a stream to play the audio
            source = await discord.FFmpegOpusAudio.from_probe(url_new, **FFMPEG)
            
            # play the audio by streaming the source directly into the voice channel
            voice_channel.play(source)

    # pause command
    @commands.command()
    async def pause(self, ctx):
        await ctx.voice_client.pause()
        await ctx.send("Music is paused")

    # resume command
    @commands.command()
    async def resume(self, ctx):
        await ctx.voice_client.resume()

def setup(client):
    client.add_cog(music(client))
