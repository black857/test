class LeapYears:
    def __init__(self):
        self.a = 2020
    def __iter__(self):
        return self
    def __next__(self):
        self.a = self.a - 1
        if ((self.a%4 == 0 and self.a%100!=0) or (self.a%400 == 0)):
            print(a)

leapYears = LeapYears()
for i in leapYears:
    if i >= 2000:
        print(i)
    else:
        break