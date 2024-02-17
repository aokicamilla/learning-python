# 
# Example file for variables
# LinkedIn Learning Python course by Joe Marini
#


# Basic data types in Python: Numbers, Strings, Booleans, Sequences, Dictionaries
myint = 5
myfloat = 13.2
mystr = "This is a string"
mybool = True
mylist = [0, 1, "two", 3.2, False]
mytuple = (0, 1, 2)
mydict = {"one" : 1, "two" : 2}

print(myint)
print(myfloat)
print(mystr)
print(mybool)
print(mylist)
print(mytuple)
print(mydict)

# re-declaring a variable works
myint = "abc"
print(myint)

# to access a member of a sequence type, use []
print(mylist[2])

# use slices to get parts of a sequence, the 2 in this example is the step value (número que será pulado)
print(mylist[1:5])
print(mylist[1:5:2])

# you can use slices to reverse a sequence, os :: é para dizer que não tem começo e fim definido, será o que tem na lista
print(mylist[::-1])

# dictionaries are accessed via keys
print(mydict["one"])

# ERROR: variables of different types cannot be combined
print("string" + str(123))

# Global vs. local variables in functions, uma variavel pode ser mudada localmente como no exemplo
def someFunction ():
    mystr = "def"
    print(mystr)

someFunction()
print(mystr)

#para deletar uma variavel podemos usar del mystr
