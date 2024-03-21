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


from math import cos, sin, radians, sqrt                # importing math module for trigonometric calculations


def getLatitude(distance, azimuth):                     # defining a function that computes for the latitude
    '''
    Compute for the latitude of a given line.

    Input:
    distance - float
    azimuth - float

    Output:
    latitude - float
    '''
    latitude = -distance * cos(radians(azimuth))        # formula for solving the latitude given a distance and azimuth in decimal degrees

    return latitude



def getDeparture(distance, azimuth):                    # defining a function that computes for the departure
    '''
    Compute for the departure of a given line.

    Input:
    distance - float
    azimuth - float

    Output:
    departure - float
    '''
    departure = -distance * sin(radians(azimuth))       # formula for solving the departure given a distance and azimuth in decimal degrees

    return departure



def azimuthToBearing(azimuth):                          # defining a function that computes for the bearing
    '''
    Compute for the DMS bearing of a given line.

    Input:
    azimuth - float

    Output:
    bearing - string
    '''
    if "-" in str(azimuth):     # if user gives DMS
        degrees, minutes, seconds = azimuth.split("-")      # taking only the digits part, removing the '-'
        azimuth = (int(degrees) + int(minutes)/60 + float(seconds/3600)) % 360      # converting from DMS to decimal degrees
    else:      # general
        azimuth = float(azimuth) % 360      # using modulo to return the remainder

    # conditions for the inputted azimuth
    if azimuth > 0 and azimuth < 90:        # if the azimuth is between 0-90, it will give the bearing direction SW
        bearing = 'S {: ^10} W'.format(azimuth)          # azimuth remains as it is if it is between 0 - 90
    elif azimuth > 90 and azimuth < 180:    # if the azimuth is between 90-180, it will give the bearing direction NW
        bearing = 'N {: ^10} W'.format(180 - azimuth)   # if the bearing is in NW, azimuth is subtracted from 180
    elif azimuth > 180 and azimuth < 270:   # if the azimuth is between 180-270, it will give the bearing direction NE
        bearing = 'N {: ^10} E'.format(azimuth - 180)   # if the bearing is in NE, 180 will be subtracted from azimuth
    elif azimuth > 270 and azimuth < 360:   # if the azimuth is between 270-360, it will give the bearing direction SE
        bearing = 'S {: ^10} E'.format(360 - azimuth)   # if the bearing is in SE, azimuth will be subtracted from 360

    # conditions if the inputted azimuth is exactly 0, 90, 180, 270
    elif azimuth == 0: 
        bearing = "DUE SOUTH"   # if the azimuth is 0, bearing is due south
    elif azimuth == 90:
        bearing = "DUE WEST"    # if the azimuth is 90, bearing is due west
    elif azimuth == 180:
        bearing = "DUE NORTH"   # if the azimuth is 180, bearing is due north
    elif azimuth == 270:
        bearing = "DUE EAST"    # if the azimuth is 270, bearing is due east
    else:
        bearing = "not defined" # if the azimuth is neither 0, 90, 180, 270, bearing is labeled not defined
    
    return bearing



def reciprocal(n):         # defining a function that computes for the reciprocal
    '''
    Computes for the reciprocal of a number.
    This will be used for REC.
    '''
    return 1.0 / n         # formula in reciprocating a number



# create a sentinel-controlled loop
counter = 1     # to indicate that this is the start
lines = []      # empty list to store line data
# to indicate that the values start from 0
sumLat = 0     
sumDep = 0
sumDist = 0

# loop to input data
while True:
    # this is the display while being asked for distance and azimuth for each line no.
    print()
    print("LINE NO.", counter)

    distance = float(input("Distance: "))   # to indicate that the data type should be a float
    azimuth = float(input("Azimuth from the South (in DD): "))     # to indicate that the data type should be a float

    bearing = azimuthToBearing(azimuth)
    lat = getLatitude(distance, azimuth)
    dep = getDeparture(distance, azimuth)

    # computes for the total values of latitude, departure, and distance
    sumLat += lat
    sumDep += dep
    sumDist += float(distance)

    line = (counter, distance, bearing, lat, dep)   # create tuple of the line
    lines.append(line)  # append line data to the list

    # to enter data for another line
    x = input("Add new line? ")
    if x.lower() == "yes" or x.lower() == "y":
        counter = counter + 1   # increasing line number for next iteration
        continue
    else:   # break the loop if the user's input is not yes or y
        break


print("\n\n")   # two consecutive newlines causing blank lines printed 
print('{: ^10} {: ^20} {: ^30} {: ^30} {: ^30}'.format("LINE NO.", "DISTANCE", "BEARING", " LATITUDE", "DEPARTURE")) # to format the line data centered within a width of (given number) characters  

# iterate over each line in the lines list
# print data for each line in a table format
for line in lines: 
    print('{: ^10} {: ^20} {: ^30} {: ^30} {: ^30}'.format(line[0], line[1], line[2], line[3], line[4])) # to format the line data centered within a width of (given number) characters

print("\n") # newline, causing a blank line printed

# to display the values for the total latitude, departure, and distance
print("Summation of Latitude: ", sumLat)
print("Summation of Departure: ", sumDep)
print("Summation of Distance: ", sumDist)

print("\n") # newline, causing a blank line printed

lec = sqrt(sumLat**2 + sumDep**2)   # formula for solving the linear error of closure
print("LEC: ", lec)     # to display computed value of lec

rec = (lec/sumDist)     # formula for solving the relative error of closure
reciprocal_rec = reciprocal(rec) # reciprocating the computed rec using the defined function of reciprocal above
print("REC: ", round(reciprocal_rec, -3)) # to display the rounded value to hundreds place of reciprocated rec

# compass rule formula is distance*(-totalLat/totalDistance) and distance*(-totalDep/totalDistance)
constCorrLat = -sumLat/sumDist      # separating the distance, solving this first and represent as a constant
constCorrDep = -sumDep/sumDist

# iterate over each line in the lines list
for line in lines:
    corr_lat = constCorrLat*line[1]     # line[1] is the distance column, every corresponding values for each line will be multiplied to the constant corrected lat
    corr_dep = constCorrDep*line[1]     # line[1] is the distance column, every corresponding values for each line will be multiplied to the constant corrected dep

    adjLat = line[3] + corr_lat         # adding the computed latitude to the corrected latitude for adjustment
    adjDep = line[4] + corr_dep         # adding the computed departure to the corrected departure for adjustment

print("----------END----------")



