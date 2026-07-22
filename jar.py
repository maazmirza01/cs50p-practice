class Jar:
    def __init__(self, capacity=12):
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        print(self.size * "🍪")

    def deposit(self, n):
        if n + self.size > self.capacity:
            raise ValueError("No Capacity")
        else:
            self._size = n + self.size

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Insufficient Cookies")
        else:
            self._size = self.size - n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

jar = Jar(100)
print(jar.size)
jar.deposit(75)
jar.withdraw(70)
print(jar)
