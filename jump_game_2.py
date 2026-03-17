class Solution:
    def jump(self, nums):
        n = len(nums)
        if n <= 1:
            return 0
        jumps = 0
        maxReach = nums[0]
        steps = nums[0]
        for i in range(1, n):
            if i == n - 1:
                jumps += 1
                return jumps
            maxReach = max(maxReach, i + nums[i])
            steps -= 1
            if steps == 0:
                jumps += 1
                steps = maxReach - i
        return jumps
