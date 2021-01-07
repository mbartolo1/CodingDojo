#1 Biggie Size, given an list, write a function that changes all positive numbers in the list to "big"
def biggiesize(arr):
    for i in range(len(arr)):
        if arr[i] >= 0:
            print("big")
        elif arr[i]<= 0:
            print(arr[i])
    return arr
biggiesize([-1, 3, 5, -5])

#2 Count Positives, given a list of numbers, create a function to replace the last value with the number of positive values.
def count_postivies(arr):
    count = 0
    for x in range(len(arr)):
        if arr[x] > 0 :
            count += 1
    arr[-1] = count
    return arr
print(count_postivies([-1,1,1,1]))

#3 sum totals,create a function that takes a list and returns the sum of all the values in the list. 
def Sumtotals(arr):
    numbers = arr()
    sum = sum(numbers)
print(sum([1,2,3,4,5]))

#4 average, create a function that takes a list and returns the average of all the values.x 
from statistics import mean
def average(arr):
    numbers = arr()
    Average = mean(numbers)
print(mean([10,20,30,25,500]))

#5 length, create a function that takes a list and returns the length of the list
from typing import Counter


def longboi(arr):
    x = len(arr)
    return x
print(longboi([1,3,3,2,1,1,2]))

#6 minimum, create a function that takes a list and returns the minimum value in the list. if the list is empty have the function return false.
def smallest(numbers):
    smallest_num = numbers[0]
    for num in numbers:
        if num < smallest_num:
            smallest_num = num
        while smallest_num == 0:
            print(False)
    return smallest_num
print(smallest([10,3,11,33]))

#7 maximum, create a function that takes a list and returns the maximum value in the list. 
def max(arr):
    max = arr[0]
    n = len(arr) 
    for i in range(1,n):
        if arr[i] > max:
            max = arr[i]
        if arr[i] == 0:
            print(False)
    return max
print(max([11,434,22,33]))

#8 ultimate Analysis - create a function that takes a list and returns a dictionary that has the sumtotal, average, minimumn, maximum and length of list
from statistics import mean
from typing import Counter
def ultiate(arr, number):
    numbers = arr()
    sum = sum(numbers)
    Average = mean(arr(len))
    x = len(arr)
    max = arr[0]
    n = len(arr) 
    for i in range(1,n):
        if arr[i] > max:
            max = arr[i]
            return max
    smallest_num = numbers[0]
    for num in numbers:
        if num < smallest_num:
            smallest_num = num
            return smallest_num
print(ultiate([11,33,44,365]))

#9 reverse list- create a function that takes a list and return that list with values reversed.
def reverse(arr):
    arr.reverse()
    return arr
print(reverse([1,3,4,5]))
