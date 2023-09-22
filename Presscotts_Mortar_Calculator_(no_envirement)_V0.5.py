"""
Presscotts Mortar Calculator 
Made by Discord user: corruptedgingerale////steam user: Presscott
made with the help of this guide: https://steamcommunity.com/sharedfiles/filedetails/?id=1516328874
"""

"""to slice in the ditionary list======    charge0[50][2]

the tables are a dictionary with a list as the value below are the indecies of the list with there respective values
the keys for the dictionary are the range values
[
0 elevation, 
1 d-elev/per100m/dr,
2 time of flight per 100md/r,
3 time of flight,
4 azimuth crosswind corrrection of 1mps,
5 rangewind headwind 1mps m,
6 rangewind tailwind 1mps m,
7 air temp 15degree std 1 deg decline,
8 air temp 15degree std 1 deg incline,
9 air density 1pct decline,
10 air density 1pct incline
]
"""

import math
import os
import sys


def restart():
    os.execl(sys.executable, sys.executable, *sys.argv)


def getList(dict):
    list = []
    for key in dict.keys():
        list.append(key)

    return list


def checkKey(dic, key):
    if key in dic.keys():
        print("Present, ", end=" ")
        print("value =", dic[key])
    else:
        print("Not present")


"""
range calculation needs a generalized format

the gernallized form should take the result of the get list 
all is intialized
then it should simply be 
rangeCalculation(l0)
rangeCalculation(l1)
rangeCalculation(l2)

issue all values are marked and specified to generalize would cause the values to of course become generalized meaning the values assign would be over written every successive loop
solution would be to contain the whole process to  for each charge to in its own chunk which as far as i can tell taht would be a complete restructure of the last 150-200 lines of code 
"""


def rangeCalculation(x, distance, charge, count):
    count = count
    allFar = []
    allNear = []
    rangeUpper = "a"
    rangeLower = "a"
    for i in range(len(x)):
        if distance < x[i]:
            allNear.append(x[i])
        if distance > x[i]:
            allFar.append(x[i])

    if len(allFar) == 0 or len(allNear) == 0:
        # print("No valid Range in Charge 0")
        chargeTruth = False
    else:
        allFar.sort(reverse=True)
        allNear.sort(reverse=False)
        rangeUpper = allNear[0]
        rangeLower = allFar[0]
        chargeTruth = True
    if type(rangeUpper) and type(rangeLower) == int:
        farEL = charge[rangeUpper][0]
        nearEL = charge[rangeLower][0]
        avgelevation = (farEL + nearEL) / 2

    """Flight Time Calculations"""
    if chargeTruth == True:
        nearFT = charge[rangeLower][3]
        farFT = charge[rangeUpper][3]
        avgFL = (nearFT + farFT) / 2
    if chargeTruth == True:
        print(
            f" [ Charge {count} Near Elevation:{nearEL}, Far Elevation:{farEL}] \n Average Elevation for Charge {count} {avgelevation} \n Flight Time: {avgFL:.2f}S"
        )
    else:
        print(f" Charge {count} is invalid")


