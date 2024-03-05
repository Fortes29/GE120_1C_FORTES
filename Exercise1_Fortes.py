"""
GE 120: Intro to OOP
Maria Fe Fortes

Machine Exercise 1: 
Write a script that accepts decimal degrees (XXX.xxxxxx) as input and outputs the degree, minute, and second (XXX-XX-XX.xx).
After this, write a script that accepts degree, minutes, seconds (XXX-XX-XX.xx) as input and outputs the decimal degrees.
Be sure to include all the necessary comments explaining your code.

"""

# Part 1: Converting DD to DMS

DD = float(input("Enter any number here: "))    # using float to describe that the data type to be inputted is with decimal fractional part

degree = int(DD)                                # takes the integer part of the inputted number, that is without the decimal fractional part
minutes = (DD - degree) * 60                    # computes for the minute part of the DMS by subtracting degree from DD and multiplying to 60
minutes_int = int(minutes)                      # takes the number without the decimal fractional part
seconds = (minutes - minutes_int) * 60          # computes for the second part of the DMS

# outputs DMS in XXX-XX-XX.xx format
# using variables a,b,c to represent degree, minutes_int, and seconds, respectively
# using 0 as fillers for the minutes_int part in case that the result is only 1 digit, >2d for taking 2 digits
# using abs to take the absolute values of minutes_int and seconds part in case that the inputted number is negative
print("DMS: {a}-{b:0>2d}-{c}".format(a=degree, b = abs(minutes_int), c = abs(round(seconds,2))))


# Part 2: Converting DMS to DD

dms = str(input("Enter any number here in this format XX-XX-XX.xx: ")) 

values = dms.split("-")

d = int(values[0])
m = int(values[1])
s = float(values[2])

dd = d + (m/60) + (s/3600)

print("DD: ", round(dd,6))