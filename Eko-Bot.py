import discord
import random
from setting import settings
# Zmienna intencje przechowuje uprawnienia bota
intents = discord.Intents.default()
# Włączanie uprawnienia do czytania wiadomości
intents.message_content = True
# Tworzenie bota w zmiennej klienta i przekazanie mu uprawnień
client = discord.Client(intents=intents)
propc= {
    1: "Statystyczny Polak wytwarza ponad 320 kg śmieci rocznie. Z tego na wysypiska ląduje ponad 12 milionów ton odpadów, natomiast aż 98% można by wykorzystać poprzez segregację.",
    2: "Szacuje się, że 35 butelek plastikowych wystarczy, by wyprodukować jedną bluzę polarową. Uzyskane z butelek włókno poliestrowe stanowi znakomity materiał do wyrobu m.in. plecaków, namiotów czy butów.",
    3: "Każda szklana butelka ponownie wprowadzona do obiegu pozwala zaoszczędzić energię potrzebną do świecenia 100 watowej żarówki przez 4 godziny.",
    4: " Każde 100 kg papieru to średniej wielkości dwa drzewa, przy czym należy wiedzieć, że jedno drzewo produkuje w ciągu roku tlen wystarczający dla 10 osób.",
    5: "Możemy „uratować sześciometrową sosnę, jeżeli poddamy recyklingowi stos makulatury o wysokości sto dwudziestu pięciu centymetrów.",
    6: "Stal i aluminium pochodzące z odzysku z opakowań metalowych można przetwarzać w nieskończoność i to bez utraty surowca.",
    7: "Aby uzyskać jedną tonę papieru musi zostać ścięte aż siedemnaście drzew."}
propj = { 
    1 : "Idąc na zakupy zabieraj ze sobą torby wielokrotnego użytku, najlepiej wykonane z materiałów ekologicznych.",
    2 : "Jeżeli już weźmiesz ze sklepu torbę foliową, zanim ją wyrzucisz wykorzystaj ją w gospodarstwie domowym np. do pakowania i przechowywania, albo jako torbę na śmieci.",
    3 : "Kupuj tyle, ile naprawdę potrzebujesz.",
    4 : "Wybieraj produkty w dużych opakowaniach.",
    5 : "Zamiast zwykłych, jednorazowych baterii stosuj akumulatorki, które można wielokrotnie ładować.",
    6 : "Unikaj produktów zapakowanych  w wiele warstw opakowań.",
    7 : "Jeśli masz przydomowy ogródek, kompostuj odpady.",

}
czas = {
    1 : "Papier: Około 2-5 miesięcy. Papier jest materiałem biodegradowalnym, który może szybko ulec rozkładowi w odpowiednich warunkach.",
    2 : "Karton: Około 3 miesięcy do 2 lata. Podobnie jak papier, karton jest materiałem biodegradowalnym, ale może się rozkładać wolniej ze względu na swoją gęstszą strukturę.",
    3 : "Owoce i warzywa: Około 1-6 tygodni. Owoce i warzywa są organicznymi materiałami, które mogą szybko się rozkładać pod wpływem naturalnych procesów.",
    4 : "Plastik: Plastik może się rozkładać od kilkudziesięciu lat do ponad tysiąca lat, w zależności od rodzaju plastiku i warunków środowiskowych. Niektóre rodzaje plastiku są trudne do rozłożenia przez naturalne procesy, co sprawia, że ​​ich rozkład trwa bardzo długo.",
    5 : "Styropian: Styropian może się rozkładać od kilku dziesięciu lat do ponad tysiąca lat. Jest to materiał sztuczny, który jest bardzo trudny do rozłożenia przez naturalne procesy biodegradacji.",
    6 : "Metal: Metale, takie jak aluminium i stal, mogą przetrwać setki lub nawet tysiące lat. Jednakże, mogą być one poddane recyklingowi, co pozwala na odzyskanie i ponowne wykorzystanie surowców metalicznych." ,

}
@client.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {client.user}')


   
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!hello'):
        await message.channel.send("Cześć!, wybierz co cię interesuje:")
        await message.channel.send("ciekawostki, jak zapobiegać, czas rozkładu")
        await message.channel.send("Pamiętaj aby przed wyborzem napisać  !  ")

    elif message.content.startswith('!jak zapobiegać'):
        los_k = random.choice(list(propj.keys()))
        propozycj = propj[los_k]
        await message.channel.send(propozycj)

    elif message.content.startswith('!ciekawostki'):
        los_k = random.choice(list(propc.keys()))
        propozycja = propc[los_k]
        await message.channel.send(propozycja)
    
    elif message.content.startswith('!czas rozkładu'):
        los_k = random.choice(list(czas.keys()))
        propozycja = czas[los_k]
        await message.channel.send(propozycja)
    
        
    else:
        await message.channel.send(message.content)

client.run(settings["TOKEN"])
