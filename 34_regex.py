'''
Identifiers:
\d = any number
\D = anything but a number
\s = space
\S = anything but a space
\w = any character
\W = anything but a character
.  = any character except newline(\n)
\b = the white space around words
\. = period

Modifiers:
amount and type
{1,3} = we're expecting 1-3
+ = match 1 or more
? = match zero or 1
* = match zero or more
$ = match the END of the string
^ = match the BEGINNING of the string
| = either or
[] = range or variance --> [A-Za-z]
{x} = expecting x amount

Whitespace characters:
\n = newline
\s = space
\t = tabs
\e = escape
\f = form feed
\r = return

DON'T FORGET!!
. + * ? [ ] $ ^ ( ) { } | \

'''

import re

exampleString = '''
Jesica is 14 years ollld, and Daniel is 27 years old.
Edward is 87, and his grandpa, Oscarman, is 112.
'''

ages = re.findall(r'\d{1,3}', exampleString)
names = re.findall(r'[A-Z][a-z]*', exampleString)

print(ages, names)

ageDict = {}
x=0
for eachName in names:
    ageDict[eachName] = ages[x]
    x+=1


print(ageDict)
