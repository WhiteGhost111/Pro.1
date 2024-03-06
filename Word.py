meme_dict = {
            "LOL":"odpowiedź na coś zabawnego",
            "CRINGE": "coś dziwnego lub wstydliwego",
            "ROFL": "odpowiedź na żart",
            "SHEESH": "lekka dezaprobata",
            "CREEPY": "straszny, złowieszczy",
            "AGGRO": "stać się agresywnym/zły ",
            "REL": "coś, z czym możemy się utożsamić  ",
            }
print("cześć, witaj w naszym słowniczku!!")
word = input("Wpisz słowo, którego nie rozumiesz (używaj wielkich liter!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("nawet my nie wiemy co to znaczy :( ")
