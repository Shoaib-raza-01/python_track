class Counter:
    value = 0
    def incr(self):
        self.value += 1
        print(self.value)

    def decr(self):
        self.value -= 1
        print(self.value)

    def incrby(self,n):
        self.value += n
        print(self.value)

    def decrby(self,n):
        self.value -= n
        print(self.value)

c = Counter()
print (c.incr(),c.decr(),c.incrby(5),c.decrby(3))