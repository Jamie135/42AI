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
    def var(x):
        if not isinstance(x, (list, np.ndarray)) or len(x) == 0:
            return None
        try:
            mean = TinyStatistician.mean(x)
            variance = 0
            for value in x:
                variance += (value - mean) ** 2
            return variance / len(x)
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
# Expected result: [10, 59]

print(stat.var(x))
# Expected result: 12279.439999999999

print(stat.std(x))
# Expected result: 110.81263465868862
