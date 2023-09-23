class RecentCounter(object):

    def __init__(self):
        self.time_range = []

    def ping(self, t):
        counter = 1
        self.time_range.append(t)
        for i in reversed(range(len(self.time_range)-1)):
            if t - self.time_range[i] <= 3000:
                counter += 1
            else:
                return counter
        return counter

        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)