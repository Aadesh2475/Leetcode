class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        # If the total count of '1's is less than k, no beautiful substring exists
        if s.count('1') < k:
            return ""
        
        ans = ""
        l = 0
        ones_count = 0
        
        for r in range(len(s)):
            if s[r] == '1':
                ones_count += 1
                
            # Shrink the window from the left while it still contains k ones
            while ones_count == k:
                candidate = s[l:r+1]
                
                # Update ans if it's shorter, or if it's the same length but lexicographically smaller
                if not ans or len(candidate) < len(ans) or (len(candidate) == len(ans) and candidate < ans):
                    ans = candidate
                    
                if s[l] == '1':
                    ones_count -= 1
                l += 1
                
        return ans