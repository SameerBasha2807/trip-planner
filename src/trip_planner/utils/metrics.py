import time

class Metrics:
    def __init__(self):
        self.start = time.time()
        

    def total_latency(self):
        return round(time.time() - self.start, 2)