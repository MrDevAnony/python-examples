import random

soal = "yes"

while soal=="yes":
    tas = random.randint(1, 6)
    print("tas", tas, "oomad.")
    soal = input("again? yes or no: ").lower()

    if soal not in  ["yes", "no"]:
        print("invalid answer, bye bye.")
