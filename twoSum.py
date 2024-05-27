
class Solution:

    def two_sum(self,nums, target):
        
        complement_dict = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in complement_dict:
                return [complement_dict[complement], i]
            complement_dict[num] = i

        return []

solution = Solution()
target = 9

nums = [2, 7, 11, 15]
print(solution.two_sum(nums, target))