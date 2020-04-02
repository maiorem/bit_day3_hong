
nums = [10,20,30,40,50,60,70,80]

score = 67

nums.sort(key = lambda num: abs(score-num))

print(nums)