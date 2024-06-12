import numpy as np

class TinyStatistician:

    def mean(self, x):
        if not x:
            return None
        total = 0
        for i in x:
            total += i
        return total / len(x)


    def median(self, x):
        if not x:
            return None
        sorted_x = sorted(x)
        n = len(sorted_x)
        mid = len(sorted_x) // 2
        if n % 2 == 0:
            return (sorted_x[mid - 1] + sorted_x[mid]) / 2
        else:
            return sorted_x[mid]


    def quartiles(self, x):
        if not x:
            return None
        sorted_x = sorted(x)
        n = len(sorted_x)
        
        quart1 = self.median(sorted_x[:n // 2])
        quart3 = self.median(sorted_x[(n + 1) // 2:])
        return [quart1, quart3]


    def var(self, x):
        if not x:
            return None
        mean = self.mean(x)
        variance = 0
        for value in x:
            variance += (value - mean) ** 2
        return variance / len(x)


    def std(self, x):
        if not x:
            return None
        variance = self.var(x)
        return variance ** 0.5
    

stat = TinyStatistician()
x = [1, 42, 300, 10, 59]

print(stat.mean(x))
# Expected result: 82.4

print(stat.median(x))
# Expected result: 42.0

print(stat.quartiles(x))
# Expected result: [10.0, 59.0]

print(stat.var(x))
# Expected result: 12279.439999999999

print(stat.std(x))
# Expected result: 110.81263465868862
