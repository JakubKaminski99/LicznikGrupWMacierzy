#text = input('Input value of coins and amount e.g. "coins = [1,2,5], amount = 11')

values = [1,2]
target = 2

def loop(values, target):
    for val in values:
        target -= val
        if(target == 0):
            break
        else:
            print("d")


loop(values, target)