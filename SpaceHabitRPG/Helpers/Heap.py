from Daily import Daily
from Habit import Habit
from Todo import Todo
from Good import Good
from collections import OrderedDict


class Heap(object):

    def __init__(self, sortByFunction):
        self._heap = []
        self._sortByFunction = sortByFunction

    def is_empty(self):
        return len(self._heap) == 0

    def __len__(self):
        return len(self._heap)

    def push(self,item):
        self._heap.append(item)
        i = len(self._heap) -1
        parent = (i -1) // 2
        while i > 0:
            if self._sortByFunction(self._heap[i],self._heap[parent]):
                self._heap[parent], self._heap[i] = self._heap[i],self._heap[parent]
                i = parent
                parent = (i -1) // 2
            else:
                return


    def pop(self):
        if len(self._heap) == 0:
            raise IndexError("You tried to pop from an empty heap")
        topItem = self._heap[0]
        if len(self._heap) == 1:
            self._heap.pop()
            return topItem
        self._heap[0] = self._heap.pop()
        i = 0
        i1 = 2*i +1
        i2 = 2*i +2
        while i1 < len(self._heap):
            maxChild = i1
            if i2 < len(self._heap) and self._sortByFunction(self._heap[i2],self._heap[maxChild]):
                maxChild = i2
            if self._sortByFunction(self._heap[maxChild],self._heap[i]):
                self._heap[maxChild], self._heap[i] = self._heap[i],self._heap[maxChild]
            i = maxChild
            i1 = 2*i +1
            i2 = 2*i +2
        return topItem

    def push_list(self,list):
        for i in list:
            self.push(i)

    def get_sorted_list(self):
        sorted = []
        while len(self._heap) > 0:
            sorted.append(self.pop())
        return sorted

    def popper(self):
        while len(self._heap) > 0:
            yield self.pop()

    def top(self):
        return self._heap[0]
    
    def clear(self):
        self._heap.clear()




               
