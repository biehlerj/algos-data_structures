#!/usr/bin/python3
'''
Writing the Bubble Sort algorithm in Python
'''

def bubbleSort(array, size):
    '''
    Sorting an array of integers in ascending order using the Bubble sort algorithm
    '''
    for i in range(size):
        for j in range(0, size-i-1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

# Code to test if bubble sort is working
arr = [64, 34, 25, 12, 22, 11, 90]
 
bubbleSort(arr, len(arr))
 
print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i]),
