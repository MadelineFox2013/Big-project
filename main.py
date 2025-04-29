import discord
from discord.ext import commands
from model import check_bird
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('information, please'):
        await message.channel.send("you know nature was polluted, so I will give you some informathion to save nature: 1. recycle ; 2. buy thing that you need ; 3. use electric cars ; 4.don't burn trash")
    elif message.content.startswith('what can we do?'):
        await message.channel.send("let's choose pratical idea! And make it true")   
    else:
        await message.channel.send(message.content)    




@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for file in ctx.message.attachments:
            file_name = file.filename
            await file.save(f"./images/{file.filename}")
            await ctx.send(check_bird(f"./images/{file.filename}"))
    else:
        await ctx.send("Bir fotoğraf eklemelisiniz")

bot.run("TOKENN")