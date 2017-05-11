try:
    x = 19/0

except Exception as e:
    print('exception:',e)

try:
    print(r)

except NameError as r:
    print('error:',r)
