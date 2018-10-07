#!/usr/bin/python3
'''
Writing the Bubble Sort algorithm in Python
'''
from sys import exit

def bubbleSort(array, size):
    '''
    Sorting an array of integers in ascending order using the Bubble sort algorithm
    '''
    if array is None:
        raise TypeError("No values in the list")
    
    if size == 0:
        raise AttributeError("Size cannot be zero")
    
    if size == 1:
        print("Array is already sorted")
        exit -1

    for i in range(size):
        for j in range(0, size-i-1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
