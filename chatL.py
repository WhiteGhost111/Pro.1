import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password
def money():
    x= random.randint(1,2)
    anim = ""
    if x==1:
        anim ="orzeł"
    else:
        anim ="reszka"
    return anim
