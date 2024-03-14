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

def getLatitude(d,AzS):

