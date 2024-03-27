import discord
from settings import settings
from bot_logic import gen_pass
from bot_logic import money
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
async def on_ready():
    await client.change_presence(status=discord.Status.Online)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Cześć!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    elif message.content.startswith('pif'):
        await message.channel.send("aa")
    elif message.content.startswith('password'):
        await message.channel.send(gen_pass)
    elif message.content.startswith('$moneta'):
        await message.channel.send("@")
    else:
        await message.channel.send(message.content)

client.run("TOKEN")
