#! Given a binary array nums, return the maximum niumber of maxcpsecutive 1's in the array 
nums = [1,1,0,1,1,1]
def maxconsecutive_ones(arr):
    m=len(arr)
    i= m-1  #! last element of the array 
    j=0   #! counting index which counts elments of current streak
    k=0   #!  max count (compares the max of 1's streak)
    while i>=0:
        if arr[i]==0:      
           print("new window has terminated")
           if k<j:
              k=j                 #! restore the max count in a streak in k index 
           j=0                    #! reset the counting index when 0 is found
        else:
            print("new window has begin")
            if arr[i]==1:         #! This  is redundant 
                j = j+1  
        i=i-1   #! move pointer towards left 
    return k 
print(maxconsecutive_ones(nums))
  

# What is a Streak?
# A streak is a continuous sequence of the same thing happening without interruption.