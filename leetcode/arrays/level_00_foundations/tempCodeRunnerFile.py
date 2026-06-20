nums1 = [1, 2, 3, 3,4]
nums2 = [2, 5, 6]
m = len(nums1)
n = len(nums2)
combined = nums1+nums2
p = len(combined)
small_to_large_arr = sorted(combined, reverse=False) #! By default python sorrt from low to high value 
print(small_to_large_arr)
