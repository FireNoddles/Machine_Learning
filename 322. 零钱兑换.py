#
# 给定不同面额的硬币 coins 和一个总金额 amount。
# 编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
# 如果没有任何一种硬币组合能组成总金额，返回 -1。
#
#
#
# 示例 1:
#
# 输入: coins = [1, 2, 5], amount = 11
# 输出: 3
# 解释: 11 = 5 + 5 + 1

#dp 从1 到 amount 依次计算每个值的最少组成方式
# dp[i]记录的是目标为i至少需要多少个硬币来兑换，
# 那么转移方程就是dp[i] = min([dp[i - coin] for coin in coins]) + 1。
# 但是有需要注意的就是要注意有无法兑换成功的情况不能考虑在内，
# 比如硬币给了[3, 4]，如果要凑出2，是不可能的，
# 后续如果有要基于2进行凑硬币的方案一律都是不考虑的。
#

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [-1 for i in range(amount+1)]
        dp[0] = 0
        for _ in range(1, amount+1):
            # 可选方法
            temp = []
            for __ in coins:
                if _ - __ >=0 and dp[_ - __]!=-1:
                    temp.append(dp[_ - __]+1)
            if temp !=[]:
                dp[_] = min(temp)
        return dp[-1]
