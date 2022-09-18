import random

# ötös lottó
ötöslottó1 = random.sample(range(1,91), k=5)
ötöslottó2 = random.sample(range(1,91), k=5)
ötöslottó1.sort()
ötöslottó2.sort()
ötöslottó_számok = "Ötöslottó generált számok: {} és {}"
print(ötöslottó_számok.format(ötöslottó1, ötöslottó2))

# hatos lottó
hatoslottó1 = random.sample(range(1,46), k=6)
hatoslottó2 = random.sample(range(1,46), k=6)
hatoslottó1.sort()
hatoslottó2.sort()
hatoslottó_számok = "Hatoslottó generált számok: {} és {}"
print(hatoslottó_számok.format(hatoslottó1, hatoslottó2))

#skandi
skandi1 = random.sample(range(1,36), k=7)
skandi2 = random.sample(range(1,36), k=7)
skandi1.sort()
skandi2.sort()
skandi_számok = "Skandi generált számok: {} és {}"
print(skandi_számok.format(skandi1,skandi2))
