from typing import List

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        
        # Step 1: sort indices by position
        idx = list(range(n))
        idx.sort(key=lambda i: positions[i])
        
        stack = []  # will store indices of robots moving right
        
        # Step 2: simulate collisions
        for i in idx:
            if directions[i] == 'R':
                stack.append(i)
            else:
                # current robot moving left
                while stack and healths[i] > 0:
                    j = stack[-1]  # last right-moving robot
                    
                    if healths[j] < healths[i]:
                        stack.pop()
                        healths[i] -= 1
                        healths[j] = 0
                    elif healths[j] > healths[i]:
                        healths[j] -= 1
                        healths[i] = 0
                        break
                    else:
                        # equal health
                        stack.pop()
                        healths[j] = 0
                        healths[i] = 0
                        break
        
        # Step 3: collect survivors in original order
        return [healths[i] for i in range(n) if healths[i] > 0]