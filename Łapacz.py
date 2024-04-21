import random

WIDTH = 600  # szeoko
HEIGHT = 300  # wysokość
FPS = 55

tlo = Actor("tlo")
kosz = Actor("kosz")
kosz.pos = (300, 300)
enemies = []
tlo1 = Actor("tlo1")
gra = Actor("gra")
gra.pos = (300, 50)
kol = Actor("kolekcja")
kol.pos = (300, 150)
sk = Actor("sklep")
sk.pos = (300, 250)
po = Actor("poma", (100, 150))
tru = Actor("trus", (500, 150))
x = Actor("cross", (580, 20))
banan = Actor("banana", (300, 150))
banan1 = Actor("banana", (300, 150))

punkty = 0
kasa = 200
mode = "menu"

for i in range(1):  # tworzenie owoców
    w = random.randint(0, 600)
    y = random.randint(-300, -50)

    enemy = Actor("banana2", (w, y))
    enemy.speed = random.randint(6, 9)
    enemies.append(enemy)
animals = [banan]


def draw():  # rysowane
    if mode == "game":
        tlo.draw()
        kosz.draw()
        screen.draw.text("wynik    ", center=(50, 20), color="white", fontsize=36)
        screen.draw.text(str(punkty), center=(110, 20), color="white", fontsize=36)
        screen.draw.text("monety   ", center=(50, 50), color="white", fontsize=36)
        screen.draw.text(str(kasa), center=(110, 50), color="white", fontsize=36)
        x.draw()
        for i in range(len(enemies)):
            enemies[i].draw()
    elif mode == "menu":

        tlo1.draw()
        gra.draw()
        kol.draw()
        sk.draw()
        screen.draw.text("monety    ", center=(50, 50), color="white", fontsize=36)
        screen.draw.text(str(kasa), center=(110, 50), color="white", fontsize=36)
        screen.draw.text("wynik     ", center=(50, 20), color="white", fontsize=36)
        screen.draw.text(str(punkty), center=(110, 20), color="white", fontsize=36)
    elif mode == "shop":
        tlo.draw()
        po.draw()
        screen.draw.text("50 monet", center=(100, 250), color="white", fontsize=36)
        tru.draw()
        screen.draw.text("100 monet", center=(500, 250), color="white", fontsize=36)
        x.draw()
        screen.draw.text("monety", center=(50, 20), color="white", fontsize=36)
        screen.draw.text(str(kasa), center=(110, 20), color="white", fontsize=36)

    elif mode == "collection":
        tlo.draw()
        x.draw()
        banan1.draw()
        for i in range(len(animals)):
            animals[i].draw()

        screen.draw.text("monety", center=(50, 20), color="white", fontsize=36)
        screen.draw.text(str(kasa), center=(110, 20), color="white", fontsize=36)


def new_enemy():  # nowe owocki

    x = random.randint(100, 500)
    y = -50
    enemy = Actor("banana2", (x, y))

    if owoc == "pom":
        enemy.image = "orange"
    elif owoc == "tru":
        enemy.image = "tr"
    elif owoc == "ba":
        enemy.image = "banana2"
    enemy.speed = random.randint(4, 6)
    enemies.append(enemy)


def enemy_ship():  # spadanie owocków
    for i in range(len(enemies)):
        if enemies[i].y < 450:
            enemies[i].y += enemies[i].speed
        else:
            enemies.pop(i)
            new_enemy()


def collision():
    global punkty
    global kasa
    if mode == "game":
        for i in range(len(enemies)):
            if kosz.colliderect(enemies[i]):
                punkty += 1
                kasa += 1
                enemies.pop(i)
                new_enemy()
                break


def update(dt):
    global mode
    enemy_ship()
    collision()
    if keyboard.a or keyboard.left and kosz.x > 30:
        kosz.x -= 5
    if keyboard.d or keyboard.right and kosz.x < 570:
        kosz.x += 5
    if mode == "game":
        for i in range(len(enemies)):
            if enemies[i].y > 300:
                mode = "menu"


owoc = "banan"


def on_mouse_down(button, pos):
    global mode
    global punkty
    global kasa, owoc
    if mode == "menu" and button == mouse.LEFT:
        if gra.collidepoint(pos):
            mode = "game"
            punkty = 0
        elif sk.collidepoint(pos):
            mode = "shop"
        elif kol.collidepoint(pos):
            mode = "collection"
    elif x.collidepoint(pos):
        mode = "menu"

    elif po.collidepoint(pos) and mode == "shop":  # po=pomarańcza
        if kasa >= 50:
            owoc = "pom"
            kasa -= 50
            animals.append(po)
        # Wybór trusk
    elif tru.collidepoint(pos) and mode == "shop":
        if kasa >= 100:
            owoc = "tru"

            kasa -= 100
            animals.append(tru)
    elif banan1.collidepoint(pos) and mode == "collection":
        owoc = "ba"
    elif po.collidepoint(pos) and mode == "collection":
        owoc = "pom"
    elif tru.collidepoint(pos) and mode == "collection":
        owoc = "tru"
