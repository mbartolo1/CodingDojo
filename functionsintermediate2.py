x = [ [5,2,3], [10,8,9] ]
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20} ]

# #Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0] = 15
print(x)
# #Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name']='bryant'
print(students)
# #In the sports_directory, change 'Messi' to 'Andres'
players = sports_directory['soccer']
players[0] = "andres"
print(players)
# #Change the value 20 in z to 30
z[0]['y'] = 30
print(z)
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    for i in range(len(students)):
        print(students[i]['first_name'],students[i]['last_name'])
iterateDictionary(students)
def iterateDictionary2(key, students):
    for dictonary in students:
        print(dictonary[key])
iterateDictionary2('first_name',students)
iterateDictionary2('last_name', students)
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
    # first_name - Michael, last_name - Jordan
    # first_name - John, last_name - Rosales
    # first_name - Mark, last_name - Guillen
    # first_name - KB, last_name - Tonel

#4 iterate through a dictionary with list values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon'] 
}
def printInfo(dojo):
        print(dojo['locations'])
        print(dojo['instructors'])
printInfo(dojo)
#printInfo('locations', dojo)
