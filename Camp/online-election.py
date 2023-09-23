class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.persons = persons

        self.arr,self.recent = [[self.persons[0]]],[self.persons[0]]
        for i in range(1,len(self.persons)):
            count = Counter(self.persons[:i+1])
            count = count.most_common()
            count = [key for key, value in count if value == count[0][1]]
            self.recent.append(self.persons[i] if  self.persons[i] in count else self.recent[-1])
            self.arr.append(count)

        

    def q(self, t: int) -> int:
        point = bisect_right(self.times,t)-1 if bisect_right(self.times,t)-1 < len(self.persons) else len(self.persons)-1
        a = self.arr[point]
        if len(a) == 1:
            return a[0]
        return self.persons[point] if self.persons[point] in self.arr[point] else self.recent[point]

        

        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)