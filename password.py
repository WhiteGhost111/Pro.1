import random

def gpassword(length=10):
    
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=-"
    
    
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password


length = int(input("Podaj długość hasła: "))
password = gpassword(length)
print("Wygenerowane hasło:", password)
