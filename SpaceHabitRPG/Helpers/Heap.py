from collections import OrderedDict




class Heap(object):
    """
    This is a standard heap object for sorting. This is not needed for the 
    actual application but is nevertheless used for testing purposes.
    """
    def __init__(self, sortByFunction):
        """
            args:
                sortByFunction: 
                    needs to be a lamba that that can be used to
                    compare the values of two items in the heap
        """
        self._heap = []
        self._sortByFunction = sortByFunction


    def is_empty(self):
        return len(self._heap) == 0


    def __len__(self):
        return len(self._heap)


    def push(self,item):
        """
            Adds items to the sorting heap to be sorted.
            args:
                item type should be consistent with whatever type you've 
                already been put in the heap otherwise, you're gonna
                have a bad time.
        """
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
        """
            Standard sorting heap pop method. Get's the next item based on 
            sort order and then removes that item from the heap.

            returns:
                the next item in order. You know what you added to this. I don't.
                If there are no more items, this throws an error.
        """
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
        """
            push a whole list onto the sorting heap to be sorted.

            args:
                list: 
                    this should be a list or at least some sort of iterable object.
                    Idealy, all of the items in this list should also be the
                    same type but that's your fucking problem.
        """
        for i in list:
            self.push(i)


    def get_sorted_list(self):
        """
            Get's a sorted list.
            The heap will be empty after you call this and if you try to 
            call it again, it will thrown an error because it's empty.

            returns:
                a sorted list of whatever you put in here.
        """
        sorted = []
        while len(self._heap) > 0:
            sorted.append(self.pop())
        return sorted


    def popper(self):
        """
            this is a generator to get items off of the sort heap in order.
            This is useful when you don't want to get all of the items at once
            or when you want to distribute work load between different calls.

            yields:
                the item next in the sort order.
                throws an error in the heap is empty.
        """
        while len(self._heap) > 0:
            yield self.pop()


    def top(self):
        """
            returns:
                get the next item in order from the heap without removing it.
            
        """
        return self._heap[0]
    

    def clear(self):
        """
            removes all items from the heap
        """

        self._heap.clear()




               
