class Solution:
    def isInterleave(self, s1, s2, s3):
        if s1 == "" and s2 == "":
            if s3 == "":
                return True
            else:
                return False
        if len(s1) > len(s2):
            candidate = str(s1[0])
            for i in range(len(s2)):
                candidate += s2[i]
                candidate += s1[i+1]
            print(candidate)
            if candidate == s3:
                return True
            else:
                return False
        elif len(s2) > len(s1):
            candidate = str(s2[0])
            for i in range(len(s1)):
                candidate += s1[i]
                candidate += s2[i+1]
            print(candidate)
            if candidate == s3:
                return True
            else:
                return False
        else:
            candidate_1 = ""
            candidate_2 = ""
            for i in range(len(s1)):
                candidate_1 += s1[i]
                candidate_1 += s2[i]
                candidate_2 += s2[i]
                candidate_2 += s1[i]
            print(candidate_1)
            print(candidate_2)
            if candidate_1 == s3 or candidate_2 == s3:
                return True
            else:
                return False

sol = Solution()
a = sol.isInterleave("aabcc", "dbbca", "aadbbbaccc")
print(a)