import math
input = 10978
root = 0.0
rootMod = 0
done = "not final"
if input <= 0:
    print("ERROR: please enter a valid number")
else:
    mod = math.sqrt(input)
    intMod = int(mod)
    if input/intMod == intMod:
        print(f"Square Root: {intMod}") #perfect square
    else:
        def print_factors(num):
            for i in range(1, num + 1):
                outside = 1
                if num % i == 0:
                    root = math.sqrt(i)
                    rootMod = str(root)
                    length = len(rootMod)
                    zeroSpot = rootMod[length-1]
                    if zeroSpot == "0": #factor is perfect square
                        outside = root*outside
                        insideHouse = 1
                        rootSquared = root**2
                        insideSimple = input/rootSquared
                        insideHouse = insideSimple*insideHouse
                        done = f"{outside} √ {insideHouse}"
            print(done)
        print_factors(input)
