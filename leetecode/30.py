from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        total_words = len(words)
        window_len = word_len * total_words
        word_count = Counter(words)
        
        result = []
        
        # We try starting from each possible offset within word_len
        for i in range(word_len):
            left = i
            current_count = Counter()
            count = 0  # number of valid words in current window
            
            # Move right pointer in steps of word_len
            for right in range(i, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]
                
                if word in word_count:
                    current_count[word] += 1
                    count += 1
                    
                    # If word appears too many times, shrink window
                    while current_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        current_count[left_word] -= 1
                        left += word_len
                        count -= 1
                    
                    # If all words matched
                    if count == total_words:
                        result.append(left)
                else:
                    # Reset window if invalid word found
                    current_count.clear()
                    count = 0
                    left = right + word_len
        
        return result