def gridmarks(charge0, charge1, charge2):
    count = 0
    print("*" * 90)
    print("[INPUT]")
    print("=" * 90)
    posMortar = str(
        input(
            "Enter your position (The Gridmark, 8-10 digit, no spaces or punctuation): "
        )
    )
    posTarget = str(
        input(
            "Enter your targets position (The Gridmark, 8-10 digit, no spaces or punctuation): "
        )
    )

    print("=" * 90)

    while len(posMortar) % 2 == 1 or not posMortar.isnumeric():
        print("=" * 90)
        print(
            "ERROR: The length of the gridmark is odd or it contains non-numeric characters. Please re-enter the gridmark of your position."
        )
        posMortar = str(
            input(
                "Enter your position (The Gridmark, 8-10 digits, no spaces or punctuation): "
            )
        )

    while len(posTarget) % 2 == 1 or not posTarget.isnumeric():
        print("=" * 90)
        print(
            "ERROR: The length of the gridmark is odd or it contains non-numeric characters. Please re-enter the gridmark of your target."
        )
        posTarget = str(
            input(
                "Enter your target's position (The Gridmark, 8-10 digits, no spaces or punctuation): "
            )
        )

    """
    Determining X,Y coordinates and setup for distance
    documentation for understanding:
    
    Here’s a breakdown of what each part does:
    posMortarXY = str(posMortar): Converts the posMortar variable to a string.
    mUpper = (len(posMortarXY)) / 2: Calculates the upper index for splitting the string in half.
    mUpper = int(mUpper): Converts the upper index to an integer.
    xGridM = posMortarXY[0:mUpper:1]: Extracts the first half of the string using slicing.
    posMortarX = str(xGridM): Converts the extracted first half to a string.
    posMortarX = int(posMortarX): Converts the extracted first half to an integer, representing the X coordinate of the mortar position.
    mLower = len(posMortarXY) / 2: Calculates the lower index for splitting the string in half.
    mLower = int(mLower): Converts the lower index to an integer.
    yGridM = posMortarXY[mLower::1]: Extracts the second half of the string using slicing.
    posMortarY = str(yGridM): Converts the extracted second half to a string.
    posMortarY = int(posMortarY): Converts the extracted second half to an integer, representing the Y coordinate of the mortar position.
    posTargetXY = str(posTarget): Converts the posTarget variable to a string.
    tUpper = (len(posTargetXY) / 2) + 1: Calculates the upper index for splitting the string in half, considering an additional character for proper splitting.
    tUpper = int(tUpper): Converts the upper index to an integer.
    xGridT = posTargetXY[0:mUpper:1]: Extracts the first half of the string using slicing.
    posTargetX = str(xGridT): Converts the extracted first half to a string.
    posTargetX = int(posTargetX): Converts the extracted first half to an integer, representing the X coordinate of the target position.
    tLower = len(posTargetXY) / 2: Calculates the lower index for splitting the string in half.
    tLower = int(tLower): Converts the lower index to an integer.
    yGridT = posTargetXY[mLower::1]: Extracts the second half of the string using slicing.
    posTargetY = str(yGridT): Converts the extracted second half to a string.
    posTargetY = int(posTargetY): Converts the extracted second half to an integer, representing the Y coordinate of the target position.
    """
    # the orginal and described method the current implemented is in testing
    posMortarXY = str(posMortar)
    mUpper = (len(posMortarXY)) / 2
    mUpper = int(mUpper)
    xGridM = posMortarXY[0:mUpper:1]
    posMortarX = str(xGridM)
    posMortarX = int(posMortarX)

    mLower = len(posMortarXY) / 2
    mLower = int(mLower)
    yGridM = posMortarXY[mLower::1]
    posMortarY = str(yGridM)
    posMortarY = int(posMortarY)

    posTargetXY = str(posTarget)
    tUpper = (len(posTargetXY) / 2) + 1
    tUpper = int(tUpper)
    xGridT = posTargetXY[0:mUpper:1]
    posTargetX = str(xGridT)
    posTargetX = int(posTargetX)

    tLower = len(posTargetXY) / 2
    tLower = int(tLower)
    yGridT = posTargetXY[mLower::1]
    posTargetY = str(yGridT)
    posTargetY = int(posTargetY)

    """
    #lmao the code is bad
    posMortarXY = str(posMortar)
    mUpper = len(posMortarXY) // 2
    xGridM = int(posMortarXY[:mUpper])
    posMortarX = int(xGridM)

    mLower = len(posMortarXY) // 2
    yGridM = int(posMortarXY[mLower:])
    posMortarY = int(yGridM)

    posTargetXY = str(posTarget)
    tUpper = (len(posTargetXY) // 2) + 1
    xGridT = int(posTargetXY[:tUpper])
    posTargetX = int(xGridT)

    tLower = len(posTargetXY) // 2
    yGridT = int(posTargetXY[tLower:])
    posTargetY = int(yGridT)
    """
    # print(f'tartget x{posTargetX} target y{posTargetY} \n youX {posMortarX} yourY {posMortarY} ')
    """ distance CALC"""
    dx = posTargetX - posMortarX
    # print(f'dx= {dx}')
    dy = posTargetY - posMortarY
    # print(f'dy= {dy}')
    distance = math.sqrt(dx**2 + dy**2)

    """distance unit adjuestment"""

    if len(posMortar) == 6:
        distance = 100 * distance
    if len(posMortar) == 8:
        distance = 10 * distance
    if len(posMortar) == 10:
        distance = distance
    # print(distance)
    """Determing azimuth in mills, and setting up for special cases where arctan is undefined"""
    """change "if" statement to negative check and then assign ones or zeros to do a true false"""
    # 17.77777777777777777778 is the constant used to convert degrees to mills
    azimuth = 0
    dToMills = 17.77777777777777777778
    # print (f' DX{dx}//DY{dy}')
    if dy == 0:
        if dx < 0:
            azimuth = 4800
        if dx > 0:
            azimuth = 1600
    # NE
    if dx > 0 and dy > 0:
        azimuth = dToMills * math.degrees(math.atan(dx / dy))
        # print('NE')
    # NW
    if dx < 0 and dy > 0:
        azimuth = 6400 + dToMills * math.degrees(math.atan(dx / dy))
        # print('NW')
    # SE
    if dx > 0 and dy < 0:
        azimuth = 3200 + dToMills * math.degrees(math.atan(dx / dy))
        # print('SE')
    # SW
    if dx < 0 and dy < 0:
        azimuth = 3200 + dToMills * math.degrees(math.atan(dx / dy))
        # print('SW')
    """Variable set up for elevation calculations"""
    l0 = getList(charge0)
    l1 = getList(charge1)
    l2 = getList(charge2)
    allFar = []
    allNear = []
    rangeUpper = "a"
    rangeLower = "a"
    """ l0A goes with range0B and vice versea """
    # makes sure distance is valid
    if distance > 3100 or distance < 50:
        print("ERROR: you are out of range")
        restart()

    # the below is the printed output for the "fire mission"
    print("[OUTPUT]")
    print("=" * 90)
    print(f" FIRE MISSION ")
    print(f" Azimuth: {azimuth:.2f}")
    print(f" Distance from Target {distance:.2f} Meters ")

    print(f" Elevation ranges: ")
    print("=" * 90)

    rangeCalculation(l0, distance, charge=charge0, count="0")
    print("=" * 90)
    rangeCalculation(l1, distance, charge=charge1, count="1")
    print("=" * 90)
    rangeCalculation(l2, distance, charge=charge2, count="2")

    # possible recursive main fix unsure

    main()


