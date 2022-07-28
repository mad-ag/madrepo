#largest sum contiguos subarray
def sub(arr):
    maxs=arr[0]
    maxe=arr[0]
    for i in range(1,len(arr)):
        maxe=max(arr[i],maxe+arr[i])
        maxs=max(maxs,maxe)
    return(maxs)
arr=[-1,5,-2,3,-4]
print(sub(arr))
