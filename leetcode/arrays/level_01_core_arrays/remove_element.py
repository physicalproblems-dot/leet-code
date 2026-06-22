# nums = [3,2,2,3]
# nums = [0,1,2,2,3,0,4,2]
# def remove_element(arr):
#     m= len(arr)
#     target= 2
#     i=m-1   #! the last element of the array       
#     k=0     #! counter initialize
#     while i>=0:    #! iterate through all the element of the the array from right to left
#         if arr[i]==2:
#             arr[i]=0
#             k=k+1
#         else:
#             arr[i]=arr[i]    
#         i=i-1
#     return m-k, arr
# print(remove_element(nums))

#! first k elements must be the non-target values
nums = [0,1,2,2,3,0,4,2]
def remove_element(arr):
    m= len(arr)
    target= 2
    i=0      #! the first element pointer of the array 
    j=m-1     #! the last element pointer of the array 
    k=0      #! counter initialize
    while i<=j:
        if arr[i]==target:
            arr[i]= arr[j]
            j=j-1
            k=k+1
        else:
            i=i+1                            
    return i, arr
print(remove_element(nums))

#! Explanantion
#Replace in one way
# Make the two pointers index condition  on one another 
# iteration condition are wuthin the branching statement
# Third type of condition   