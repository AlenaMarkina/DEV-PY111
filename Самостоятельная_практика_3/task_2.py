nums = [3, 6, 9, 1]
nums.sort()  # nums = [1, 3, 6, 9]

diff = set()

for i in range(len(nums)-1):  # [0, 1, 2]
    diff.add(nums[i+1] - nums[i])

print(max(diff))


