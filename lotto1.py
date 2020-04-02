from random import randrange

nums = []

def checkDuplicate(num_list, target):

    result = False

    for x in num_list:
        if x == target:
            result = True
            break

    return result


# 1.루프를 nums가 6개가 되는 동안
while len(nums) < 6 :

# 2. 1부터 45 사이의 숫자를 뽑는다.
    num = randrange(1, 46)

# 3.기존에 뽑은 값과 새로 뽑은 값을 비교하여 있다면 다시 뽑는다. (중복체크 함수 생성)
    if checkDuplicate(nums, num) == True :
        continue

    nums.append(num)
print(nums)


