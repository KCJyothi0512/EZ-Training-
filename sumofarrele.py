#find sum of array elements using divide and conquer approach
'''def sum_of_array(arr, low, high):
    if low == high:
        return arr[low]
    mid = (low + high) // 2
    left_sum = sum_of_array(arr, low, mid)
    right_sum = sum_of_array(arr, mid+1, high)
    return left_sum + right_sum

n = int(input("Enter the number of elements for the list:"))
a = []
for i in range(0, n):
    element = int(input("Enter element:"))
    a.append(element)

print("The list is:")
print(a)

print("Sum of items in the list:")
b = sum_of_array(a, 0, n - 1)
print(b)'''
def sum_(l,si,li):
    if si==li:
        return l[si]

    if si>li:
        return -1
    mid=(si+li)//2
    return sum_(l,si,mid)+sum_(l,mid+1,li)

