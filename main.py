import discord
from discord.ext import commands
from discord import app_commands
import asyncio
import datetime

intents=discord.Intents.all()
bot=commands.Bot(command_prefix="?", intents=intents)

@bot.event
async def on_ready():
    print("The bot is ready")

@bot.event
async def on_member_join(member:discord.Member):
    channel=member.guild.get_channel(channel_id) #give the channel id where you want to welcome the members, and keep the id as integer
    embed=discord.Embed(title=f"Welcome!!!",
                        description=f"{member} you are my best friend and you are very welcome to my server, I hope you will have a great stay here...and please, don't act suspicious to me, the rest is all set!",
                        color=0x5b34eb) #and about color, this is embed color and you can use hex color picker and find a good one, then copy. It will be #000000, so make it 0x000000, no "#"
    await channel.send(f"Welcome {member.mention}", embed=embed)
    await asyncio.sleep(5)
    await member.timeout(datetime.timedelta(seconds=10))
    embed=discord.Embed(description=f"I knew it! You were looking suspicious from a very long time {member.mention}, from where have you came?!")
    await channel.send(embed=embed)
    await asyncio.sleep(10)
    embed=discord.Embed(description=f"Oh...sorry, I was wrong, you were looking suspicious...cause this is April Fool's Day {member.mention}!")
    await channel.send(embed=embed)

bot.run("YOUR_TOKEN")

"""And this is my small prank plan, it's not 1st April right now...but there's someone's birthday on 1st April, and I am planning something to make, but it won't be a Discord (if I make it for real, I am lazy)
And all set...ez bhai, kya sikha diya mujhe"""
