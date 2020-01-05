def twoSum(numbers, target):
    left = 0
    right = len(numbers)-1
    while left < right:
        n = numbers[left]+numbers[right]
        if n == target:
            return left+1, right+1
        elif n < target:
            left+=1
        else:
            right-=1

            
print(twoSum([2, 3, 6, 8, 10], 16))