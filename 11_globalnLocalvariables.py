x = 6

def example():
    print(x)
    print(x+5)
    #works fine

    #x += 7 #doesn't work - uncomment and see
    #so it is taking in x as a local variable when we are assigning something
    
example()
    
#instead, follow example below

y = 9

def example2():
    global y
    print(y)
    print(y+8)

    y += 10
    print(y)

    #works

example2()

##IF you are against using global, use the below way

z = 10

def example3():
    globz = z
    globz+= 10
    return globz

z = example3()
print(z)
