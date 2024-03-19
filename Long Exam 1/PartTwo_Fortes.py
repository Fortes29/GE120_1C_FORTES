"""
GE 120
LE 1_PartTwo: Direct Levelling Computations
Maria Fe Fortes
"""

def floatInput(prompt):
    '''
    This function contains the input function

    Parameter - prompt
    '''
    

tp_counter = 1    # to indicate where it starts
levelling_table = []      # empty list to store line data  

# loop to input data
while True:
    # to display 
    print()
    print("Sta.", tp_counter)
    
    # user input
    BS = float(input("Backsight: ")) # user inputs the backsight value
    FS = float(input("Foresight: ")) # user inputs the foresight value
    Elev = float(input("Elevation: ")) # user inputs the elevation value
    HI = Elev + BS # computes for height of the instrument

    line = (tp_counter, BS, HI, FS, Elev)     # create tuple of the line
    levelling_table.append(line)  # append line data to the list

    # to enter data for another line
    x = input("Create a new measurement (Y/N)? ")
    if x == "Y":
        tp_counter = tp_counter + 1   # increasing line number for next iteration
        continue
    else:   # break the loop if the user's input is not Y
        break

print("\n\n")   # two consecutive newlines causing a blank line printed between
print("\"Solo Leveling\" \nMaria Fe Fortes\nThis program performs direct levelling computations.")
print("\n")   # newline causing a blank line printed between each inputted leveling data
print('{: ^10} {: ^10} {: ^10} {: ^10} {: ^10}'.format("Sta.", "B.S", "H.I", "F.S", "Elev.")) # to format the line data centered within a width of (given number) characters  

# iterate over each line in the list
# print data for each line in a table format
for line in levelling_table: 
    print('{: ^10} {: ^10} {: ^10} {: ^10} {: ^10}'.format(line[0], line[1], line[2], line [3], line [4])) # to format the line data centered within a width of (given number) characters

