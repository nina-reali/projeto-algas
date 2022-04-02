import time
from datetime import datetime
import sys

class Data:
    def sum_time_memory(array):
        start_time = datetime.now()
        start = array[0]
        end = array[1]
        gap = array[2]
        data = []

        for item in range(end, start, -(gap)):
            data.append([{'time': (datetime.now() - start_time).total_seconds(), 'memory': sys.getsizeof(item), 'start': start, 'end': end, 'gap': gap, 'transaction': item}])


        return data