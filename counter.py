class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        print("next")
        print(self)
        if self.current < self.high:
            num = self.current
            self.current += 1
            return num
        raise StopIteration


c = Counter(10, 12)

for x in c:
    print(x)
    
    
    
    
    
answer =:
 "no" if answer == yes
 else yes
    
if answer == "yes":
    answer = "no"
else:
    answer = "yes"
