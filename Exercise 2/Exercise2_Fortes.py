'''
GE 120: Intro to OOP
Maria Fe Fortes

Machine Exercise 2: 
Write a script that executes a sentinel-controlled loop that asks for the Distance and Azimuth (in decimal degrees) of a line.
If yes, the process must repeat until dictated otherwise. 
Finally, the script must print out a small table showing the line Number, Distance, and Bearing (in DMS, converted from Azimuth in DD) of all of the lines.
'''

counter = 1     # start sa line #1, define muna to 
lines = []      # empty list, para makuha kung san isstore

while True:
    print()
    print("LINE NO.", counter)
    distance = input("Distance: ")
    while not(bobo_magtype):
    if bobo_magtype:
        print
    azimuth = float(input("Azimuth from the South: ")) % 360

    if azimuth > 0 and azimuth < 90:
        bearing = 'S {: ^10} W'.format(azimuth)
    elif azimuth > 90 and azimuth < 180:
        bearing = 'N {: ^10} W'.format(180 - azimuth)
    elif azimuth > 180 and azimuth < 270: 
        bearing = azimuth - 180




    elif azimuth == 0:
        bearing == "DUE SOUTH"
    elif azimuth == 90:
        bearing == "DUE SOUTH"
    elif azimuth == 0:
        bearing == "DUE SOUTH"
    elif azimuth == 0:
        bearing == "DUE SOUTH"

    else:
        bearing = "ewan ko"

    line = (counter, distance, bearing)     #create tuple of the line
    lines.append(line)


    yn = input("Add new line? ")
    if yn.lower() == "yes" or yn.lower() == "y":
        counter = counter + 1
        continue
    else:
        break

print("\n\n")
print('{: ^10} {: ^10} {: ^10}'.format("LINE NO.", "DISTANCE", "BEARING"))

for line in lines:
    print('{} {} {}'.format(line[0], line[1], line[2]))

print(lines)
print("----END----")
