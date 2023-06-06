class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """

        salary.sort()
        salary.remove(salary[-1])
        salary.remove(salary[0])

        total = 0.0

        for item in salary:
            total += item

        average = total/len(salary)

        return average