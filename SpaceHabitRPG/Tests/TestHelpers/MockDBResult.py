class MockDBResult(object):
    """
        This will be used with the mock version of get_sorted_stuff_by_search.
        It's basically a mock mongodb cursor
    
    """

    def __init__(self,data):
        """
            args:
                data:
                    this should be a list of dicts. Doesn't really matter 
                    what's in  those dicts
        """
        self._data = data

    def next(self):
        """
            this is a generator function that gets the next item in the list

            yieds:
                a dict containing dummy data most likely
        """
        for d in self._data:
            yield d


