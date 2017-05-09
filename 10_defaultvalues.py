def simple(num1, num2):
    pass

def simple2(num1, num2=3): #3 is the default values of num2
    print(num1, num2)

#taking advantage of default
simple2(5) #this will be taken ans num1 and num2 will be 2

#you can either pass both values
simple2(7,8)

#customizations
def basic_window(width, height, font='TNR',
                 backgroun='white', scrollbar= True):
    print(width, height, font, backgroun, scrollbar)


basic_window(500, 350)
                 

#To avoid ambiguity, provide which value of default should be overridden
basic_window(500, 342, backgroun='yellow')
