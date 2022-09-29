# 1 update values in dictionaries and lists

#a
x = [ [5,2,3], [10,8,9] ]
x[1][0] = 15
print(x)

#b
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name'] = "Bryant"
print(students)

#c
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = "Andres"
print(sports_directory)

#d
z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30
print(z)


# 2 Iterate through a list of dictionaries

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(list):
    for i in range(len(list)):
        for key, val in students[i].items():
            print(key, " - ", val)

print(iterateDictionary(students))

#3 
students = [
        {'first_name' :  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary2(some_key, some_list):
    for i in range(len(some_list)):
        if some_key in some_list[i]:
            print(some_list[i][some_key])

print(iterateDictionary2('last_name', students))

#4
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key, val in some_dict.items():
        print(len(val), key)
        for i in range(len(val)):
            print(val[i])

printInfo(dojo)
