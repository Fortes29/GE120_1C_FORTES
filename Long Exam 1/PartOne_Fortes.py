# 1 Differentiate Procedural programming from Functional programming.
"""
Procedural programming is more of a step by step execution based on given conditions if ever were there any. 
Procedural programming involves control structures like sequence structure, selection structure and repetition structure. 
A sequence structure is a line by line execution, it follows the top-down approach. However, programming is not always like that,
that's why there are selection and repetition structures. 
Selection structure executes the code based on given conditions and it uses if, if-else, and if-elif-else statements.
Repetition structure also called loops, uses while and for statements in executing the code. 

While functional programming uses a function. 
A function is a set of instructions or a block of code that performs a specific operation, 
it has three parts: function names, parentheses that hold the arguments, and the function arguments.
We use functions because it upholds the DRY (Don't Repeat Yourself) principle.
So that in any large programming codes, we do not have to repeat the codes and avoid having to repetitively edit the block of codes.
For example, you are editing a block of code and do the copy-paste method, and then you commit a mistake, 
you have to go back again to the previous codes so you can edit them out, to avoid having to do this over and over again, we use functions.
"""


# 2 How does Git help in the collaborative Development and version control environment of programming?
"""
Git is a free and open source repository that enables the users to clone and branch their repository files. 
There are also some git commands like push, pull, commit, sync, etc. In cloning a repository file, it basically creates a copy of a folder.
In branching a repository file, the users are allowed to edit one's code. 
I imagine this like Google Collaboratory, wherein I share access to one end, and he/she will be able to edit my code. 
But with Git, parang nagkakaroon ng isang copy pa ng code file kung saan makakaedit ang isa pang user without having any changes on my end.
And then, we users will be able to combine our code works. 
Git helps in interactive coding of users. 
"""


# 3 When should one use a while loop and when should one use a for loop? Give examples in the field of geomatics.
"""
While loops are used when the number of executions are unknown or is a sentinel-controlled. It runs until the execution is considered false.
For loops are used when you want to iterate over each item and the number of executions are known or is a counter-controlled.

An example is our Exercise 2. 
This is my code from Exercise 2:
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
"""


# 4 Discuss the Divide and Conquer paradigm in programming
"""
Divide and conquer is a paradigm wherein a big problem is subdivided into smaller problems, 
and that smaller problems are also divided into more smaller problems. 
These subproblems are being solved until the solution for the big problem is achieved.
These subproblems are often solved by using programming codes.
"""


# 5 Give an example of a task related to geomatics that is done manually and can be optimized using programming. What would be your plan-of-attack for this solution?
"""
As of now, we are manually solving the traverse and leveling adjustments 
by inputting the gathered data in excel or sheets as well as the formulas.

If we can make a programming application wherein we just have
to input the gathered data without having to put the formulas, 
I think the fieldwork would be easier because we will be able to find out promptly the REC. 

Maganda rin sana kung pagka input ng mga data, agad-agad nalalaman kung saan din may mali at kung saang line uulit ng pagtraverse or leveling
para hindi buong area ang uuliting itraverse/level.
"""


