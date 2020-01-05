def twoSum(nums, target):
    k = 0
    for i in nums:
        l = k
        for j in nums[k+1:]:
            l += 1
            if i+j == target:
                return k, l
        k += 1
        
