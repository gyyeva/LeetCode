class Solution:
    def twoSum(self, nums, target):
        dic = {}
        for i in range(0,len(nums)):
            if target - nums[i] not in dic:
                dic[nums[i]] = i
            else:
                index1 = dic[target - nums[i]]
                index2 = i
                return([index1,index2])
