import discord
import os
import requests
import json
import random
client = discord.Client()

def get_fact():
    response = requests.get("https://uselessfacts.jsph.pl/random.json")
    json_data = json.loads(response.text)
    text = json_data['text']
    return text

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " - " + json_data[0]['a']
    return quote

@client.event
async def on_ready():
    print('I am here moth.....!'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$fact'):
        fact = get_fact()
        await message.channel.send(fact)
    if message.content.startswith('$quote'):
        quote = get_quote()
        await message.channel.send(quote)
    if message.content.startswith('$help'):
        embed = discord.Embed(
            title="Commands:",
            url="https://i.postimg.cc/T3rnr4m4/Untitled.png",
            description=""
                        "$help  - show this embed\n"
                        "$fact  - display a nice fact\n"
                        "$rank  - show server rank\n"
                        "$quote - show a random quoute",
            color=0xFF5733
        )
        await message.channel.send(embed=embed)
    if message.content.startswith('$rank'):
        points = random.randrange(3000)
        points_kintaro = points - random.randrange(20)
        embed = discord.Embed(
            title="Ranks:",
            url="https://i.postimg.cc/T3rnr4m4/Untitled.png",
            description="Ranks on this server\n\n 1. luap:\t\t" + str(points) + "\n 2. kintaro:\t\t" + str(
                points_kintaro),
            color=0xFF5733
        )
        await message.channel.send(embed=embed)


client.run(os.getenv('TOKEN'))
