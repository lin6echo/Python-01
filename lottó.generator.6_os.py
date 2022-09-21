import random

hatoslottó1 = random.sample(range(1,46), k=6)
hatoslottó2 = random.sample(range(1,46), k=6)
hatoslottó1.sort()
hatoslottó2.sort()
hatoslottó_számok = "Hatoslottó generált számok: {} és {}"
print(hatoslottó_számok.format(hatoslottó1, hatoslottó2))