class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        ans = []
        kelvin = celsius + 273.15
        Fahrenheit = celsius * 1.80 + 32.00
        ans.append(kelvin)
        ans.append(Fahrenheit)

        return ans