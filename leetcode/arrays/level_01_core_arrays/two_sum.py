#! Two sum 
#! assumption is that each input will have exactly one solution , or no number will be repeated
nums =[2,7,11,15]
target = 9

#! brute force method
def two_sum(arr, target):
    m=len(arr)
    i = 0      #! pointer that points extreme left 
    j= m-1      #! pointer that points extreme right
    while i<m:
        while j>i:
            if arr[i]+arr[j]==target:  
               return [i,j]
            j=j-1     #! move pointers right left           
        i=i+1  #! move pointers top left to right 
        return []
    
print(two_sum(nums, target))

#! debug it 