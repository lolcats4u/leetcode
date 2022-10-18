len_of_nums_pre_filter = len(nums)

for i, number in enumerate(nums):
    while nums.count(number) > 1:
        nums.pop(i)

len_of_nums_post_filter = len(nums)

empty_elements = len_of_nums_pre_filter - len_of_nums_post_filter

while empty_elements != 0:
    nums.append(None)
    empty_elements -= 1

print(len_of_nums_post_filter)