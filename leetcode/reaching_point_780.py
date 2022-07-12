class Solution:
    def reachingPoints(self, sx, sy, tx, ty):
        while tx >= 1 and ty >= 1:
            if tx == sx and ty == sy:
                return True
            if tx > ty:
                tx = tx - ty
            else:
                ty = ty - tx
        return False

sol = Solution()
a = sol.reachingPoints(1, 1, 2, 2)
b = sol.reachingPoints(1, 1, 1, 1)
print(a)
print(b)