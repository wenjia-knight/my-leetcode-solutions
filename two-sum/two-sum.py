class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {} # val : inx
        for i,n in enumerate(nums): # index of original in nums
            diff = target - n
            if diff not in hashmap:
                hashmap[n] = i
            else:
                return [hashmap[diff], i]
