import numpy as np

class TinyStatistician:

    @staticmethod
    def mean(x):
        if not isinstance(x, (list, np.ndarray)) or len(x) == 0:
            return None
        try:
            total = 0
            for value in x:
                total += value
            return total / len(x)
        except:
            return None


    @staticmethod
    def median(x):
        if not isinstance(x, (list, np.ndarray)) or len(x) == 0:
            return None
        try:
            sorted_x = sorted(x)
            n = len(sorted_x)
            middle = n // 2
            if n % 2 == 0:
                return (sorted_x[middle - 1] + sorted_x[middle]) / 2
            else:
                return sorted_x[middle]
        except:
            return None


    @staticmethod
    def quartiles(x):
        if not isinstance(x, (list, np.ndarray)) or len(x) == 0:
            return None
        try:
            sorted_x = sorted(x)
            n = len(sorted_x)
            q1 = sorted_x[int(n * 0.25)]
            q3 = sorted_x[int(n * 0.75)]
            return [float(q1), float(q3)]
        except:
            return None
        

    @staticmethod
    def percentile(x, p):
        if not isinstance(x, (list, np.ndarray)) or len(x) == 0:
            return None
        if not isinstance(p, (int, float)) or not (0 <= p <= 100):
            return None
        try:
            sorted_x = sorted(x)
            # k is the index in the sorted list where the p-th percentile value lies
            k = (len(sorted_x) - 1) * (p / 100)
            # round k to the nearest greater and smaller interger
            f = int(np.floor(k))
            c = int(np.ceil(k))
            # if k is an integer then f = c and the percentile lies exactly at that index
            if f == c:
                return float(sorted_x[int(k)])
            
            # linear interpolation
            # d0 is the contribution from the lower index f, weighted by how close k is to c
            d0 = sorted_x[f] * (c - k)
            # d1 is the contribution from the upper index c, weighted by how close k is to f
            d1 = sorted_x[c] * (k - f)
            return float(d0 + d1)
        except:
            return None


    @staticmethod
    def var(x):
        if not isinstance(x, (list, np.ndarray)) or len(x) == 0:
            return None
        try:
            mean = TinyStatistician.mean(x)
            return sum((value - mean) ** 2 for value in x) / (len(x) - 1)
        except:
            return None


    @staticmethod
    def std(x):
        if not isinstance(x, (list, np.ndarray)) or len(x) == 0:
            return None
        try:
            variance = TinyStatistician.var(x)
            return variance ** 0.5
        except:
            return None
    

stat = TinyStatistician()
x = [1, 42, 300, 10, 59]

print(stat.mean(x))
# Expected result: 82.4

print(stat.median(x))
# Expected result: 42.0

print(stat.quartiles(x))
# Expected result: [5.5, 179.5]

print(stat.percentile(x, 10))  # Expected: 4.6
print(stat.percentile(x, 15))  # Expected: 6.4
print(stat.percentile(x, 20))  # Expected: 8.2

print(stat.var(x))
# Expected result: 12279.439999999999

print(stat.std(x))
# Expected result: 110.81263465868862
