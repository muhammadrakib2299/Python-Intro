from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        n = len(words)
        
        while i < n:
            # Step 1: pick words greedily
            line_len = len(words[i])
            j = i + 1
            
            while j < n and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1
            
            line_words = words[i:j]
            num_words = len(line_words)
            
            # Step 2: build line
            if j == n or num_words == 1:
                # last line OR single word → left-justified
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
            else:
                total_chars = sum(len(w) for w in line_words)
                total_spaces = maxWidth - total_chars
                slots = num_words - 1
                
                space_per_slot = total_spaces // slots
                extra_spaces = total_spaces % slots
                
                line = ""
                for k in range(slots):
                    line += line_words[k]
                    # distribute extra spaces to the left slots
                    spaces = space_per_slot + (1 if k < extra_spaces else 0)
                    line += " " * spaces
                
                line += line_words[-1]  # last word
            
            res.append(line)
            i = j
        
        return res