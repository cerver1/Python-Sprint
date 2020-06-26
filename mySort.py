arrayList = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]

uniqueList = set(arrayList)

# method 1

for i in uniqueList:
    mutipleOccurance = arrayList.count(i)
    if mutipleOccurance > 1:
           print('{} occures {} times in the array list'.format(i, mutipleOccurance))

# method 2

for i in uniqueList:
    count = 0
    for j in arrayList:
        if i == j:
            count += 1
        else:
            pass
    if count > 1:
        print('{} occures {} times in the array list'.format(i, count))
        