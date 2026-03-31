class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        size = n + m - 1
        
        word = ['?'] * size
        locked = [False] * size  # Track positions fixed by 'T'
        
        # Step 1: Apply 'T' constraints
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    if word[i + j] == '?' or word[i + j] == str2[j]:
                        word[i + j] = str2[j]
                        locked[i + j] = True
                    else:
                        return ""
        
        # Step 2: Fill remaining with 'a'
        for i in range(size):
            if word[i] == '?':
                word[i] = 'a'
        
        # Step 3: Fix 'F' constraints
        for i in range(n):
            if str1[i] == 'F':
                # Check if substring matches str2
                match = True
                for j in range(m):
                    if word[i + j] != str2[j]:
                        match = False
                        break
                
                if match:
                    # Try to break WITHOUT touching locked positions
                    changed = False
                    for j in reversed(range(m)):
                        pos = i + j
                        
                        if locked[pos]:
                            continue  # can't modify
                        
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            if c != str2[j]:
                                word[pos] = c
                                changed = True
                                break
                        
                        if changed:
                            break
                    
                    if not changed:
                        return ""
        
        return "".join(word)