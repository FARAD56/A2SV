class Solution:
    def splitString(self, s: str) -> bool:
        def is_valid_state(state):
            if state[1] == len(s): return True

        def get_candidates(state):
            lis,curr = [], ''
            if state[0] == float("inf"):
                for i in range(len(s)):
                    curr += s[i]
                    lis.append((int(curr), i+1))
            else:
                for i in range(state[1], len(s)):
                    curr += s[i]
                    if int(curr) + 1 == state[0]:
                        lis.append((int(curr),i+1))
            return lis



        def search(state, solutions):
            if is_valid_state(state):
                solutions.add(state)
                return

            for candidate in get_candidates(state):
                state = candidate
                search(state, solutions)
        
        solutions = set()
        state = (float("inf"),-1)
        search(state, solutions)
        print(solutions)
        return True if len(solutions) > 1 else False