def polar(charge0, charge1, charge2):
    """
    a polar fire mission consists of a given bearing and a given distance such as 500m 0541mil

    in a polar coordinate mission what is given for the interpeter to enter?

    google says:
    Target Location: The FO provides the target’s location using either grid coordinates or polar coordinates 1.
    Target Description: The FO describes the target, including its type, size, and any distinguishing features that can aid in identification 2.
    Target Elevation: The FO provides the target’s elevation, which is crucial for calculating the correct mortar firing data 2.
    Target Range: The FO provides the target’s range from the mortar position, which is necessary for determining the appropriate charge and elevation settings 2.
    Target Description: The FO describes the target, including its type, size, and any distinguishing features that can aid in identification 2.
    Method of Control: The FO specifies the method of control to be used, such as “Adjust Fire” or “Fire for Effect” 3.
    Safety Information: The FO may provide additional safety information, such as friendly unit locations or any potential hazards in the vicinity of the target 3.
    """
    count = 0
    print("*" * 90)
    print("[INPUT]")
    print("=" * 90)
    Target_distance = str(
        input("Enter your the distance from you to the target in meters: ")
    )

    Target_bearing = str(
        input(
            "enter the bearing of the target in either mils or degrees (you must use leading zeros): "
        )
    )

    # target bearing conversion; dToMills = 17.77777777777777777778 is the constant used for conversion
    dToMills = 17.77777777777777777778
    if len(Target_bearing) == 4:
        average_Bearing = Target_bearing
        # since the bearing is already in mils we dont need to do anytihng
    if len(Target_bearing) == 3:
        # since this will mean that the bearing is entered in degrees we must convert it
        # bearing_win  l/u is the weill take the values of two azimuths since the will be
        # because we are scaling down there will be a level of undefined variation in mils there fore +/- dToMills
        # please note that this is a estimation so in some cases the upper or lower may be more accurate
        #however providing the middle and/or average number would is the more preferable outcome for a single output instance due to it being the middle number and a comprimise in short use mills you fukin heathen
        bearing_WinL = (Target_bearing) * dToMills
        bearing_WinU = (Target_bearing + 1) * dToMills
        average_Bearing = (bearing_WinL + bearing_WinU) / 2
    # this creates a list of all ranges in the dictionaries which will be passed to the range calc func
    l0 = getList(charge0)
    l1 = getList(charge1)
    l2 = getList(charge2)
    print("=" * 90)
    print("[OUTPUT]")
    print("=" * 90)
    print("=" * 90)
    print(f" FIRE MISSION ")
    print(f" Azimuth: {average_Bearing:.2f}")
    print(f" Distance from Target {Target_distance:.2f} Meters ")

    print(f" Elevation ranges: ")
    print("=" * 90)
    rangeCalculation(l0, distance=Target_distance, charge=charge0, count="0")
    print("=" * 90)
    rangeCalculation(l1, distance=Target_distance, charge=charge1, count="1")
    print("=" * 90)
    rangeCalculation(l2, distance=Target_distance, charge=charge2, count="2")

    polar()


