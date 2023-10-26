class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if flowerbed[0] == 0 and len(set(flowerbed)) ==1:
            if len(flowerbed) % 2 == 1:
                return (len(flowerbed)+1)// 2 >= n
            return len(flowerbed)// 2 >= n

        total, zer = 0,0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                zer += 1
            else:
                if zer%2 == 0 and zer > 0 and i!=zer:
                    total -= 1
                total += (zer // 2)
                zer = 0
        total += zer//2
        return total >= n


                