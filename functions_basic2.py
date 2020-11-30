#1: create a function that accepts a number as an input. return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element)
def countdown(num):
    list = []
    for i in range (num, -1, -1):
        list.append(i)
    return list
print(countdown(7))

#2 Create a function that will receive a list with two numbers. Print the first value and return the second.
#Example: print_and_return([1,2]) should print 1 and return 2
def funlist(list):
    print(list[0])
    return list[1]
print (list([1,2]))

#3 Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
#Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)
def first_plus_length(list):
    print(list[0] + len(list))
    return(list)
print(first_plus_length([80,20,2]))

#4 Values Greater than Second
def Greater_than_second(list):
    if len(list)<2:
        return False
    newlist = []
    for val in list:
        if val > list [1]:
            newlist.append(val)
    print(len(newlist))
    return newlist 
print(Greater_than_second([30,10,20,5,50,60]))
print(Greater_than_second([5,2,3,2,1,4]))
print(Greater_than_second([3]))

#5 This Length, That Length
def Length_and_Value(size,value):
    list = []
    for i in range(size):
        list.append(value)
    return list
print(Length_and_Value(4,7))
print(Length_and_Value(6,2))

#6 minimum - create a function that takes a list of numbers and returns the minimum value in the list. if the list is empty, have the function return false.
def minimum(list):
    for  i in range(list.range):
        if [i] is < 0:
            print(false)
        elif [i] >= 0:
            return 