nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

new_nums = set()
count = 0

for i in nums1:
    count = nums2.count(i)
    if count:
        new_nums.add(i)

print(list(new_nums))


