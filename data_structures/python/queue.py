from collections import deque


class Queue:
    def __init__(self, max_size: int):
        self.__max_size = max_size
        self.__queue = deque(maxlen=max_size)

    def size(self):
        return len(self.__queue)

    def enqueue(self, new_num: int):
        if self.size() >= self.__max_size:
            raise IndexError('The max size of the queue has been reached')
        self.__queue.append(new_num)

    def dequeue(self):
        return self.__queue.pop()

    def __repr__(self):
        return list(self.__queue)
