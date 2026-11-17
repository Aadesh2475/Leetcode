from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        counts = Counter(s)

        def can_form(idx, current_counts):

            path = []
            c = current_counts.copy()
            for i in range(idx, n):
                # Find the smallest available character
                found = False
                for ch in sorted(c.keys()):
                    if c[ch] > 0:
                        path.append(ch)
                        c[ch] -= 1
                        found = True
                        break
                if not found:
                    return None
            return "".join(path)


        path = []
        
        def backtrack(i, counts_map):
            if i == n:
                res = "".join(path)
                return res if res > target else ""
            
            target_char = target[i]
            if counts_map[target_char] > 0:
                counts_map[target_char] -= 1
                path.append(target_char)
                
                res = backtrack(i + 1, counts_map)
                if res:
                    return res
                
                path.pop()
                counts_map[target_char] += 1
                
            for ch in sorted(counts_map.keys()):
                if ch > target_char and counts_map[ch] > 0:
                    counts_map[ch] -= 1
                    path.append(ch)

                    remaining = []
                    c_copy = counts_map.copy()
                    possible = True
                    for j in range(i + 1, n):
                        found_next = False
                        for next_ch in sorted(c_copy.keys()):
                            if c_copy[next_ch] > 0:
                                remaining.append(next_ch)
                                c_copy[next_ch] -= 1
                                found_next = True
                                break
                        if not found_next:
                            possible = False
                            break
                    
                    if possible:
                        return "".join(path) + "".join(remaining)
                    
                    path.pop()
                    counts_map[ch] += 1
                    
            return ""

        return backtrack(0, counts)