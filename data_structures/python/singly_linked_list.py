#!/usr/bin/python3
'''
Implementing a singly linked list in Python
'''

class Node(object):
    '''
    Setting up the class Node to allow for a singly linked list to have multiple elements
    '''
    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.nextNode = nextNode

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def nextNode(self):
        return self.__nextNode

    @nextNode.setter
    def nextNode(self, value):
        self.__nextNode = value

class LinkedList(object):
    '''
    Creating the Linked List class
    '''
    