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

#if you want to find the length of hypotenuse:
#type "findHyp()"
#Inside type the value of leg A
#then a comma then the value of leg B

#If you want to simplify a square root:
#type "simp()"
#type the value inside the square root inside the ()

#if you want to find the length of a leg
#Type "findLeg()"
#In the () type the value of the first leg
#then a comma
#then the value of the hypotenuse


#Type here v
simp(1)
print("-----------")
findHyp(1,1)
print("-----------")
findLeg(1,2)
print("-----------")
#Type here ^
