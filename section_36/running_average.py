class Rav:
    def __init__(self):
        self.accumulator = 0
        self.size = 0

    def inner(self, number):
        self.accumulator += number
        self.size += 1
        return self.accumulator / self.size


o = Rav()
print(o.inner(10))
print(o.inner(11))

o2 = Rav()
print(o2.inner(11))

"""
def running_average():
    running_average.accumulator = 0
    running_average.size = 0
    print(f"First {running_average.accumulator}")

    def inner(number):
        print(f"Inner {running_average.accumulator}")
        running_average.accumulator += number
        running_average.size += 1
        return running_average.accumulator / running_average.size
        
    return inner


rAvg = running_average()
print(rAvg(10))
print(rAvg(11))

rAvg2 = running_average()
print(rAvg2(12))

"""