def main():
    """mortar range table for reference for math"""
    charge0 = {
        50: [1547, 5, 1.4, 14.1, 7.3, 0.4, -0.3, 0, 0, 0, 0],
        100: [1493, 9, 1.4, 14.0, 3.7, 0.4, -0.3, 0, 0, 0, 0],
        150: [1438, 14, 1.4, 13.9, 2.5, 0.5, -0.4, 0, 0, -0.1, 0.1],
        200: [1381, 20, 1.4, 13.8, 1.9, 0.5, -0.4, 0, 0, -0.1, 0.1],
        250: [1321, 27, 1.5, 13.6, 1.5, 0.5, -0.4, 0, 0, -0.1, 0.1],
        300: [1256, 36, 1.6, 13.3, 1.3, 0.6, -0.4, 0.1, -0.1, -0.1, 0.1],
        350: [1183, 49, 1.7, 12.9, 1.1, 0.6, -0.5, 0.1, -0.1, -0.1, 0.1],
        400: [1097, 69, 1.9, 12.4, 0.9, 0.6, -0.5, 0.1, -0.1, -0.2, 0.2],
        450: [979, 112, 2.3, 11.6, 0.8, 0.6, -0.5, 0.1, -0.1, -0.2, 0.2],
    }
    charge1 = {
        150: [1556, 1, 0.8, 27.2, 12.3, 2.5, -2.4, 0, 0, -0.2, 0.2],
        200: [1541, 1, 0.8, 27.2, 12.3, 2.5, -2.4, 0, 0, -0.3, 0.3],
        250: [1527, 2, 0.8, 27.2, 9.9, 2.6, -2.4, 0, 0, -0.3, 0.3],
        300: [1512, 2, 0.8, 12.1, 8.2, 2.6, -2.4, 0, 0, -0.3, 0.3],
        350: [1497, 3, 0.8, 27.1, 7.1, 2.7, -2.5, 0.1, -0.1, -0.5, 0.4],
        400: [1482, 3, 0.8, 27.1, 6.2, 2.7, -2.5, 0.1, -0.1, -0.7, 0.7],
        450: [1466, 3, 0.8, 27, 5.6, 2.8, -2.5, 0.1, -0.1, -0.6, 0.6],
        500: [1451, 4, 0.8, 27, 5, 2.9, -2.6, 0.1, -0.1, -0.7, 0.6],
        550: [1436, 4, 0.8, 26.9, 4.6, 2.9, -2.6, 0.1, -0.1, -0.7, 0.7],
        600: [1420, 5, 0.8, 26.8, 4.2, 3, -2.7, 0.1, -0.1, -0.8, 0.8],
        650: [1404, 5, 0.8, 26.7, 3.9, 3, -2.7, 0.1, -0.1, -0.9, 0.8],
        700: [1388, 6, 0.8, 26.7, 3.6, 3.1, -2.8, 0.1, -0.1, -0.9, 0.9],
        750: [1372, 6, 0.8, 26.6, 3.4, 3.2, -2.8, 0.1, -0.1, -1, 1],
        800: [1355, 7, 0.8, 26.5, 3.2, 3.2, -2.9, 0.1, -0.1, -1.1, 1],
        850: [1338, 8, 0.8, 26.4, 3, 3.3, -2.9, 0.1, -0.1, -1.1, 1.1],
        900: [1321, 8, 0.8, 26.2, 2.8, 3.4, -3, 0.1, -0.1, -1.2, 1.2],
        950: [1303, 9, 0.9, 26.1, 2.7, 3.4, -3.1, 0.1, -0.1, -1.3, 1.2],
        1000: [1285, 10, 0.9, 26, 2.6, 3.5, -3.1, 0.2, -0.2, -1.4, 1.3],
        1050: [1266, 11, 0.9, 25.8, 2.4, 3.6, -3.2, 0.2, -0.2, -1.4, 1.4],
        1100: [1247, 12, 0.9, 25.6, 2.3, 3.6, -3.2, 0.2, -0.2, -1.5, 1.5],
        1150: [1227, 13, 0.9, 25.5, 2.2, 3.7, -3.3, 0.2, -0.2, -1.6, 1.5],
        1200: [1207, 14, 0.9, 25.3, 2.1, 3.7, -3.4, 0.2, -0.2, -1.7, 1.6],
        1250: [1186, 15, 1, 25, 2, 3.8, -3.4, 0.2, -0.2, -1.7, 1.7],
        1300: [1163, 17, 1, 24.8, 1.9, 3.8, -3.5, 0.2, -0.2, -1.8, 1.7],
        1350: [1140, 19, 1, 24.5, 1.9, 3.9, -3.5, 0.2, -0.2, -1.9, 1.8],
        1400: [1115, 21, 1.1, 24.2, 1.8, 3.9, -3.6, 0.2, -0.2, -1.9, 1.9],
        1450: [1088, 24, 1.1, 23.9, 1.7, 4, -3.6, 0.2, -0.2, -2, 1.9],
        1500: [1059, 27, 1.2, 23.5, 1.6, 4, -3.6, 0.2, -0.2, -2.1, 2],
        1550: [1027, 32, 1.3, 23.1, 1.5, 4, -3.7, 0.2, -0.2, -2.1, 2.1],
        1600: [991, 39, 1.4, 22.6, 1.5, 4.0, -3.7, 0.2, -0.2, -2.2, 2.1],
        1650: [947, 39, 1.4, 22.6, 1.5, 4, -3.7, 0.2, -0.2, -2.3, 2.2],
        1700: [886, 71, 2.1, 20.9, 1.3, 3.9, -3.6, 0.3, -0.3, -2.3, 2.2],
    }
    charge2 = {
        250: [1559, 1, 0.6, 37.3, 23.7, 6.1, -5.9, 0, 0, -0.6, 0.5],
        300: [1551, 1, 0.6, 37.3, 19.9, 6.1, -5.9, 0, 0, -0.7, 0.6],
        350: [1543, 1, 0.6, 37.3, 17.1, 6.2, -5.9, 0, 0, -0.8, 0.8],
        400: [1535, 1, 0.6, 37.3, 15, 6.2, -5.9, 0.1, -0.1, -0.9, 0.9],
        450: [1527, 1, 0.6, 37.2, 13.4, 6.3, -6, 0.1, -0.1, -1, 1],
        500: [1519, 1, 0.6, 37.2, 12.1, 6.3, -6, 0.1, -0.1, -1.1, 1.1],
        550: [1510, 1, 0.6, 37.2, 11, 6.4, -6, 0.1, -1, -1.3, 1.2],
        600: [1502, 1, 0.6, 37.2, 10.1, 6.4, -6.1, 0.1, -0.1, -1.4, 1.3],
        650: [1494, 1, 0.6, 37.1, 9.4, 6.5, -6.1, 0.1, -0.1, -1.5, 1.4],
        700: [1485, 2, 0.6, 37.1, 8.7, 6.5, -6.2, 0.1, -0.1, -1.6, 1.5],
        750: [1477, 2, 0.6, 37.1, 8.1, 6.6, -6.2, 0.1, -0.1, -1.7, 1.6],
        800: [1468, 2, 0.6, 37, 7.6, 6.7, -6.6, 0.1, -0.1, -1.8, 1.8],
        850: [1460, 2, 0.6, 37, 7.2, 6.7, -6.3, 0.1, -0.1, -2, 1.9],
        900: [1451, 2, 0.6, 36.9, 6.8, 6.8, -6.4, 0.1, -0.1, -2.1, 2],
        950: [1443, 2, 0.6, 36.9, 6.5, 6.9, -6.4, 0.1, -0.1, -2.2, 2.1],
        1000: [1434, 2, 0.6, 36.8, 6.1, 6.9, -6.5, 0.1, -0.1, -2.3, 2.2],
        1050: [1425, 2, 0.6, 36.8, 5.9, 7, -6.5, 0.1, -0.1, -2.4, 2.3],
        1100: [1417, 3, 0.6, 36.7, 5.6, 7.1, -6.6, 0.1, -0.1, -2.6, 2.4],
        1150: [1408, 3, 0.6, 36.7, 5.4, 7.1, -6.7, 0.2, -0.2, -2.7, 2.5],
        1200: [1399, 3, 0.6, 36.6, 5.1, 7.2, -6.7, 0.2, -0.2, -2.8, 2.7],
        1250: [1390, 3, 0.6, 36.6, 4.9, 7.3, -6.8, 0.2, -0.2, -2.9, 2.8],
        1300: [1381, 3, 0.6, 36.5, 4.8, 7.4, -6.9, 0.2, -0.2, -3, 2.9],
        1350: [1371, 3, 0.6, 36.4, 4.6, 7.4, -6.9, 0.2, -2, -3.2, 3],
        1400: [1362, 4, 0.6, 36.3, 4.4, 7.5, -7, 0.2, -0.2, -3.3, 3.1],
        1450: [1353, 4, 0.6, 36.3, 4.3, 7.6, -7.1, 0.2, -0.2, -3.4, 3.2],
        1500: [1343, 4, 0.6, 36.2, 4.1, 7.6, -7.1, 0.2, -0.2, -3.5, 3.4],
        1550: [1334, 4, 0.6, 36.1, 4, 7.7, -7.2, 0.2, -0.2, -3.7, 3.5],
        1600: [1324, 4, 0.6, 36, 3.9, 7.8, -7.3, 0.2, -0.2, -3.8, 3.6],
        1650: [1314, 4, 0.6, 35.9, 3.8, 7.9, -7.3, 0.2, -0.2, -3.9, 3.7],
        1700: [1304, 5, 0.7, 35.8, 3.7, 7.9, -7.4, 0.2, -0.2, -4, 3.8],
        1750: [1294, 5, 0.7, 35.7, 3.6, 8, -7.5, 0.2, -0.2, -4.2, 3.9],
        1800: [1284, 5, 0.7, 35.6, 3.5, 8.1, -7.5, 0.2, -0.2, -4.3, 4.1],
        1850: [1274, 5, 0.7, 35.5, 3.4, 8.1, -7.6, 0.2, -0.2, -4.4, 4.2],
        1900: [1263, 6, 0.7, 35.3, 3.3, 8.2, -7.7, 0.3, -0.3, -4.5, 4.3],
        1950: [1252, 6, 0.7, 35.2, 3.2, 8.3, -7.8, 0.3, -0.3, -4.7, 4.4],
        2000: [1242, 6, 0.7, 35.1, 3.1, 8.4, -7.8, 0.3, -0.3, -4.8, 4.5],
        2050: [1230, 7, 0.7, 34.9, 3, 8.4, -7.9, 0.3, -0.3, -4.9, 4.6],
        2100: [1219, 7, 0.7, 34.8, 2.9, 8.5, -8, 0.3, -0.3, -5, 4.8],
        2150: [1207, 7, 0.7, 34.6, 2.9, 8.5, -8, 0.3, -0.3, -5.2, 4.9],
        2200: [1196, 8, 0.7, 34.5, 2.8, 8.6, -8.1, 0.3, -0.3, -5.3, 5],
        2250: [1184, 8, 0.7, 34.3, 2.7, 8.7, -8.2, 0.3, -0.3, -5.4, 5.1],
        2300: [1171, 9, 0.8, 34.1, 2.7, 8.7, -8.2, 0.3, -0.3, -5.5, 5.2],
        2350: [1158, 9, 0.8, 33.9, 2.6, 8.8, -8.3, 0.3, -0.3, -5.7, 5.4],
        2400: [1145, 10, 0.8, 33.7, 2.5, 8.8, -8.3, 0.3, -0.3, -5.8, 5.5],
        2450: [1132, 10, 0.8, 33.5, 2.5, 8.9, -8.4, 0.3, -0.3, -5.9, 5.6],
        2500: [1118, 11, 0.8, 33.3, 2.4, 8.9, -8.4, 0.3, -0.3, -6, 5.7],
        2550: [1103, 12, 0.8, 33.1, 2.3, 9, -8.5, 0.3, -0.3, -6.1, 5.8],
        2600: [1088, 13, 0.9, 32.8, 2.3, 9, -8.5, 0.3, -0.3, -6.3, 5.9],
        2650: [1072, 14, 0.9, 32.5, 2.2, 9, -8.6, 0.4, -0.4, -6.4, 6],
        2700: [1056, 15, 0.9, 32.2, 2.2, 9, -8.6, 0.4, -0.4, -6.5, 6.1],
        2750: [1038, 16, 1, 31.9, 2.1, 9, -8.6, 0.4, -0.4, -6.6, 6.2],
        2800: [1019, 18, 1, 31.6, 2, 9, -8.6, 0.4, -0.4, -6.7, 6.4],
        2850: [999, 20, 1.1, 31.2, 2, 9, -8.6, 0.4, -0.4, -6.8, 6.4],
        2900: [978, 22, 1.1, 30.7, 1.9, 9, -8.6, 0.4, -0.4, -6.9, 6.5],
        2950: [954, 26, 1.2, 30.3, 1.9, 9, -8.6, 0.4, -0.4, -7, 6.6],
        3000: [926, 31, 1.4, 29.7, 1.8, 8.9, -8.5, 0.4, -0.4, -7.1, 6.7],
        3050: [893, 39, 1.6, 28.9, 1.7, 8.8, -8.4, 0.4, -0.4, -7.1, 6.8],
        3100: [848, 54, 2, 27.9, 1.6, 8.5, -8.2, 0.4, -0.4, -7.2, 6.8],
    }

    """
    add way for usesr to choose between polar fire and linear fire 
    """
    print("*" * 90)
    print("[CHOOSE A FIRE MISSION TYPE]")
    print("=" * 90)
    mission_determiner = str(
        input(
            "For linear missions enter 1\nFor Polar missions enter 2\nEnter Your 1 or 2: "
        )
    )
    if mission_determiner == "1":
        gridmarks(charge0, charge1, charge2)
    if mission_determiner == "2":
        polar(charge0, charge1, charge2)
    while mission_determiner != "1" or mission_determiner != "2":
        print("=" * 90)
        print("ERROR: You did not enter a valid input")
        mission_determiner = str(
            input(
                f"1 is for linear fire mission\n2 is for polar fire mission\nEnter either a 1 or a 2: "
            )
        )
        if mission_determiner == "1":
            gridmarks(charge0, charge1, charge2)
        if mission_determiner == "2":
            polar(charge0, charge1, charge2)

    main()
    """
        restart_input = input("New Fire Mission? (yes/no): ")
        if restart_input.lower() in ["yes", "y"]:
            print("New Mission...")
            restart()
        else:
            print("Exiting...")
    """


main()
