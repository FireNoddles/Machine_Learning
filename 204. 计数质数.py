#
# 统计所有小于非负整数 n 的质数的数量。
#
# 示例:
#
# 输入: 10
# 输出: 4
# 解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。

# 暴力法 On^2

# 高效解决这个问题的核心思路是和上面的常规思路反着来：排除法
#
# 首先从 2 开始，我们知道 2 是一个素数，那么 2 × 2 = 4, 3 × 2 = 6, 4 × 2 = 8... 都不可能是素数了。
#
# 然后我们发现 3 也是素数，那么 3 × 2 = 6, 3 × 3 = 9, 3 × 4 = 12... 也都不可能是素数了。
#
# 不需要遍历到 n，而只需要到 sqrt(n) 即可。为什么呢，我们举个例子，假设 n = 12。
#
#
# 12 = 2 × 6
# 12 = 3 × 4
# 12 = sqrt(12) × sqrt(12)
# 12 = 4 × 3
# 12 = 6 × 2
#

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        flag = [1 for i in range(n)]
        up = int(n ** 0.5) + 1
        for i in range(2, up):

            if flag[i] == 1:
                j = i * 2
                while j < n:
                    flag[j] = 0
                    j += i
        return sum(flag[2:])