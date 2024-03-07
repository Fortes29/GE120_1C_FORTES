# Control Structures

# LIST (Mutable- pwede palitan yung value ng elements sa loob)
# accessed by index number
listahan = ["mafe", "justin", "mika", "uste"]
print(listahan[2])

# subset of the list
print(listahan[0:2])

print(listahan[1:3])

#nagsstart sa simula
print(listahan[:3])

print(listahan[0:])

#start sa dulo
print(listahan[-1])
print(listahan[-2])

#gets first item, last item, and those in betweeen
print(listahan[-3:3]) 

#list addition
print(listahan[0:2]+listahan[2:4])
print(listahan[0:4])

# palitan
listahan[0] = "chelzy"
print(listahan)

# TUPLES (immutable)
# accessed by index
tuple_1 = ("maja", "gianna", "jewel")
print(tuple_1)

# tuples are immutable
# tuple_1[0] = "quinmar"

# nested lists
list_1 = [ ["apple", "bola", "carton"], ["apricot", "banana", "cow"]]
print(list_1[0][2])

# nested tuples
tuple_2 = ((12.1244, -12.12414), (35.46261, -67.1231), (123.143, 56.232))
print(tuple_2[2][0])

# DICTIONARY 
# accessed by key
# key value pairs

dict = {
        "name": "Bogart",
        "age": 2,
        "color": "white",
        "number": 3.14,
        1: 45   # pwede si numbers as keys
        }
print(dict[1])
print(dict.values())    # returns a list of values
print(dict.keys())      # returns a list of keys

dict["number"] = 39
print(dict)

x = 6
y = 7

print(x == y)
x != y 
x > y
x < y
x >= y
x <= y 
print(not(x==y))

grade = 93
if grade >= 92:
    print("YAHOO")
if grade >= 60:
    print("NICE")    # magpi-print ng YAHOO and NICE, kaya kung gusto mo na isa lang masatisfy use "elif"
else:
    print("SAD")

grade = 92; favorite = True
if grade >= 92:
    print("YAHOO")
elif grade >= 60:
    print("NICE")
elif grade < 60 and favorite:
    print("PASANG AWA")
else:
    print("SAD")


range(0,10)
range(10)

# LOOPS AND BREAK CONTINUE AND PASS

numbers = range(50,100)
print(numbers)

for number in numbers:
    print(number)

for number in range(10):
    print(number)

for number in range(10):
    if number == 5:
        break
    print(number)

for number in range(10):
    if number == 5:
        continue
    print(number)

for number in range(10):
    if number == 5:
        pass
    print(number)

for number in range(10):
    if number == 5:
        pass
        print(number)

for number in range(10):
    if number == 5:
        continue
        print(number)
        
rec = 0      # para may mapagcomparean yung <5000
while rec <= 5000:
    rec = int(input("enter REC: "))
    kulang = 5000 - rec
    if rec >= 4500:
        print("onti na lang kulang pwede na")
        break
    print("kulang ka ng rec na", kulang)

print("PASOK NA REC")
print("----END----")


rec = 0      # para may mapagcomparean yung <5000
while rec <= 5000:
    rec = int(input("enter REC: "))
    kulang = 5000 - rec
    if rec >= 4500:
        print("onti na lang kulang kaya mo yan")
        continue
    print("kulang ka ng rec na", kulang)
    
print("PASOK NA REC")
print("----END----")


lista = [1,2,3]
lista.append(5) #adds 5 to the list
print(lista)

lista.pop(3)    #removes 3 from the list
print(lista)

lista.reverse()
print(lista)