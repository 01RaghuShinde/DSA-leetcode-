class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        s = self.countAndSay(n - 1)
        ans, cnt = '', 1
        for i in range(len(s)):
            if i + 1 < len(s) and s[i] == s[i + 1]:
                cnt += 1
            else:
                ans += str(cnt) + str(s[i])
                cnt = 1
        return ans