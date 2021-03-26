l = [308, 323, 249, 339, 324, 406, 11, 376, 172, 492, 47, 290, 58]

def sort(nums):
	for i in range(len(l)):
		minpos = i
		for j in range(i,len(l)):
			if nums[j]<nums[minpos]:
				minpos = j
				nums[minpos] ,nums[i] = nums[i],nums[minpos]

print(f"Unsorted\n{l}")

sort(l)


print(f'Sorted\n{l}')

