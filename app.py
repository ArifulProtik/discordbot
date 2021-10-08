import discord
from discord.colour import Color
from discord.ext import commands
from discord import Member
from discord.ext.commands import has_permissions, CheckFailure, MissingPermissions
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
    await bot.process_commands(message)



@bot.command()
@has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member=None, *, reason=None):
    if member == None:
        await ctx.send("You Have to Mention a Member")
        return
    if reason == None:
        reason = "No reason specified!!"
    try:
        await member.kick(reason=reason)
        await ctx.send(f"{member} kicked From the Server")
    except:
        await ctx.send("You Dont Have permission to Kick or Ban")

@bot.command()
@has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member=None, *, reason=None):
    if member == None:
        await ctx.send("You Have to Mention a Member")
        return
    if reason == None:
        reason = "No reason specified!!"
    try:
        await member.ban(reason=reason)
        await ctx.send(f"{member} banned From the Server")
    except:
        await ctx.send("You Dont Have permission to Kick or Ban")









bot.run(os.getenv('KEY'))