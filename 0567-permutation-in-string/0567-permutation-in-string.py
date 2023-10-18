class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        compare = defaultdict(int)

        count = Counter(s1)

        for i in range(len(s2)):
            s = s2[i:len(s1)+i]
            if count == Counter(s):
                return True

        return False


