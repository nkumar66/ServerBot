import discord
from discord.channel import TextChannel
from discord.ext import commands
import os

my_secret = os.environ['TOKEN']
#intents = discord.Intents.all()
#client = discord.Client(intents=intents)

intents = discord.Intents.default()
intents.members = True
#client = commands.Bot(command_prefix="!", intents=intents)
client = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.command()
async def hello(ctx):
  await ctx.send('Hello!')


@client.event
async def on_member_join(member):
  channel = client.get_channel(640361794182840332)
  await channel.send("Welcome! Thank you for joining the server!")


@client.event
async def on_member_remove(member):
  channel = client.get_channel(640361794182840332)
  await channel.send("Goodbye! We hope to see you again!")


@client.command(pass_context=True)
async def join(ctx):
  if (ctx.author.voice):
    channel = ctx.message.author.voice.channel
    await channel.connect()
  else:
    await ctx.send("You are not in a voice channel!")


@client.command(pass_context=True)
async def leave(ctx):
  if (ctx.voice_client):
    await ctx.guild.voice_client.disconnect()
    await ctx.send("Left voice channel!")
  else:
    await ctx.send("I am not in a voice channel!")


client.run(my_secret)
