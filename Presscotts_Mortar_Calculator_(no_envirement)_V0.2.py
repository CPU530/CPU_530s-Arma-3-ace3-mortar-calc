'''
Presscotts Mortar Calculator 
Made by Discord user: corrupted ginger ale#144////steam user: CPU 530
made with the help of this guide: https://steamcommunity.com/sharedfiles/filedetails/?id=1516328874
'''

'''to slice in the ditionary list======    charge0[50][2]
list ins dictionary is as follows
   [elevation, 
   d-elev/per100m/dr, 
time of flight per 100md/r, 
time of flight, 
azimuth crosswind corrrection of 1mps, 
rangewind headwind 1mps m,
rangewind tailwind 1mps m,
air temp 15degree std 1 deg decline, 
air temp 15degree std 1 deg incline,
air density 1pct decline,
   air density 1pct incline]
'''

import math 
def getList(dict):
    list = []
    for key in dict.keys():
        list.append(key)
         
    return list
def checkKey(dic, key):
    if key in dic.keys():
        print("Present, ", end =" ")
        print("value =", dic[key])
    else:
        print("Not present")
        

def main():
    '''mortar range table for reference for math'''
    charge0 = {
      50 : [ 1547, 5, 1.4, 14.1, 7.3, .4, -.3, 0, 0, 0, 0 ],
      100 : [ 1493, 9, 1.4, 14.0, 3.7, .4, -.3, 0, 0, 0, 0 ],
      150 : [ 1438, 14, 1.4, 13.9, 2.5, .5, -.4, 0, 0, -.1, .1],
      200 : [ 1381, 20, 1.4, 13.8, 1.9, .5, -.4, 0, 0, -.1, .1],
      250 : [ 1321, 27, 1.5, 13.6, 1.5, .5, -.4, 0, 0, -.1, .1],
      300 : [ 1256, 36, 1.6, 13.3, 1.3, .6, -.4, .1, -.1, -.1, .1],
      350 : [ 1183, 49, 1.7, 12.9, 1.1, .6, -.5, .1, -.1, -.1, .1],
      400 : [ 1097, 69, 1.9, 12.4, .9, .6, -.5, .1, -.1, -.2, .2],
      450 : [ 979, 112, 2.3, 11.6, .8, .6, -.5, .1, -.1, -.2, .2]
       }
    charge1 = {
      150 : [ 1556, 1, .8, 27.2, 12.3, 2.5, -2.4, 0, 0, -.2, .2],
      200 : [ 1541, 1, .8, 27.2, 12.3, 2.5, -2.4, 0, 0, -.3, .3],
      250 : [ 1527, 2, .8, 27.2, 9.9, 2.6, -2.4, 0, 0, -.3, .3],
      300 : [ 1512, 2, .8, 12.1, 8.2, 2.6, -2.4, 0, 0, -.3, .3],
      350 : [ 1497, 3, .8, 27.1, 7.1, 2.7, -2.5, .1, -.1, -.5, .4],
      400 : [ 1482, 3, .8, 27.1, 6.2, 2.7, -2.5, .1, -.1, -.7, .7],
      450 : [ 1466, 3, .8, 27, 5.6, 2.8, -2.5, .1, -.1, -.6, .6],
      500 : [ 1451, 4, .8, 27, 5, 2.9, -2.6, .1, -.1, -.7, .6],
      550 : [ 1436, 4, .8, 26.9, 4.6, 2.9, -2.6, .1, -.1, -.7, .7],
      600 : [ 1420, 5, .8, 26.8, 4.2, 3, -2.7, .1, -.1, -.8, .8],
      650 : [ 1404, 5, .8, 26.7, 3.9, 3, -2.7, .1, -.1, -.9, .8],
      700 : [ 1388, 6, .8, 26.7, 3.6, 3.1, -2.8, .1, -.1, -.9, .9],
      750 : [ 1372, 6, .8, 26.6, 3.4, 3.2, -2.8, .1, -.1, -1, 1],
      800 : [ 1355, 7, .8, 26.5, 3.2, 3.2, -2.9, .1, -.1, -1.1, 1],
      850 : [ 1338, 8, .8, 26.4, 3, 3.3, -2.9, .1, -.1, -1.1, 1.1],
      900 : [ 1321, 8, .8, 26.2, 2.8, 3.4, -3, .1, -.1, -1.2, 1.2],
      950 : [ 1303, 9, .9, 26.1, 2.7, 3.4, -3.1, .1, -.1, -1.3, 1.2],
      1000 : [ 1285, 10, .9, 26, 2.6, 3.5, -3.1, .2, -.2, -1.4, 1.3],
      1050 : [ 1266, 11, .9, 25.8, 2.4, 3.6, -3.2, .2, -.2, -1.4, 1.4],
      1100 : [ 1247, 12, .9, 25.6, 2.3, 3.6, -3.2, .2, -.2, -1.5, 1.5],
      1150 : [ 1227, 13, .9, 25.5, 2.2, 3.7, -3.3, .2, -.2, -1.6, 1.5],
      1200 : [ 1207, 14, .9, 25.3, 2.1, 3.7, -3.4, .2, -.2, -1.7, 1.6],
      1250 : [ 1186, 15, 1, 25, 2, 3.8, -3.4, .2, -.2, -1.7, 1.7],
      1300 : [ 1163, 17, 1, 24.8, 1.9, 3.8, -3.5, .2, -.2, -1.8, 1.7],
      1350 : [ 1140, 19, 1, 24.5, 1.9, 3.9, -3.5, .2, -.2, -1.9, 1.8],
      1400 : [ 1115, 21, 1.1, 24.2, 1.8, 3.9, -3.6, .2, -.2, -1.9, 1.9],
      1450 : [ 1088, 24, 1.1, 23.9, 1.7, 4, -3.6, .2, -.2, -2, 1.9],
      1500 : [ 1059, 27, 1.2, 23.5, 1.6, 4, -3.6, .2, -.2, -2.1, 2],
      1550 : [ 1027, 32, 1.3, 23.1, 1.5, 4, -3.7, .2, -.2, -2.1, 2.1],
      1600 : [ 991, 39, 1.4, 22.6, 1.5, 4.0, -3.7, .2, -.2, -2.2, 2.1],
      1650 : [ 947, 39, 1.4, 22.6, 1.5, 4, -3.7, .2, -.2, -2.3, 2.2],
      1700 : [ 886, 71, 2.1, 20.9, 1.3, 3.9, -3.6, .3, -.3, -2.3, 2.2]
      }
              
    charge2 = {
        250 : [ 1559, 1, .6, 37.3, 23.7, 6.1, -5.9, 0, 0, -.6, .5],
        300 : [ 1551, 1, .6, 37.3, 19.9, 6.1, -5.9, 0, 0, -.7, .6],
        350 : [ 1543, 1, .6, 37.3, 17.1, 6.2, -5.9, 0, 0, -.8, .8],
        400 : [ 1535, 1, .6, 37.3, 15, 6.2, -5.9, .1, -.1, -.9, .9],
        450 : [ 1527, 1, .6, 37.2, 13.4, 6.3, -6, .1, -.1, -1, 1],
        500 : [ 1519, 1, .6, 37.2, 12.1, 6.3, -6, .1, -.1, -1.1, 1.1],
        550 : [ 1510, 1, .6, 37.2, 11, 6.4, -6, .1, -1, -1.3, 1.2],
        600 : [ 1502, 1, .6, 37.2, 10.1, 6.4, -6.1, .1, -.1, -1.4, 1.3],
        650 : [ 1494, 1, .6, 37.1, 9.4, 6.5, -6.1, .1, -.1, -1.5, 1.4],
        700 : [ 1485, 2, .6, 37.1, 8.7, 6.5, -6.2, .1, -.1, -1.6, 1.5],
        750 : [ 1477, 2, .6, 37.1, 8.1, 6.6, -6.2, .1, -.1, -1.7, 1.6],
        800 : [ 1468, 2, .6, 37, 7.6, 6.7, -6.6, .1, -.1, -1.8, 1.8],
        850 : [ 1460, 2, .6, 37, 7.2, 6.7, -6.3, .1, -.1, -2, 1.9],
        900 : [ 1451, 2, .6, 36.9, 6.8, 6.8, -6.4, .1, -.1, -2.1, 2],
        950 : [ 1443, 2, .6, 36.9, 6.5, 6.9, -6.4, .1, -.1, -2.2, 2.1],
        1000 : [ 1434, 2, .6, 36.8, 6.1, 6.9, -6.5, .1, -.1, -2.3, 2.2],
        1050 : [ 1425, 2, .6, 36.8, 5.9, 7, -6.5, .1, -.1, -2.4, 2.3],
        1100 : [ 1417, 3, .6, 36.7, 5.6, 7.1, -6.6, .1, -.1, -2.6, 2.4],
        1150 : [ 1408, 3, .6, 36.7, 5.4, 7.1, -6.7, .2, -.2, -2.7, 2.5],
        1200 : [ 1399, 3, .6, 36.6, 5.1, 7.2, -6.7, .2, -.2, -2.8, 2.7],
        1250 : [ 1390, 3, .6, 36.6, 4.9, 7.3, -6.8, .2, -.2, -2.9, 2.8],
        1300 : [ 1381, 3, .6, 36.5, 4.8, 7.4, -6.9, .2, -.2, -3, 2.9],
        1350 : [ 1371, 3, .6, 36.4, 4.6, 7.4, -6.9, .2, -2, -3.2, 3],
        1400 : [ 1362, 4, .6, 36.3, 4.4, 7.5, -7, .2, -.2, -3.3, 3.1],
        1450 : [ 1353, 4, .6, 36.3, 4.3, 7.6, -7.1, .2, -.2, -3.4, 3.2],
        1500 : [ 1343, 4, .6, 36.2, 4.1, 7.6, -7.1, .2, -.2, -3.5, 3.4],
        1550 : [ 1334, 4, .6, 36.1, 4, 7.7, -7.2, .2, -.2, -3.7, 3.5],
        1600 : [ 1324, 4, .6, 36, 3.9, 7.8, -7.3, .2, -.2, -3.8, 3.6],
        1650 : [ 1314, 4, .6, 35.9, 3.8, 7.9, -7.3, .2, -.2, -3.9, 3.7],
        1700 : [ 1304, 5, .7, 35.8, 3.7, 7.9, -7.4, .2, -.2, -4, 3.8],
        1750 : [ 1294, 5, .7, 35.7, 3.6, 8, -7.5, .2, -.2, -4.2, 3.9],
        1800 : [ 1284, 5, .7, 35.6, 3.5, 8.1, -7.5, .2, -.2, -4.3, 4.1],
        1850 : [ 1274, 5, .7, 35.5, 3.4, 8.1, -7.6, .2, -.2, -4.4, 4.2],
        1900 : [ 1263, 6, .7, 35.3, 3.3, 8.2, -7.7, .3, -.3, -4.5, 4.3],
        1950 : [ 1252, 6, .7, 35.2, 3.2, 8.3, -7.8, .3, -.3, -4.7, 4.4],
        2000 : [ 1242, 6, .7, 35.1, 3.1, 8.4, -7.8, .3, -.3, -4.8, 4.5],
        2050 : [ 1230, 7, .7, 34.9, 3, 8.4, -7.9, .3, -.3, -4.9, 4.6],
        2100 : [ 1219, 7, .7, 34.8, 2.9, 8.5, -8, .3, -.3, -5, 4.8],
        2150 : [ 1207, 7, .7, 34.6, 2.9, 8.5, -8, .3, -.3, -5.2, 4.9],
        2200 : [ 1196, 8, .7, 34.5, 2.8, 8.6, -8.1, .3, -.3, -5.3, 5],
        2250 : [ 1184, 8, .7, 34.3, 2.7, 8.7, -8.2, .3, -.3, -5.4, 5.1],
        2300 : [ 1171, 9, .8, 34.1, 2.7, 8.7, -8.2, .3, -.3, -5.5, 5.2],
        2350 : [ 1158, 9, .8, 33.9, 2.6, 8.8, -8.3, .3, -.3, -5.7, 5.4],
        2400 : [ 1145, 10, .8, 33.7, 2.5, 8.8, -8.3, .3, -.3, -5.8, 5.5],
        2450 : [ 1132, 10, .8, 33.5, 2.5, 8.9, -8.4, .3, -.3, -5.9, 5.6],
        2500 : [ 1118, 11, .8, 33.3, 2.4, 8.9, -8.4, .3, -.3, -6, 5.7],
        2550 : [ 1103, 12, .8, 33.1, 2.3, 9, -8.5, .3, -.3, -6.1, 5.8],
        2600 : [ 1088, 13, .9, 32.8, 2.3, 9, -8.5, .3, -.3, -6.3, 5.9],
        2650 : [ 1072, 14, .9, 32.5, 2.2, 9, -8.6, .4, -.4, -6.4, 6],
        2700 : [ 1056, 15, .9, 32.2, 2.2, 9, -8.6, .4, -.4, -6.5, 6.1],
        2750 : [ 1038, 16, 1, 31.9, 2.1, 9, -8.6, .4, -.4, -6.6, 6.2],
        2800 : [ 1019, 18, 1, 31.6, 2, 9, -8.6, .4, -.4, -6.7, 6.4],
        2850 : [ 999, 20, 1.1, 31.2, 2, 9, -8.6, .4, -.4, -6.8, 6.4],
        2900 : [ 978, 22, 1.1, 30.7, 1.9, 9, -8.6, .4, -.4, -6.9, 6.5],
        2950 : [ 954, 26, 1.2, 30.3, 1.9, 9, -8.6, .4, -.4, -7, 6.6],
        3000 : [ 926, 31, 1.4, 29.7, 1.8, 8.9, -8.5, .4, -.4, -7.1, 6.7],
        3050 : [ 893, 39, 1.6, 28.9, 1.7, 8.8, -8.4, .4, -.4, -7.1, 6.8],
        3100 : [ 848, 54, 2, 27.9, 1.6, 8.5, -8.2, .4, -.4, -7.2, 6.8]
        
      }
    
    print('='*90)         
    print('INPUT')
    print('='*90)
        
    posMortar = str (input("Enter your position (The Gridmark, 8-10 digit, no spaces or punctuation): "))
    posTarget = str (input("Enter your targets position (The Gridmark, 8-10 digit, no spaces or punctuation): "))

    print('='*90)
    print('OUTPUT')
    
    
    '''Determining X,Y coordinates and setup for distance'''
    posMortarXY = str(posMortar)
    mUpper = ((len (posMortarXY))/2) 
    mUpper = int(mUpper) 
    xGridM = posMortarXY[0:mUpper:1]
    posMortarX = str(xGridM)
    posMortarX = int(posMortarX)
    
    mLower = ((len (posMortarXY )/2))
    mLower = int(mLower)
    yGridM = posMortarXY[mLower::1]
    posMortarY = str(yGridM)
    posMortarY = int(posMortarY)
     
     
    posTargetXY = str(posTarget)
    tUpper = ((len (posTargetXY )/2)+1) 
    tUpper = int(tUpper)
    xGridT = posTargetXY[0:mUpper:1]
    posTargetX = str(xGridT)
    posTargetX = int(posTargetX)
    
    tLower = ((len (posTargetXY )/2)) 
    tLower = int(tLower)
    yGridT = posTargetXY[mLower::1]
    posTargetY = str(yGridT)
    posTargetY = int(posTargetY)
  
    ''' distance CALC'''
    dx = (posTargetX - posMortarX)
   # print(f'dx= {dx}')
    dy = (posTargetY - posMortarY)
   # print(f'dy= {dy}')
    distance = math.sqrt(dx**2 + dy**2) 
    
    '''distance unit adjuestment'''    
    
    if len(posMortar) == 6: 
        distance = 100*distance    
    if len(posMortar) == 8:
        distance = 10*distance
    if len(posMortar) == 10:
        distance = distance    
    #print(distance)
    '''Determing azimuth in mills, and setting up for special cases where arctan is undefined'''
    '''change "if" statement to negative check and then assign ones or zeros to do a true false'''
    azimuth=0
    #print (f' DX{dx}//DY{dy}')
    if dy == 0:
        if  dx < 0:
            azimuth = 4800
        if  dx > 0:
            azimuth = 1600
    #NE
    if dx > 0 and dy > 0:   
        azimuth = 17.77777777777777777778 * math.degrees(math.atan(dx / dy))
        #print('NE')
    #NW
    if dx < 0 and dy > 0:   
        azimuth = 6400 + 17.77777777777777777778 * math.degrees(math.atan(dx / dy))  
        #print('NW')
    #SE
    if dx > 0 and dy < 0: 
        azimuth = 3200 + 17.77777777777777777778 * math.degrees(math.atan(dx / dy))
        #print('SE')
    #SW
    if dx < 0 and dy < 0: 
        azimuth = 3200 + 17.77777777777777777778 * math.degrees(math.atan(dx / dy))
        #print('SW')
    '''Variable set up for elevation calculations'''
    l0 = getList(charge0)
    l1 = getList(charge1)
    l2 = getList(charge2)
    allFar0 = []
    allFar1 = []
    allFar2 = []
    allNear0 = []
    allNear1 = []
    allNear2 = []
    range0Upper = 'a'
    range0Lower = 'a'
    range1Upper = 'a'
    range1Lower = 'a'
    range2Upper = 'a'
    range2Lower = 'a'
    ''' l0A goes with range0B and vice versea '''
    
    if distance > 3100: 
        print( "ERROR: OUT OF RANGE (Target Too Far)")
        
    if distance < 50:
        print( "ERROR: OUT OF RANGE (Target Too close)")
        
    
        '''finding the valid ranges'''
   
    '''charge 0'''
    for i in range(len(l0)):
        if distance < l0[i]:
            allNear0.append(l0[i])
        if distance > l0[i]:
            allFar0.append(l0[i])    
    
    if len(allFar0) == 0 or len(allNear0) == 0:
        #print("No valid Range in Charge 0")
        charge0Truth = 0
    else:
        allFar0.sort(reverse=True)   
        allNear0.sort(reverse=False)
        range0Upper = allNear0[0]
        range0Lower = allFar0[0]
        charge0Truth = 1
  
    '''charge 1'''   
    for i in range(len(l1)):
        if distance < l1[i]:
            allNear1.append(l1[i])
        if distance > l1[i]:
            allFar1.append(l1[i])    
    
    if len(allFar1) == 0 or len(allNear1) == 0:
        #print("No valid Range in Charge 1")
        charge1Truth = 0
    else:
        allFar1.sort(reverse=True)   
        allNear1.sort(reverse=False)
        range1Upper = allNear1[0]
        range1Lower = allFar1[0]
        charge1Truth = 1 
    
    '''charge 2'''   
    for i in range(len(l2)):
        if distance < l2[i]:
            allNear2.append(l2[i])
        if distance > l2[i]:
            allFar2.append(l2[i])    
    
    if len(allFar2) == 0 or len(allNear2) == 0:
        #print("No valid Range in Charge 2")
        charge2Truth = 0 
    else:
        allFar2.sort(reverse=True)   
        allNear2.sort(reverse=False)
        range2Upper = allNear2[0]
        range2Lower = allFar2[0]
        charge2Truth = 1 

    '''elevation calc'''
    '''charge 0'''   
    if type(range0Upper) and type(range0Lower) == int:
        farEL0 = charge0[range0Upper][0]
        nearEL0 = charge0[range0Lower][0]
        avgelevation0 = (farEL0 + nearEL0)/2
    '''charge 1'''   
    if type(range1Upper) and type(range1Lower) == int:
        farEL1 = charge1[range1Upper][0]
        nearEL1 = charge1[range1Lower][0]
        avgelevation1 = (farEL1 + nearEL1)/2
    '''charge 2'''   
    if type(range2Upper) and type(range2Lower) == int:
        farEL2 = charge2[range2Upper][0]
        nearEL2 = charge2[range2Lower][0]
        avgelevation2 = (farEL2 + nearEL2)/2 
    '''Flight Time Calculations'''
    if charge0Truth == 1:
        nearFT0 = charge0[range0Lower][3]
        farFT0 = charge0[range0Upper][3]
        avgFL0 = (nearFT0 + farFT0)/2
    if charge1Truth == 1:
        nearFT1 = charge1[range0Lower][3]
        farFT1 = charge1[range0Upper][3]
        avgFL1 = (nearFT1 + farFT1)/2
    if charge2Truth == 1:
        nearFT2 = charge2[range0Lower][3]
        farFT2 = charge2[range0Upper][3]
        avgFL2 = (nearFT2 + farFT2)/2
            
    ''' The print statments '''
    print('='*90)
    print('='*90)
    print (f' FIRE MISSION ')
    print (f' Azimuth: {azimuth}') 
    print (f' Distance from Target {distance} Meters ')
    print (f' Elevation ranges: ')
    if  charge0Truth == 1:
        print (f' [ Charge 0 Near Elevation:{nearEL0}, Far Elevation:{farEL0}] \n Average Elevation for Charge 0 {avgelevation0} \n Flight Time: {avgFL0}S')
    else:
        print(' Charge 0 is invalid')
    print('='*90)
    if  charge1Truth == 1:
        print (f' [ Charge 1 Near Elevation:{nearEL1}, Far Elevation:{farEL1}] \n Average Elevation for Charge 1 {avgelevation1}\n Flight Time: {avgFL1}S')
    else:
        print(' Charge 1 is invalid')
    print('='*90)
    if  charge2Truth == 1:
        print (f' [ Charge 2 Near Elevation:{nearEL2}, Far Elevation:{farEL2}] \n Average Elevation for Charge 2 {avgelevation2}\n Flight Time: {avgFL2}S')
    else:
        print(' Charge 2 is invalid')
    print('='*90)

    main()
main()
