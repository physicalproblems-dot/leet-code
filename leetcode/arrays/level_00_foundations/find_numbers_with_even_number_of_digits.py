#! Given an array nums of integers, return how many of them contain an even number of digit
nums =[12, 345, 2, 6, 7896]

# def even_number_digits(arr):
#     m=len(arr)
#     i = m-1   #! last element of array 
#     j = m-1     #! index that store  no of digit in a number
#     k = 0     #! index that store  number of even number of digits
#     while i>=0:
#         arr[j]= arr[i]
#         j=j-1
#         i=i-1       #! moving tghe pointer from right to left   
#     return arr 

# print(even_number_digits(nums))


nums =[12, 345, 2, 6, 7896]

def even_number_digits(arr):
    m=len(arr)
    i = m-1   #! last element of array 
    j = 0     #! index that store  no of digit in a number
    k = 0     #! index that store  number of even number of digits
    while i>=0:
        while arr[i]>0:            #! count bumber of digits in arr[i] 
             arr[i] = arr[i]//10   #! remove the last digit 
             j =j+1
        if j%2 ==0:                 #! check the even or odd condition 
           k=k+1                    #! store in k index the even bunber of duigit
        i=i-1       #! moving tghe pointer from right to left   
    return k 

print(even_number_digits(nums))

#! Explanantion
#While loop within while loop