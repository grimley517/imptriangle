import math

ACCURACY = 10**(-1)

def cos(x):
    x =math.radians(x)
    x = math.cos(x)
    return (x)

def sin(x):
    x =math.radians(x)
    x = math.sin(x)
    return (x)

def getLength(pA,pB):
    xdist = pA[0]-pB[0]
    ydist = pA[1] -pB[1]
    length = math.hypot(xdist, ydist)
    return (length)

def getAngle(pA, pB):
    xdist = pA[0]-pB[0]
    ydist = pA[1] -pB[1]
    angle = ydist/xdist
    angle = math.atan2(ydist, xdist)
    angle = math.degrees(angle)
    return(angle)


def checkInt(floatToChk):
    intver = int(floatToChk)
    zero = math.fabs(floatToChk - intver)
    return (zero < ACCURACY)

def findC(pA, pB):
    '''finds point C given two points pA and pB suct that ABC is equilateral'''
    length = getLength(pA,pB)
    angle = getAngle(pA,pB)
    angle += 60
    C = (length * cos(angle), length * sin(angle))
    return (C)

def testIntCoOrds(x,y):
    return (checkInt(x) and checkInt(y))

def run():
    return (testIntCoOrds(B[0],B[1]) and testIntCoOrds(C[0],C[1]))



A = (0,0)
i = 1
j = 0
B = (i,j)
C = findC(A, B)
while run():
    if j>i:
        j=0
        i+=1
    else:
        j+=1
    B = i,j
    C = findC(A, B)
print(B)
print(C)
input()
