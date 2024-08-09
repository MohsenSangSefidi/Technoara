from random import randint


def verify_code(count=6):
    var = ''
    for item in range(0, count + 1):
        num = randint(1, 9)
        var += str(num)
    return var
