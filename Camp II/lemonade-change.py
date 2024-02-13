class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        Dict = defaultdict(int)
        change = 0
        for num in bills:
            if num == 5: Dict[5] += 1

            if num == 10:
                if not Dict[5]: return False
                Dict[10] += 1
                Dict[5] -= 1
            
            if num == 20:
                if Dict[5] and Dict[10]:
                    Dict[5] -= 1
                    Dict[10] -= 1
                elif Dict[5] >= 3: Dict[5] -= 3
                else: return False
                Dict[20] += 1     
        return True

