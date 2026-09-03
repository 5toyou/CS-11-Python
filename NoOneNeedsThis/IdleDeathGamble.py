import random

tickets = 1000

print("if you need more tickets press 1")


while True:
    slot1 = random.randint(1,9)
    slot2 = random.randint(1,9)
    slot3 = random.randint(1,9)

    print(f"You have {tickets} tickets")

    choice = input("Press Enter to roll: ")
    match choice:
        case "":
            if tickets <= 0:
                print()
                print("Out of tickets")
                print()
            if tickets >= 100:
                tickets -= 100
                if slot1 == slot2 == slot3:
                    tickets += 10000
                    print("  JACKPOT")
                    print(f" = {slot1} {slot2} {slot3} = ")
                    print("  JACKPOT")
                else:
                    print()
                    print(f" = {slot1} {slot2} {slot3} = ")
                    print()

        case "1":
            tickets += 1000
            print("You got 1000 tickets")

        case _:
            print("99.9% of gamblers quit before hitting it big")
            break

    