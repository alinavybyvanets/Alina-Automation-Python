class ReverseListIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data) -1
    def __iter__(self):
        return self
    def __next__(self):
        if self.index < 0:
            raise StopIteration
        value = self.data[self.index]
        self.index -= 1
        return value
inems = [1,2,3,4,5,6,7,8,9, 10]
for i in ReverseListIterator(inems):
    print(i)

class EvenIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        value = self.current
        self.current += 2
        return value
N = 12
for num in EvenIterator(N):
    print(num)