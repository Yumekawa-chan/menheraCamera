import discord
import datetime
import os

TOKEN = 'MTA2MTMyODA4NTk1NTM4NzUxMw.GbOF8v.G_exgMmNavQ7BSv27UCYFtQSaxw6azzS7SGn_w'

Intents = discord.Intents.default()
Intents.members = True
Intents.message_content = True
client = discord.Client(intents=Intents)

@client.event
async def on_ready():
    print('Login process is completed.')

@client.event
async def on_message(message):
    if message.content == '/now':
        dt_now = datetime.datetime.now()
        await message.channel.send(file=discord.File(f"./images/{dt_now.hour:02}{dt_now.minute:02}.jpg"))
    if message.content[:5] == '/past':
        tmp_time = message.content[5:9]
        if not (f"{tmp_time}.jpg" in os.listdir(path='./images/')):
            await message.channel.send('Your text might be incorrect.')
        else:
            await message.channel.send(file=discord.File(f"./images/{message.content[5:9]}.jpg"))

client.run(TOKEN)