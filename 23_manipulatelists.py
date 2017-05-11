alist = [1,3,2,4,2,13, 23, 13,23123, 'asdasf', 343, 12, 332]
alist.append(23)
print(alist)

alist.insert(2, 99)
print(alist)


alist.remove(3)
print(alist)


alist.remove(alist[3])
print(alist)



print(alist[3:9])

print(alist[10:])

print(alist[-1], alist[-2])


print(alist.index(343))

print(alist.count(13))


alist.sort()
print(alist)

#sort() also sorts alphabetically


