# Python program for implementation of MergeSort
def mergeSort(arr):
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid]
 
        # into 2 halves
        R = arr[mid:]
 
        # Sorting the first half
        mergeSort(L)
 
        # Sorting the second half
        mergeSort(R)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            
        return(arr)
            
print(mergeSort([1,2,3,4,43,2,1,1,4,6,78,9,0,99]))

print("hi")
def find(k, sort_lst):
    count = 0

    for index in range(len(sort_lst)-1):
       
        if sort_lst[index] < sort_lst[index+1]:
            count += 1
            if count == k:
                return sort_lst[index]
            

arr = mergeSort([1,2,3,4,43,2,1,1,4,6,78,9,0,99])
print(find(4, arr))










