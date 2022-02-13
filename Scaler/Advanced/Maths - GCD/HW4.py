import math

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        A.sort(reverse=True)
        ans = []
        m = {}
        for x in A:
            if x in m:
                m[x] -= 1
                if m[x] == 0:
                    del m[x]
            else:
                for y in ans:
                    m[math.gcd(x, y)] = m.get(math.gcd(x, y), 0) + 2
                ans.append(x)
        return ans

if __name__ == "__main__":
    s = Solution()
    A = [2, 2, 2, 2, 8, 2, 2, 2, 10]
    print(s.solve(A))
    A = [5,5,5,15]
    print(s.solve(A))
    A = [ 634, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 844, 4, 4, 2, 2, 1, 2, 2, 4, 1, 1, 4, 1, 1, 1, 1, 1, 4, 1, 4, 1, 1, 1, 4, 2, 4, 780, 20, 10, 6, 1, 2, 26, 4, 1, 15, 12, 5, 3, 1, 1, 1, 4, 65, 12, 1, 1, 5, 20, 2, 4, 20, 140, 70, 2, 1, 2, 2, 4, 1, 5, 28, 35, 7, 1, 1, 1, 28, 5, 28, 1, 1, 5, 140, 2, 2, 10, 70, 490, 2, 1, 2, 2, 2, 1, 5, 14, 35, 7, 1, 1, 1, 14, 5, 14, 1, 1, 5, 70, 2, 2, 6, 2, 2, 726, 1, 2, 22, 2, 1, 3, 6, 1, 33, 1, 1, 11, 2, 1, 6, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 677, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 86, 2, 2, 1, 1, 2, 1, 1, 1, 1, 43, 2, 2, 1, 1, 1, 1, 2, 2, 2, 26, 2, 2, 22, 1, 2, 286, 2, 1, 1, 2, 1, 11, 1, 1, 11, 2, 13, 2, 1, 1, 1, 2, 2, 4, 4, 4, 2, 2, 1, 2, 2, 376, 1, 1, 8, 1, 1, 1, 1, 1, 4, 1, 8, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 359, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 15, 5, 5, 3, 1, 1, 1, 1, 1, 3, 75, 5, 3, 1, 1, 1, 1, 25, 3, 1, 1, 5, 25, 2, 4, 12, 28, 14, 6, 1, 2, 2, 8, 1, 3, 168, 7, 21, 1, 1, 1, 28, 1, 168, 1, 1, 1, 28, 1, 1, 5, 35, 35, 1, 1, 1, 1, 1, 1, 5, 7, 595, 7, 1, 1, 1, 7, 5, 7, 1, 1, 5, 35, 1, 1, 3, 7, 7, 33, 1, 1, 11, 1, 1, 3, 21, 7, 693, 1, 1, 11, 7, 1, 21, 1, 1, 1, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 943, 1, 1, 1, 1, 1, 23, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 193, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 11, 1, 43, 11, 1, 1, 1, 1, 1, 11, 1, 1, 473, 1, 1, 1, 1, 1, 1, 1, 2, 4, 4, 28, 14, 2, 1, 2, 2, 4, 1, 1, 28, 7, 7, 1, 1, 1, 28, 1, 28, 1, 1, 1, 28, 1, 1, 65, 5, 5, 1, 1, 1, 13, 1, 1, 25, 1, 5, 1, 1, 1, 1, 1, 325, 1, 1, 1, 5, 25, 2, 4, 12, 28, 14, 6, 1, 2, 2, 8, 1, 3, 168, 7, 21, 1, 1, 1, 28, 1, 168, 1, 1, 1, 28, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 23, 1, 1, 1, 1, 1, 23, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 619, 1, 1, 1, 1, 5, 5, 5, 1, 1, 1, 1, 1, 1, 5, 1, 5, 1, 1, 1, 1, 1, 5, 1, 1, 1, 635, 5, 2, 4, 20, 140, 70, 2, 1, 2, 2, 4, 1, 25, 28, 35, 7, 1, 1, 1, 28, 25, 28, 1, 1, 700, 5 ]
    print(s.solve(A))