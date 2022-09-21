names = ["Csaba", "Szilvia", "Zsani", "Bogi"]
ages = [57, 53, 33, 31]
eye_colours = ["brown", "blue", "brown", "brown"]

print(list(zip(names, ages, eye_colours)))

for name, age, eye_colour in zip(names, ages, eye_colours):
    if age < 32:
        print(name)
    print(eye_colour)