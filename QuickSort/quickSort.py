def partition(array, low, high):
    pivot = array[low]
    i = low + 1
    j = high
    
    while True:
        while i <= j and array[j]> pivot:
            j = j - 1

        while i <= j and  (array[i]< pivot):
            i = i + 1

        if i <= j:
            array[i], array[j] = array[j], array[i]
            
        else:
            break
        
    array[low], array[j] = array[j], array[low]
    return j



def quick_sort(arr, low, high):
    if len(arr)==1:
        return arr
    
    if low<high:

        p = partition(arr, low, high)
        quick_sort(arr, low, p-1)
        quick_sort(arr, p+1, high)
    
    
    
arr=[10,5,8,9,15,6,3,12,16]
low=0
high=len(arr)

quick_sort(arr, low, high - 1)
for person in arr:
    print(person)