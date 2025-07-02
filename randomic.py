import random

r_range = random.randrange(10, 20)
print("random.randrange: ",r_range)
r_range2 = random.randrange(40, 60, 2)
print("random.randrange com step: ",r_range2)

r_int = random.randint(10, 20)
print("random.randint: ",r_int)
r_float = random.uniform(10, 20)
print("random.uniform: ",r_float)

names = ["Luiz", "Ricardo", "Filipe", "Rogério"]
random.shuffle(names)
print("Array embaralhado: " ,names)

sample = random.sample(names, k=3)
#sample = random.choices(names, k=3) ligeiramente diferente
print("Subconjunto aleatório: ", sample)