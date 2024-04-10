import discord
from discord.ext import commands
import random
from settings import setting
import os
import asyncio
import requests
description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

#@bot.command()
#async def mem(ctx):
 ##   with open('images/mem1.jpg', 'rb') as f:
 #       # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
#        picture = discord.File(f)
# Możemy następnie wysłać ten plik jako parametr!
 #   await ctx.send(file=picture)

@bot.command()
async def mem(ctx):
    images_folder = 'images'
    images = [os.path.join(images_folder, image) for image in os.listdir(images_folder) if image.endswith(('.jpg',))]
    
    if images:
        random_image = random.choice(images)
        with open(random_image, 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    else:
        await ctx.send("Brak obrazów w folderze images.")  

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Po wywołaniu polecenia duck program wywołuje funkcję get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

bot.run(setting['TOKEN'])
