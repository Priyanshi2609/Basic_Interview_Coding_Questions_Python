#1. Largest Element in an array using python
'''
arr=[10, 89, 9, 56, 4, 80, 8]
largest_element=arr[0]
for i in range(1,len(arr)):
    if arr[i]>largest_element:
        largest_element=arr[i]
print(largest_element)'''

#2. Smallest Element in an array using python
'''
arr=[10, 89, 9, 56, 4, 80, 8]
smallest_element=arr[0]
for i in range(1,len(arr)):
    if arr[i]<smallest_element:
        smallest_element=arr[i]
print(smallest_element)'''

#3. Find the Smallest and largest element in an array
'''
arr=[10, 89, 9, 56, 4, 80, 8]
min=arr[0]
max=arr[0]
for i in range(1,len(arr)):
    if min>arr[i]:
        min=arr[i]
    if max<arr[i]:
        max=arr[i]
print(min,max)'''

#4. Find Second Smallest Element in an Array
'''
arr=[10,9,20,22,50,43,2,89,76,53,90,1]
smallest=arr[0]
second_smallest=arr[0]
for i in range(1,len(arr)):
    if smallest>arr[i]:
        second_smallest=smallest
        smallest=arr[i]
print(second_smallest)'''
        
#5. Calculate the sum of elements in an array
'''
arr = [10, 89, 9, 56, 4, 80, 8]
sum=0
for num in arr:
    sum+=num
print(sum)'''

#6. Reverse an Array
'''
arr = [10, 89, 9, 56, 4, 80, 8]
i=0
j=len(arr)-1
while(i<j):
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp
    i+=1
    j-=1
print(arr)'''

#7. Sort first half in ascending order and second half in descending order in an array
'''
def sort(arr):
    for i in range(len(arr)-1):
        min_idx=i
        for j in range(i+1,len(arr)):
            if arr[min_idx]>arr[j]:
                min_idx=j
        arr[i],arr[min_idx]=arr[min_idx],arr[i]
    return arr
def reverse(arr):
    i=0
    j=len(arr)-1
    while(i<j):
        temp=arr[i]
        arr[i]=arr[j]
        arr[j]=temp
        i+=1
        j-=1
    return arr
arr=[10, 89, 9, 56, 4, 80, 8]
mid=len(arr)//2
fisrt_half=sort(arr[0:mid])
second_half=sort(arr[mid:])
reverse_second=reverse(second_half)
print(fisrt_half+reverse_second)'''

#8. Python Program to sort the elements (Selection sort)
'''
def sort(arr):
    for i in range(len(arr)-1):
        min_idx=i
        for j in range(i+1,len(arr)):
            if arr[min_idx]>arr[j]:
                min_idx=j
        arr[i],arr[min_idx]=arr[min_idx],arr[i]
    return arr'''
    
#9. Finding the frequency of element Frequency of elements in an array
'''
arr = [10, 30, 10, 20, 10, 20, 30, 10]
def frequency_of_elements(arr):
    frequency_dict={}
    for num in arr:
        if num in frequency_dict:
            frequency_dict[num]+=1
        else:
            frequency_dict[num]=1
    return frequency_dict
print(frequency_of_elements(arr))'''

#10. Find the Longest Palindrome in an Array
'''
def is_palindrome(num):
    original_num=num
    reverse = 0
    while num > 0:
        rem = num % 10
        reverse = 10 * reverse + rem
        num = num // 10
    return reverse==original_num
arr = [1, 232, 5545455, 909090, 161]
largest=arr[0]
for i in range(1,len(arr)):
    if is_palindrome(arr[i]) and arr[i]>largest:
        largest=arr[i]
print(largest)'''

#11. Counting Distinct Elements in an Array
'''
arr= [10, 20, 40, 30, 50, 20, 10, 20]
distint_elements=len(set(arr))
print(distint_elements)
#OR

def distinct_elements(arr):
    distinct_elements=[]
    for num in arr:
        if num not in distinct_elements:
            distinct_elements.append(num)
    return len(distinct_elements)
print(distinct_elements(arr))'''

#12. Finding Repeating elements in an Array
'''
arr= [10, 20, 40, 30, 50, 20, 10, 20]
elements_count={}
for num in arr:
    if num not in elements_count:
        elements_count[num] = 1
    else:
        elements_count[num]+=1
repeating_elements=[key for key,value in elements_count.items() if value>1]
print(repeating_elements)'''

#13. Finding Non Repeating elements in an Array
'''
arr= [10, 20, 40, 30, 50, 20, 10, 20]
elements_count={}
for num in arr:
    if num not in elements_count:
        elements_count[num] = 1
    else:
        elements_count[num]+=1
repeating_elements=[key for key,value in elements_count.items() if value==1]
print(repeating_elements)'''

#14. Removing Duplicates elements from an array
'''
arr= [10, 20, 40, 30, 50, 20, 10, 20]
unique_elements=[]
seen=set()
for num in arr:
    if num not in seen:
        unique_elements.append(num)
        seen.add(num)
print(unique_elements)'''
        
#15. Finding minimum scalar product of two vectors
'''
def min_scalar_product(A,B):
    A.sort()
    B.sort(reverse=True)
    scalar_product=sum(a*b for a,b in zip(A,B))
    return scalar_product
A = [1, 3, 5]
B = [2, 4, 6]
result = min_scalar_product(A, B)
print(result)'''

#16. Finding maximum scalar product of two vectors
'''
def max_scalar_product(A,B):
    A.sort(reverse=True)
    B.sort(reverse=True)
    scalar_product=sum(a*b for a,b in zip(A,B))
    return scalar_product
A = [10, 30, 40, 20]
B =  [2, 4, 5, 1]
result = max_scalar_product(A, B)
print(result)'''

#17. count numbers of even and odd elements in an array
'''
arr=[11, 20, 35, 40, 53]
even_count=0
odd_count=0
for num in arr:
    if num%2==0:
        even_count+=1
    else:
        odd_count+=1
print(even_count,odd_count)'''

#18. 