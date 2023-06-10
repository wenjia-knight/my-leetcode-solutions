class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        running_sum = []  # Initialize an empty array for the running sum                            
        for i in range(len(nums)):
            if i == 0:
                running_sum.append(nums[i])  # For the first element, append it as is
            else:
                running_sum.append(running_sum[i - 1] + nums[i])  # Calculate the running sum
        return running_sum