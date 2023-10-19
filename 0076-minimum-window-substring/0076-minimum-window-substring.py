class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="" or len(t) > len(s): 
            return ""

        tCount = {}
        sCount = {}

        for c in t:
            tCount[c] = tCount.get(c,0) + 1
            sCount[c] = 0
        
        need, have = len(tCount), 0
        res = [-1,-1]
        resLen = float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            
            if c in sCount:
                sCount[c] += 1
                if sCount[c] == tCount[c]:
                    have += 1
            
            while have == need:
                if (r-l+1) < resLen:
                    res = [l,r]
                    resLen = r-l+1

                if s[l] in sCount:
                    sCount[s[l]] -= 1
                    if sCount[s[l]] < tCount[s[l]]:
                        have -= 1
                
                l +=1
            
        l,r = res
        return s[l:r+1] if resLen != float("infinity") else ""

        
                

            









