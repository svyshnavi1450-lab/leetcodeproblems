class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        robots = sorted([(positions[i], i) for i in range(n)])
        stack = [] 
        health = healths[:]
        for pos, i in robots:
            if directions[i] == 'R':
                stack.append(i)
            else:
                while stack and health[i] > 0:
                    j = stack[-1]
                    if health[j] < health[i]:
                        stack.pop()
                        health[i] -= 1
                        health[j] = 0
                    elif health[j] > health[i]:
                        health[j] -= 1
                        health[i] = 0
                    else:
                        health[j] = 0
                        health[i] = 0
                        stack.pop()
                        break
        result = []
        for i in range(n):
            if health[i] > 0:
                result.append(health[i])
        return result