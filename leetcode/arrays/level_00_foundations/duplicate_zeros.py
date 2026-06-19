
# arr = [1,2,3]
# m = len(arr)
# def duplicate_elements(arr,m):
#      i =m-1                 #! pointer i that points towards last valid number of array 0
#      j =m-1                 #! pointer j that points towards last valid position of array (8th place )
#      while i>=0:
#             arr[j]=arr[i]
#             i=i-1           #! move element identifier pointers left to right direction       
#             j=j-1          #! move placeholder pointer from left to right           
#      return arr

# output = duplicate_elements(arr,m)
# print(output)
#! use pointer i from left to right to check its element is 0 or not
#! use pointer j from left to right to fill the value 0 
#! one pointer algorithm
#! Where is the fault in my logic??



#! Hints
#When elements must be shifted within the same array, processing from the end is often safer than processing from the beginning.


#! Shift elements towards right
# arr=[1,2,3]
# m=len(arr)
# def right_shift(arr,m):
#       i=m-1
#       j=m-1
#       while i>0:
#             arr[j]= arr[i-1]
#             i=i-1
#             j=j-1
#       arr[0]=0      
#       return arr        
# print(right_shift(arr,m))

#! shift elements towards left



#! Duplicate zeroes
arr=[1,0,2,3,0,4,5,0]
def duplicate_Zeros(arr):
    m = len(arr)
    zeros = arr.count(0)  #! count number of zeroes in the array its 3 in this case 
    i=m-1   #! last element of the array
    j= m+zeros-1 #! last element index of 11 th length virtual array
    while i>=0:
        if j<m:
            arr[j]= arr[i]

        if arr[i]==0:
            j=j-1
            if j<m:
             arr[j]=0
        i=i-1             #! moving from right to left
        j=j-1             #! moving from right to left   
    return arr
print(duplicate_Zeros(arr))

#! Write a logic table by hand to solve the problem   
#! Concept of virtual array  
#! j points outside the real array         

#!       i 1  2   3   4   5   6   7   8       
#!    arr=[1, 0,  2,  3,  0,  4,  5,  0]  _  _  _    m= 8   #! Application of auxillay concept of ghost array and ghost index
#!       j 1  2   3   4   5   6   7   8   9  10 11 