# Zmienna intencje przechowuje uprawnienia bota
intents = discord.Intents.default()
# Włączanie uprawnienia do czytania wiadomości
intents.message_content = True
# Tworzenie bota w zmiennej klienta i przekazanie mu uprawnień
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {client.user}')


   
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Cześć!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    #elif message.content.startswith('$password'):
        #await message.channel.send(haslo(10))
    elif message.content.startswith('co tam'):
        await message.channel.send("nie narzekam")
    elif  message.content.startswith('$heh'):
        if len(message.content) > 4:
            count_heh = int(message.content[4:])
        else:
            count_heh = 5
        await message.channel.send("he" * count_heh)
#    elif message.content.startswith('$guess'):    - Dodanie gry 
#          await message.channel.send('Guess a number between 1 and 10.')
#    
#           def is_correct(m):
#               return m.author == message.author and m.content.isdigit()
#
#           answer = random.randint(1, 10)
#
#           try:
#               guess = await self.wait_for('message', check=is_correct, timeout=5.0)    - błąd "self"
#           except asyncio.TimeoutError:                                                 - Błąd "asyncio"
#               return await message.channel.send(f'Sorry, you took too long it was {answer}.')
#
#           if int(guess.content) == answer:
#               await message.channel.send('You are right!')
#            else:
#                await message.channel.send(f'Oops. It is actually {answer}.')
    else:
        await message.channel.send(message.content)

client.run(setting["TOKEN"])
