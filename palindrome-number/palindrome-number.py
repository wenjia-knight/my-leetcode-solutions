class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        string = str(x)
        for i in range(len(string)):
            if string == string[::-1]:
                return True
            else:
                return False