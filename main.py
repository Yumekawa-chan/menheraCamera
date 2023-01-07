import discord
import cv2

TOKEN = 'MTA2MTMyODA4NTk1NTM4NzUxMw.GbOF8v.G_exgMmNavQ7BSv27UCYFtQSaxw6azzS7SGn_w'
cap = cv2.VideoCapture(0)

Intents = discord.Intents.default()
Intents.members = True
client = discord.Client(intents=Intents)

@client.event
async def on_ready():
    print('Login process is completed.')

@client.event
async def on_message(message):
    if message.content == '彼氏':
        for i in range(10):
            ret,frame = cap.read()
        cv2.imwrite("./images/img.jpg",frame)
        cap.release()
        await message.channel.send(file=discord.File("./images/img.jpg"))
        

client.run(TOKEN)