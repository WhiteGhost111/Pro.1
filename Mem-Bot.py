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
