# 1 countdown

def countDown(num):
    newList = []
    for x in range(num, -1, -1):
        newList.append(x)
    print(newList)

print(countDown(5))

# 2 print and return

def printAndReturn(list):
    print(list[0])
    return list[1]

print(printAndReturn([1,2]))

#3 first plus length

def firstPlusLength(list):
    return list[0] + len(list)

list1 = [1,2,3,4,5]
print(firstPlusLength(list1))

# 4 values greater than second 

def greater(list):
    newList1 = []
    for x in range(len(list)):
        if list[x] > list[1]:
            newList1.append(list[x])
    print(len(newList1))
    print(newList1)

greater([3,2,3,4,5])

# 5 this length, that value

def thisThat(size, value):
    newList2 = []
    for n in range(0, size):
        newList2.append(value)
    return newList2

print(thisThat(4,8))
