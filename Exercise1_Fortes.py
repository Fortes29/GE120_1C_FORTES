"""
GE 120: Intro to OOP
Maria Fe Fortes
Machine Exercise 1: Converting Decimal Degrees (DD) to Degree-Minute-Second (DMS) and vice versa.

"""

# Part 1: Converting DD to DMS

DD = float(input("Enter a number here: ")) # using float to describe that the data type to be inputted is with decimal fractional part

degree = int(DD // 1)                      # takes the integer part of the inputted number, that is without the decimal fractional part
minutes = (DD - degree) * 60               # computes for the minute part of the DMS by subtracting degree from DD and multiplying to 60
minutes_int = int(minutes)                 # takes the number without the decimal fractional part
seconds = (minutes - minutes_int) * 60     # computes for the second part of the DMS

# outputs DMS in XXX-XX-XX.xx format
print("DMS: " + str(degree) + "-" + str(minutes_int) + "-" + str(round(seconds, 2))) 

# Part 2: Converting DMS to DD

d = float(input("Enter a number here: "))
m = float(input("Enter a number here: "))
s = float(input("Enter a number here: "))



# outputs DD in XXX.xxxxxx format
print("DD: ", round(,6))

# dms = "118-25-14.48"
# values = dms.split("-")
# degrees = int(values[0])
# minutes = int(values[1])
# seconds = float(values[2])
# dd = degrees + (minutes/60) + (seconds/3600)
# print("ETO YUNG VALUE: ", round(dd,6))