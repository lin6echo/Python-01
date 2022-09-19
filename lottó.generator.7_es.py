import random

skandi1 = random.sample(range(1,36), k=7)
skandi2 = random.sample(range(1,36), k=7)
skandi1.sort()
skandi2.sort()
skandi_számok = "Skandi generált számok: {} és {}"
print(skandi_számok.format(skandi1,skandi2))