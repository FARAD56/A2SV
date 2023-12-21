class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        check_ingredients = set(recipes)
        check_supplies = set(supplies)

        prerequisite = defaultdict(int)
        graph = defaultdict(list)

        for i in range(len(recipes)):
            for ingredient in ingredients[i]: 
                if ingredient in check_ingredients:
                    prerequisite[recipes[i]] += 1
                    prerequisite[ingredient] += 0
                    graph[ingredient].append(recipes[i])
        
        queue = deque()
        for idx,recipe in enumerate(recipes):
            if not prerequisite[recipe]:
                check = True
                for ingredient in ingredients[idx]:
                    if ingredient not in check_supplies:
                        check = False
                if check:
                    queue.append(recipe)

        ans = []
        while queue:
            leave = queue.popleft()
            ans.append(leave)

            for neighbour in graph[leave]:
                prerequisite[neighbour] -= 1
                if not prerequisite[neighbour]:
                    queue.append(neighbour)
        return ans


