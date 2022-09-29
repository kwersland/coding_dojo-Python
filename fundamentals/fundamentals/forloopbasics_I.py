
# #basics
for x in range(0,151):
    print(x)

#multiples of 5
for x in range(5,1001,5):
    print(x)

#counting the dojo way
dojo = "Coding Dojo"
coding = "Coding"
for x in range(1,101):
    if x % 10 == 0:
        print(dojo)
    elif x % 5 == 0:
        print(coding)
    else:
        print(x)

#woah that sucker's huge - Add odd integers from 0 to 500,000, and print the final sum.
x = 0
for y in range(1, 500001, 2):
    x += y

# print(x)

#countdown by fours
for x in range(2018,0,-4):
    print(x)

#flexible counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, 
# print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the 
# loop should print 3, 6, 9 (on successive lines)

lowNum = 5
highNum = 150
mult = 9

for x in range(lowNum,highNum):
    if x % mult == 0:
        print(x)

