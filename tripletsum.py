def find_triplets(arr,target_sum):
    triplets=[]
    arr.sort()
    for i in range(len(arr)-2):
        left=i+1
        right=len(arr)-1
        while left<right:
            current_sum=arr[i]+arr[left]+arr[right]
            if current_sum==target_sum:
                triplets.append([arr[i],arr[left],arr[right])
                left+=1
                right-=1
