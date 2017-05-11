#tuple is immutable
# you cannot change a value in a tuple

#list is mutable
#you can change a value in a list

x = 1, 3, 12, 3
y = (2,3,4,21)


#x and y are tuples

z = [5,3,4,3]
#z is a list

print(x[1])
print(z[3])
#tuple application in method

def exampleFunc():
    return 13, 23

a, b = exampleFunc()

print(a,b)
