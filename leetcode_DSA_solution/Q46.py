# DFS
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        self._permute(nums, [], ans)
        return ans

    def _permute(self, nums, cur, ans):
        if len(nums) == 0:
            ans.append(cur[:])
            return
        for i, num in enumerate(nums):
            cur.append(num)
            self._permute(nums[:i] + nums[i + 1:], cur, ans)
            cur.pop()