#!/usr/bin/python3
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return "<Node: ({}, {}), next: {}>".format(self.key, self.value, self.next)

    def __repr__(self):
        return str(self)


class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.buckets = [None] * self.capacity

    def hash(self, key):
        hash_sum = 0

        for i, c in enumerate(key):
            hash_sum += (i + len(key)) ** ord(c)
            hash_sum %= self.capacity
        return hash_sum

    def insert(self, key, value):
        self.size += 1
        index = self.hash(key)
        node = self.buckets[index]

        if node is None:
            self.buckets[index] = Node(key, value)
            return
        prev = node
        while node:
            prev = node
            node = node.next
        prev.next = Node(key, value)

    def find(self, key):
        index = self.hash(key)
        node = self.buckets[index]

        while node and node.key != key:
            node = node.next
        if node is None:
            return None
        else:
            return node.value

    def remove(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        prev = None

        while node and node.key != key:
            prev = node
            node = node.next
        if node is None:
            return None
        else:
            self.size -= 1
            result = node.value
            if prev is None:
                self.buckets[index] = node.next
            else:
                prev.next = prev.next.next
            return result
