#! merging two arrays 
# nums1 = [1, 2, 3]
# nums2 = [2, 5, 6]
# m = len(nums1)
# n = len(nums2)
# combined = nums1+ nums2
# p = len(combined)
# print(combined, p) 

#! merging two arrays and sort it in increasing order (from smallest value to largest value)
# nums1 = [1, 2, 3, 3,4]
# nums2 = [2, 5, 6]
# m = len(nums1)
# n = len(nums2)
# combined = nums1+nums2
# p = len(combined)
# small_to_large_arr = sorted(combined, reverse=False) #! By default python sorrt from low to high value 
# print(small_to_large_arr)

#! merging two arrays and sort it in decreasing order (from high to low )
# nums1 =[1, 2, 3, 3, 4]
# nums2 =[2, 5, 6]
# m = len(nums1)
# n = len(nums2)
# combined = nums1+nums2
# p = len(combined)
# large_to_small_arr = sorted(combined, reverse= True)
# print(large_to_small_arr)

#! Merging sorted array (Two pointers algorithm)
# nums1=[1,2,3,0,0,0]
# m=3
# nums2=[2,5,6]
# n=3

nums1 = [4,5,6, 0, 0, 0]
nums2 = [1,2,3]
m=3
n=3
def merge(nums1,m, nums2, n):
   #! pointer 1 that points to the last valid element of nums1
   i=m-1
   #! pointer 2 that points to the last valid element in nums2
   j=n-1
   #! points to the the position where the next largest element should placed
   k=m+n-1      #! python pointer starts with 0
   #! now we have to compare with last valid elements of both the array and fill up the 0 
   #! we are also utilizing the fact they are already sorted in decreasing order..
   #! Now compare the last valid elements of both arrays and fills up the nums1 0 positional values
   #! compare 3 and 6 i.e. the last element of both nums1 and nums2 array
   #! Since 6 is bigger, by using the 3rd pointer store 6 at last element of nums1
   while i>=0 and j>=0:
      if nums1[i]>nums2[j]:
         nums1[k] = nums1[i]
         i=i-1  #! move pointers left direction of nums1 array
      else :
         nums1[k] = nums2[j]
         j=j-1  #! move poniters in left direction of nums2 array
      k =k-1 
   while j>=0:
      nums1[k] = nums2[j]
      j=j-1
      k=k-1   
   return nums1   

#! solution block

modified_nums1 = merge(nums1, m, nums2, n)
print(modified_nums1)    

#! Explannation
#! compare finite number elements of bothe array and store in the first array numbers accordingly in non decreasing order
#! Time complexity 
#! While loop variable is i and j both of then at max runs m and n times
#! O(m+n) time complexity
#! Space complexity
#! No new array, dicitionary or recursion
#! O(1) space complexity
