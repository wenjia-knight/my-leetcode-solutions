class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_wealth = 0
        for i in range(len(accounts)):
            wealth = sum(accounts[i])
            max_wealth = max(max_wealth, wealth)
        return max_wealth