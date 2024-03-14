'''
GE 120: Intro to OOP
Maria Fe Fortes

Machine Exercise 2: 
Write a script that executes a sentinel-controlled loop that asks for the Distance and Azimuth (in decimal degrees) of a line.
If yes, the process must repeat until dictated otherwise. 
Finally, the script must print out a small table showing the line Number, Distance, and Bearing (in DMS, converted from Azimuth in DD) of all of the lines.
'''

# creating a sentinel-controlled loop
counter = 1     # to indicate that it starts in line number 1 
lines = []      # empty list

while True:
    print()
    print("LINE NO.", counter)
    distance = input("Distance: ")
    azimuth = (input("Azimuth from the South: "))%360
    if "-" in azimuth:
        degrees, minutes, seconds = azimuth.split("-")
        azimuth = (int(degrees) + (int(minutes/60)) + float(round(seconds/3600))) % 360
    else:
        azimuth = (azimuth)%360

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

    line = (counter, distance, bearing)     #create tuple of the line
    lines.append(line)

    # ask for input
    yn = input("Add new line? ")
    if yn.lower() == "yes" or yn.lower() == "y":
        counter = counter + 1
        continue
    else:
        break

print("\n\n")
print('{: ^10} {: ^10} {: ^10}'.format("LINE NO.", "DISTANCE", "BEARING"))

for line in lines:
    print('{: ^10} {: ^10} {: ^10}'.format(line[0], line[1], line[2]))

print("----END----")
