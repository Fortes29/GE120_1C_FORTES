'''
Divide and Conquer

Example: 
1. Traverse 
1.1. Fieldwork
    1.1.1. Recon
    1.1.2. Instrument Setup
    1.1.3. Measure
    1.1.4. Lipat
1.2. Adjustment
    1.2.1. LEC
    1.2.2. Compass Rule
    1.2.3. Add Correction
1.3. Submit of survey returns

Invoking a Function
a function is a set of instructions that performs specific operation
we can call our functions
example of functions: print, range, str, float, round
lahat ng functions may parenthesis
function name followed by parenthesis
may mga functions na wala ring laman

function has 3 parts: function name, parenthesis that holds the arguments, function arguments (ito yung nasa loob ng parenthesis, pwede maging isa lang or 2 or 3 that is separated by commas)

why use functions? THEY UPHOLD THE DRY PRINCIPLE
mga problems natin masyadong malaki, and tackle them into smaller subsets,
for large programming, 
dry principle (DONT REPEAT YOURSELF), pag may bagay na naulit sa program, it's better to replace it with a function
pangit ang copy paste method kasi ieedit mo multiple times ang ginawa mo, and what if may namali ka pang edit, di na yun masasalo sa dulo
with functions na dinefine, we only have to call the same functions every time, the benefit is kapag may error handling, hindi na uulit ulitin yung code sa susunod

built-in functions: abs() - absolute value, dict() - convert to a dictionary, dir()- look at a folder, 
                    help() - ang argument nya ay function din, sasabihin nya kung anong ginagawa ng function na yon
                    len() - length ng object, sasabihin nya ilang item ang nasa loob ng list mo, kapag string number of characters incl spaces ang binibilang

Defining a function  
we can create our own function telling what it does and what it needs to run
syntax:   def <function name>(<parameters>): parameters can be empty
and everything that you want this function to do should be indented
to call it, just use <functionname>(). dapat laging may parenthesis kahit empty
'''

# # # Convert a number to a string
# # a = 1
# # b = str(a)
# # print(type(b))

# # # Define our own functions

# # def functionname(parameters):

# def shout(word):
#     print(word + "!")
#     print("I created this function")
# #to call the function, use <functionname>()
# shout("YOLE")
# shout("Mika")
# shout("Peter")

# # variables inside functions are not available globally

# def shout(word):
#     number = 2 #local

# number = 1 #global

# shout("YOLE")
# shout("Mika")
# shout("Peter")

def shout():
    print(word + "!")

word = "HELLO"
shout()


def shout(word1, word2):
    print(word1 +"!")
    print(word2 + "....")

shout("mafe", "chelzy")

def shout(word1, list_of_names):
    print(word1.upper()+"!!!!!")
    print(list_of_names)
shout("mafe", ["omar", "uste"])

'''
Docstrings: ineexplain kung anong ginagawa ng functions
'''
def shout(word1, list_of_names):
    '''
    Given a word, kunin yung last letter, ulitin ng ilang beses
    tapos kapag prinint, print the word, plus inulit na last letter + exclamation point

    Parameters:
    word1 (string) - word to be printed
    '''
    print(word1.upper()+"!!!!!")
    print(list_of_names)
shout("mafe", ["omar", "uste"])
print(shout.__doc__)

'''
short description
arguments (data type)
return (data type)
'''

'''
4 types of arguments
1. Required arguments: kung ilang nilagay mong parameters, yung din dapat 
2. Default: kung wala kang ibibigay na variables, mayron ka ng default na laman
3. Keyword: position is not important kasi may keyword ka na ginamit
4. Variable-length
'''

#types of arguments

def convertDMStoDEG(dms):
    '''
    Convert DMS to Degrees

    Arguments:
        dms - string
    '''
    degrees, minutes, seconds = dms.split("-")
    dd = int(degrees) + int(minutes/60) + float(seconds/3600)
    print("eto yung value: ", round(dd, 6))

convertDMStoDEG("123-12-34")

def convertDMStoDEG(dms = "123-12-34", name = "maja"):
    '''
    Convert DMS to Degrees

    Arguments:
        dms - string
    '''
    degrees, minutes, seconds = dms.split("-")
    dd = int(degrees) + int(minutes/60) + float(seconds/3600)
    print(name + " , eto yung value: ", round(dd, 6))

convertDMStoDEG(name = "maja", dms = "123-12-34")

def print_as_table(*lines):

print_as_table(lines)


'''
returning from functions

'''

# returning from a function
result = convertDMStoDEG("12-12-12")
result += 10 
print(result)


# printing after returning something
def getDirection(degrees):
    '''
    Gives the direction of an angle
    Input:
    degrees -float
    Output:
    quadrant -string
    '''
    if degrees > 0 and degrees < 90:
        return "S-W"
    elif degrees > 90 and degrees < 180:
        return "N-W"
    elif degrees > 180 and degrees < 270:
        return "N-E"
    elif degrees > 270 and degrees < 360:
        return "S-E"
    else:
        return "IDK"
    print ("Hello dom")

direction = getDirection(100)
print(direction)

def getDirection(degrees):
    '''
    Gives the direction of an angle
    Input:
    degrees -float
    Output:
    quadrant -string
    '''
    print ("Hello dom")
    if degrees > 0 and degrees < 90:
        return "S-W"
    elif degrees > 90 and degrees < 180:
        return "N-W"
    elif degrees > 180 and degrees < 270:
        return "N-E"
    elif degrees > 270 and degrees < 360:
        return "S-E"
    else:
        return "IDK"
    
direction = getDirection(100)
print(direction)

def getDirection(degrees):
    '''
    Gives the direction of an angle
    Input:
    degrees -float
    Output:
    quadrant -string
    '''
    print ("Hello dom")
    if degrees > 0 and degrees < 90:
        return "S-W"
    elif degrees > 90 and degrees < 180:
        return "N-W"
    elif degrees > 180 and degrees < 270:
        return "N-E"
    elif degrees > 270 and degrees < 360:
        return "S-E"
    else:
        return "IDK"
    
dms = "100-12-14"
dd =
direction = 
print(getDirection(convertDMStoDEG()))

'''
Packages and Modules
bundles program code and data for reuse

'''

# Importing and using modules
'''
3 types of modules
1. those you write yourself
2. those you install from external sources
3. those that are pre-installed
'''

# module is a python file
# package is maraming modules


'''
sa calculator
Rec(12,160) angle from the North to. X dito ay Y, yung Y ay X.
Pol(12,89) 
'''