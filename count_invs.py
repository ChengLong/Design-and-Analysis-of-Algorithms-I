"""The file contains all the 100,000 integers between 1 and 100,000 (including both) in some random order( no integer is repeated).
Your task is to find the number of inversions in the file given (every row has a single integer between 1 and 100,000). Assume your array is from 1 to 100,000 and ith row of the file gives you the ith entry of the array.
Write a program and run over the file given. The numeric answer should be written in the space.
So if your answer is 1198233847, then just type 1198233847 in the space provided without any space / commas / any other punctuation marks. You can make upto 5 attempts, and we'll count the best one for grading.
"""

def sort_and_count(array):
    """Returns the sorted array and the number of inversions"""
    length = len(array)
    if length <=1:
        return (array, 0)
    (left, count_left) = sort_and_count(array[:length/2])
    (right, count_right) = sort_and_count(array[length/2:])
    (merged, count_split) = merge_and_count_split(left, right)
    return (merged , count_left+count_right+count_split)

def merge_and_count_split(left, right):
    """Returns a merged array of two sorted subarrays and the number of
    inversions spanning from left part to right part"""
    merged = []
    total, i, j = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            total += len(left) - i
    if i < len(left):
        merged.extend(left[i:])
    else:
        merged.extend(right[j:])
    return (merged, total)

f = open('IntegerArray.txt', 'r')
nums = map(int, f.readlines())
f.close()

(sorted, inverions) = sort_and_count(nums)
print inverions
