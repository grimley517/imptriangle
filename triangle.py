import math

ACCURACY = 10**-14

def cos(x):
    x =math.radians(x)
    x = math.cos(x)
    return (x)

def sin(x):
    x =math.radians(x)
    x = math.sin(x)
    return (x)

def checkInt(floatToChk):
    intver = int(floatToChk)
    zero = math.fabs(floatToChk - intver)
    return (zero < ACCURACY)

def getB(length):
    x=length*cos(60)
    y=length*sin(60)
    return (x,y)

def getC(length):
    x=0
    y=length
    return (x,y)

def testIntCoOrds(x,y):
    return (checkInt(x) and checkInt(y))

def done():
    return (testIntCoOrds(B[0],B[1]) and testIntCoOrds(C[0],C[1]))
    
def getCoords(length):
    B = getB(length)
    C = getC(length)


B = (0,0)
C = (0,0)
length = 1
getCoords(length)
while done():
    length += 1
    getCoords(length)
print(B)
print(C)
    