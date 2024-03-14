'''
GE 120: Intro to OOP
Maria Fe Fortes

Machine Exercise 3:
Continue the script from the previous exercise. This time, create at least three (3) functions to "break down" your code.
This include:
    Computes the latitude of a given line based on its distance and azimuth from the South
        Function Name: getLatitude
        Parameters: distance, azimuth from the South
        Return: latitude
    Computes the departure of a given line based on its distance and azimuth from the South
        Function Name: getDeparture
        Parameters: distance, azimuth from the South
        Return: departure
    Converts an azimuth (decimal degrees) to bearing (string) with signs (N, S, E, W)
        Function Name: azimuthToBearing
        Parameters: azimuth from the South
        Return: bearing
In the table to be printed, add the latitude and departure columns from the said lines. 
Finally, compute for the Linear Error of Closure (LEC) and Relative Error of Closure (REC). example: 1:500 or 1:12000
'''
from math import cos, sin, radians

def getLatitude(distance, azimuth):
    '''
    Compute for the latitude of a given line.

    Input:
    distance - float
    azimuth - float

    Output:
    latitude - float
    '''
    latitude = -distance * cos(radians(azimuth))

    return latitude

def getDeparture(distance, azimuth):
    '''
    Compute for the departure of a given line.

    Input:
    distance - float
    azimuth - float

    Output:
    latitude - float
    '''
    departure = -distance * sin(radians(azimuth))

    return departure


def azimuthToBearing(azimuth):
    '''
    Compute for the DMS bearing of a given line.

    Input:
    azimuth - float

    Output:
    bearing - string
   
    '''

    if "-" in str(azimuth) and azimuth.isType(str): # if user gives DMS
        degrees, minutes, seconds = azimuth.split("-")
        azimuth = (int(degrees) + (int(minutes/60)) + float(round(seconds/3600))) % 360
    else: # general
        azimuth = float(azimuth)%360

    if azimuth > 0 and azimuth < 90:
        bearing = 'S {: ^10} W'.format(azimuth)
    elif azimuth > 90 and azimuth < 180:
        bearing = 'N {: ^10} W'.format(180 - azimuth)
    elif azimuth > 180 and azimuth < 270: 
        bearing = 'N {: ^10} E'.format(azimuth - 180)
    elif azimuth > 270 and azimuth < 360:
        bearing = 'S {: ^10} E'.format(360 - azimuth)

    elif azimuth == 0:
        bearing = "DUE SOUTH"
    elif azimuth == 90:
        bearing = "DUE WEST"
    elif azimuth == 180:
        bearing = "DUE NORTH"
    elif azimuth == 270:
        bearing = "DUE EAST"
    else:
        bearing = "not defined"
    
    return bearing

lat = getLatitude(12, 160)
dep = getDeparture(12, 45)
print(lat, dep)
bearing = azimuthToBearing(123-12-12)
print(bearing)

