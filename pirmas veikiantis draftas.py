import random

word_list = ["stalas", "gele", "gitara"]
spejamas_zodis = random.choice(word_list)
nematomas_zodis = "_" * len(spejamas_zodis)
bandymai = 5
print("Žaidimas 'Kartuvės'. Turite 5 bandymus atspėti žodį. Sėkmės !")




while True:

    print(nematomas_zodis)
    spejimas = input("Spėkite raidę: ")
    for raide in range(len(spejamas_zodis)):
        if spejamas_zodis[raide] == spejimas:
            nematomas_zodis = nematomas_zodis[:raide] + spejamas_zodis[raide] + nematomas_zodis[raide + 1:]
    if spejimas in spejamas_zodis:
        print(f"\nAtspėjai! Raidė '{spejimas}' yra šiame žodyje.")
    else:
        bandymai -= 1
        print(f"\nNeatspėjai. Raidės '{spejimas}' šiame žodyje nėra. Liko {bandymai} bandymai.")

    if spejamas_zodis == nematomas_zodis:
        print(f"Laimėjai ! Žodis atspėtas")
        break
    elif bandymai == 0:
        print("Pralaimėjai ! Nebeliko bandymų")
        break