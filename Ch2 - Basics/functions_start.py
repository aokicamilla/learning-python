#
# Example file for working with functions
# LinkedIn Learning Python course by Joe Marini
#


# TODO: define a basic function
def func1():
    print("I'm a function")

# TODO: function that takes arguments
def func2(arg1, arg2):
    print(arg1, " ", arg2)

# TODO: function that returns a value
def cube(x):
    return x * x * x

# TODO: function with default value for an argument
def power(num, x=1):
    result = 1;
    for i in range(x):
        result = result * num
    return result

# TODO: function with variable number of arguments, o * diz que pode passar um numero variável de argumentos
def multi_add(*args):
    result = 0
    for  x in args:
        result = result + x
    return result

func1()
print(func1())

func2(10,20)
print(func2(10,20))

print(cube(3))

#aqui demos apenas o valor de num
print(power(2))
#aqui abaixo demos um valor para x
print(power(2,3))
#podemos usar fora de ordem desde que nomeados
print(power(x=3, num=2))

print(multi_add(4,5,10,2))