#! sqare and sort in increasing order
# nums =[-4, -1, 0, 3, 10]
# def sqare_sort(arr):
#     m= len(arr) 
#     i = m-1
#     j=  m-1
#     while i>=0:
#         arr[j] = arr[i]*arr[i]
#         i=i-1
#         j=j-1 
#     return arr
# print(sqare_sort(nums))

#! I have to compare their absolute values then sort it and finally sqare it 
nums =[-4, -1, 0, 3, 10]
def sqare_sort(arr):
    m = len(arr)
    solution=[0]*m
    i = m-1   #! pointer at extreme right 
    j = m-m   #! pointer at extreme left
    k = m-1   #! position pointer at extreme right
    while i>=j:
        if arr[i]*arr[i]>arr[j]*arr[j]:
           solution[k] = arr[i]**2
           i=i-1         
        else:  
           solution[k] = arr[j]**2
           j=j+1
        k=k-1     #! position pointer moving right to left    
           
    return solution
print(sqare_sort(nums))