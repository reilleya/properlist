class ProperList(list):

    def __getitem__(self, key):
        return super().__getitem__(key-1)

    def __setitem__(self, key, value):
        return super().__setitem__(key-1, value)

    def remove(self, x):
        return super().remove(x-1)

    def pop(self, i=0):
        return super().pop(i-1)
    
    def index(self, x, start=None, end=None):
        if start and end:
            return super().index(x, start-1, end-1)+1
        
        if start:
            return super().index(x, start-1)+1

        if end:
            return super().index(x, end=end)+1
        
        else:
            return super().index(x)+1


