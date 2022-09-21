import random

ötöslottó1 = random.sample(range(1,91), k=5)
ötöslottó2 = random.sample(range(1,91), k=5)
ötöslottó1.sort()
ötöslottó2.sort()
ötöslottó_számok = "Ötöslottó generált számok: {} és {}"
print(ötöslottó_számok.format(ötöslottó1, ötöslottó2))