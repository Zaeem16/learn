class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError
        else:
            self._capacity = capacity
            self._size = 0


    def __str__(self):
        cookie = "🍪"
        if self.size == 0:
            return ""
        return cookie * self._size



    def deposit(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError
        elif n + self._size > self.capacity:
            raise ValueError
        self._size = self._size + n


    def withdraw(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError
        if n > self._size:
            raise ValueError
        self._size = self._size - n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size



