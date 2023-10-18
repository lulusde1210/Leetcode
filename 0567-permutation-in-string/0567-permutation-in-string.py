class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = Counter(s1)
        count2 = Counter(s2[:len(s1)])

        if count1 == count2:
            return True

        i = 1
        j = len(s1)+i-1

        while j < len(s2):
            count2[s2[i-1]] -= 1
            if count2[s2[i-1]] == 0:
                 del count2[s2[i-1]]            
            count2[s2[j]] = count2.get(s2[j],0)+1

            if count1 == count2:
                return True
            i += 1
            j = len(s1) + i -1
        
        return False

            

        # compare = defaultdict(int)

        # count = Counter(s1)

        # for i in range(len(s2)):
        #     s = s2[i:len(s1)+i]
        #     if count == Counter(s):
        #         return True

        # return False


