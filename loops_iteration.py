import random

soal = "yes"

while True:
    tas = random.randint(1, 6)
    print("tas ", tas, " oomad.")
    soal = input("again? yes or no: ")

    if soal == "yes":
        continue
    elif soal == "no":
        break
    else:
        print("invalid answer, bye bye.")
        break