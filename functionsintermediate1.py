import random
def randInt(min=  0, max = 100):
    num = random.random()
    if max > 49:
        num = random.random()*0 + 49
    if min >= 50:
        num = random.random()*40+60
    if min < 40:
        num = random.random()*50 + 50
    if max > 499:
        num = random.random()*50+500
    return num
print(randInt())
print(randInt(max=50)),
print(randInt(min=50)),
print(randInt(min = 50, max = 500))