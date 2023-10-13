#find maximum element in an array using divide and conquer approach
def find_max(arr):
    if len(arr) == 0:
        return None

    max_element = arr[0]

    for element in arr:
        if element > max_element:
            max_element = element

    return max_element

n = int(input("Enter the number of elements for the list:"))
a = []
for i in range(0, n):
    element = int(input("Enter element:"))
    a.append(element)

print("The list is:")
print(a)

max_value = find_max(a)
if max_value is not None:
    print("The maximum element in the list is:", max_value)
else:
    print("The list is empty")
