import random
random_integers = random.randint(1, 10)
print(random_integers)

random_numbers_0_1=random.random() *10 # Generates a random float between 0 and 1
print(random_numbers_0_1)
random_float=random.uniform(1,10)
print(random_float)
random_tails_heads=random.randint(0,1)
if random_tails_heads==0:
    print("heads")
else:
    print("tails")