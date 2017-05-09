#iterate through lists

listn = [123, 123,34,24, 4, 3, 1, 4, 7]

for eachNumber in listn:
        print(eachNumber)


        print('prints through all the time in the iterations')

print('prints only once')


for x in range(1, 20):
    print(x)


#using range generates the full list occuping all memory in the case of range(1, 123424234324234234
#using xrange is better - it just generates the counter

for x in range(1, 20, 5): #in steps of 5 - prints 1, 6, 11, 16
    print(x)
