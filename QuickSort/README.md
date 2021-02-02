# QuickSort

QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways.

- Always pick first element as pivot.(implemented above)
- Always pick last element as pivot
- Pick a random element as pivot.
- Pick median as pivot.

It has two functions:
### Partition:
The function selects the first element as pivot element, places that pivot element correctly in the array in such a way that all the elements to the left of the pivot are lesser than the pivot and all the elements to the right of pivot are greater than it.

*Parameters: array, starting index and ending index*

*Returns: index of pivot element after placing it correctly in sorted array*

### Quicksort:


*Parameters: array, starting index and ending index*

## Time Complexity:

- ##### Worst Case Complexity [Big-O]: O(n2):
It occurs when the pivot element picked is either the greatest or the smallest element.
This condition leads to the case in which the pivot element lies in an extreme end of the sorted array. One sub-array is always empty and another sub-array contains n - 1 elements. Thus, quicksort is called only on this sub-array.
However, the quick sort algorithm has better performance for scattered pivots.

- ##### Best Case Complexity [Big-omega]: O(n*log n):
It occurs when the pivot element is always the middle element or near to the middle element.

- ##### Average Case Complexity [Big-theta]: O(n*log n):
It occurs when the above conditions do not occur.
Space Complexity

##### *The space complexity for quicksort is O(log n).*

### Implementation of Quick Sort
![](quicksort.png)
