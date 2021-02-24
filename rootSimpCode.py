import math
def simp(input):
    root = 0.0
    rootMod = 0
    done = "not final"
    if input <= 0:
        print("ERROR: please enter a valid number")
    else:
        mod = math.sqrt(input)
        intMod = int(mod)
        if input/intMod == intMod:
            print(intMod) #perfect square
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
def findHyp(a,b):
    leg1 = a**2
    leg2 = b**2
    legSum = leg1+leg2
    print("The length of the hypotenuse is:")
    simp(legSum)
def findLeg(a,c):
    legA = a**2
    hyp = c**2
    legB = hyp - legA
    print("The length of the leg is:")
    simp(legB)
def unsimp(out, inner):
    outRound = out**2
    tot = outRound * inner
    print(f"the original number was {tot}")
def legHyp45(leg):
    print(f"Both legs are {leg} while the hypotenuse is {leg} √2")
def legHyp3060(leg):
    hip = leg*2
    print(f"The second leg is {leg}√3 while the hypotenuse is {hip})")
def legs3060(h):
    a = .5*h
    print(f"The first leg is equal to {a}, while the second leg is {a}√3")
#Type here v
simp(30) #simplifies square root
print("-----------")
unsimp(3,54) #unsimplifies square root. First value is outside, second is inside.
print("-----------")
findHyp(1,1) #finds hypotenuse, each value is a leg
print("-----------")
findLeg(3,12) #finds other leg (in right triangle), first value is leg, second is hypotenuse
print("-----------")
legHyp45(4) #finds the leg and hypotenuse in a 45-45-90 triangle; value entered is leg
print("-----------")
legHyp3060(12) #finds the value of the other leg and hypotenuse in a 30-60-90 triangle; enter value of shorter leg
print("-----------")
legs3060(11) #finds the length of the legs, the input is the hypotenuse
print("-----------")
#Type here ^
