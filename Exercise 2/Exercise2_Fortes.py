'''
GE 120: Intro to OOP
Maria Fe Fortes

Machine Exercise 2: 
Write a script that executes a sentinel-controlled loop that asks for the Distance and Azimuth (in decimal degrees) of a line.
If yes, the process must repeat until dictated otherwise. 
Finally, the script must print out a small table showing the 
Line Number, Distance, and Bearing (in DMS, converted from Azimuth in DD) of all of the lines.
'''

# creating a sentinel-controlled loop

counter = 1     # to indicate that it starts in line number 1 
lines = []      # empty list to store line data  

# loop to input data
while True:
    # to display inputted line number
    print()
    print("LINE NO.", counter)
    
    # user input
    distance = input("Distance: ")  
    azimuth = float(input("Azimuth from the South: ")) % 360  # using modulo to return the remainder

    # using elif for multiple conditions to specify if the preceding 'if' condition is false
    if azimuth < 90:
        bearing = 'S {: ^10} W'.format(azimuth)         # if azimuth is 0-90, bearing is equal to the azimuth and SW is the direction
    elif azimuth < 180:                                  
        bearing = 'N {: ^10} W'.format(180 - azimuth)   # if azimuth is 90-180, subtracting azimuth from 180 gives the bearing, NW is the direction
    elif azimuth < 270: 
        bearing = 'N {: ^10} E'.format(azimuth - 180)   # if azimuth is 180-270, subtracting 180 from azimuth gives the bearing, NE is the direction
    elif azimuth < 360:
        bearing = 'S {: ^10} E'.format(360 - azimuth)   # if azimuth is 270-360, subtracting azimuth from 360 gives the bearing, SE is the direction

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

    line = (counter, distance, bearing)     # create tuple of the line
    lines.append(line)  # append line data to the list

    # to enter data for another line
    x = input("Add new line? ")
    if x.lower() == "yes" or x.lower() == "y":
        counter = counter + 1   # increasing line number for next iteration
        continue
    else:   # break the loop if the user's input is not yes or y
        break

print("\n\n")   # two consecutive newlines causing a blank line printed between each inputted line number
print('{: ^10} {: ^20} {: ^15}'.format("LINE NO.", "DISTANCE (m)", "BEARING")) # to format the line data centered within a width of (given number) characters  

# iterate over each line in the lines list
# print data for each line in a table format
for line in lines: 
    print('{: ^10} {: ^20} {: ^10}'.format(line[0], line[1], line[2])) # to format the line data centered within a width of (given number) characters

print("----------END----------")
