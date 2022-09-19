from random import randint


def dice_roll(rollnumber, sidenumber):
    result = []
    for _ in range(rollnumber):
        roll = randint(1, sidenumber)
        result.append(str(roll))

    output = ",".join(result)
    print(output)

    return output
