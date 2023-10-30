class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def is_valid_state(state):
            if len(state) == k: return True

        def get_candidates(state):
            lis = []
            start = max(state)+1 if state else 1
            for i in range(start,n+1):
                if i not in state:
                    lis.append(i)
            return lis

        def search(state, solutions):
            if is_valid_state(state):
                solutions.add(tuple(state.copy()))
                return

            for candidate in get_candidates(state):
                state.add(candidate)
                search(state, solutions)
                state.remove(candidate)

        
        solutions = set()
        state = set()
        search(state, solutions)
        return solutions
