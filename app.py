import discord
from discord.colour import Color
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv() 

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Room(0) [$]'))
    print('We have logged in as {0.user}'.format(bot))



@bot.event
async def on_member_join(member):
    print("Some One Joined")
    userAvatar = member.avatar_url
    embed = discord.Embed(
        title=f"Welcome!!!!",
        description=f"আরে আপনি? {member.mention} আসছেন? স্বাগতম স্বাগতম!".format(member),
        color=discord.Color.green(),


    ).set_image(url=userAvatar).set_footer(text="from BungaBot By Room(0)")
    ## Get System Channel
    system_channel = member.guild.system_channel
    await system_channel.send(embed = embed)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('$bunga'):
        await message.channel.send('Bunga Bunga!')






bot.run(os.getenv('KEY'))