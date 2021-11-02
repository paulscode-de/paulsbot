import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print('I am here moth.....!'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startwith('$what'):
        await message.channel.send('WHAT DID I JUST SAY MF?')


client.run(os.getenv('TOKEN'))
