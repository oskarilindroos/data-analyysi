import random

a = random.randint(0, 100)
print(a)
b = random.randint(0, 100)
print(b)

if (a > b):
    print(f'{a} on isompi')

elif (b > a):
    print(f'{b} on isompi')

else:
    print('yhtäsuuret')