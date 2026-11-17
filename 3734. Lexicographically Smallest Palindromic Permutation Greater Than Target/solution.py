from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        counts = Counter(s)
        
        # Step 1: Check if a palindromic permutation is possible
        odd_chars = [ch for ch, freq in counts.items() if freq % 2 != 0]
        if len(odd_chars) > (1 if n % 2 != 0 else 0):
            return ""
            
        half_len = n // 2
        
        # Identify the middle character if n is odd
        mid_char = odd_chars[0] if odd_chars else ""
        if mid_char:
            counts[mid_char] -= 1
            
        # Each remaining character count must be halved for the first half of the palindrome
        for ch in counts:
            counts[ch] //= 2
            
        # We need to construct the first half of length half_len
        target_half = target[:half_len]
        
        path = []
        
        def backtrack(i, counts_map):
            if i == half_len:
                first_half = "".join(path)
                full_palindrome = first_half + (mid_char if mid_char else "") + first_half[::-1]
                return full_palindrome if full_palindrome > target else ""
            
            target_char = target_half[i]
            
            # Option 1: Try matching target_half[i] exactly
            if counts_map[target_char] > 0:
                counts_map[target_char] -= 1
                path.append(target_char)
                res = backtrack(i + 1, counts_map)
                if res:
                    return res
                path.pop()
                counts_map[target_char] += 1
                
            # Option 2: Try the smallest available character strictly greater than target_half[i]
            for ch in sorted(counts_map.keys()):
                if ch > target_char and counts_map[ch] > 0:
                    counts_map[ch] -= 1
                    path.append(ch)
                    
                    # Greedily pick the smallest available for the rest of the half
                    remaining_half = []
                    c_copy = counts_map.copy()
                    possible = True
                    for j in range(i + 1, half_len):
                        found_next = False
                        for next_ch in sorted(c_copy.keys()):
                            if c_copy[next_ch] > 0:
                                remaining_half.append(next_ch)
                                c_copy[next_ch] -= 1
                                found_next = True
                                break
                        if not found_next:
                            possible = False
                            break
                            
                    if possible:
                        first_half = "".join(path) + "".join(remaining_half)
                        full_palindrome = first_half + (mid_char if mid_char else "") + first_half[::-1]
                        return full_palindrome
                        
                    path.pop()
                    counts_map[ch] += 1
                    
            return ""

        return backtrack(0, counts)