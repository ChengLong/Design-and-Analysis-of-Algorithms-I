'''
The file contains all of the integers between 1 and 10,000 (inclusive) in unsorted order (with no integer repeated). The integer in the ith row of the file gives you the ith entry of an input array.

Your task is to compute the total number of comparisons used to sort the given input file by QuickSort. As you know, the number of comparisons depends on which elements are chosen as pivots, so we'll ask you to explore three different pivoting rules.
You should not count comparisons one-by-one. Rather, when there is a recursive call on a subarray of length m, you should simply add m-1 to your running total of comparisons. (This is because the pivot element will be compared to each of the other m-1 elements in the subarray in this recursive call.)

WARNING: The Partition subroutine can be implemented in several different ways, and different implementations can give you differing numbers of comparisons. For this problem, you should implement the Partition subroutine as it is described in the video lectures (otherwise you might get the wrong answer). 

Three different ways to choose the pivot: first, last, median of first, middle, and last
'''

# get input numbers
f=open('QuickSort.txt')
nums = map(int, f.readlines())
f.close()

def quick_sort(array, s, e, pivot):
#Return the number of comparisions done during sorting
#the function will sort the array starting from index s and ending at e, both inclusive. 
	if s >= e:
		return 0
	choose_pivot(array, s, e, pivot)
	p_index = partition(array, s, e)
	small = quick_sort(array, s, p_index - 1, pivot)
	large = quick_sort(array, p_index+1, e, pivot)
	return (e-s) + small + large

def choose_pivot(a, s, e, pivot):
#No return value
#this function chooses pivot depending on the pivot argument and swaps it with the first element in the array
	# no work need to be done for pivot == 'first'
	if pivot == 'last':
		a[s], a[e] = a[e], a[s]
	elif pivot == 'median' : 
		m_index = (e - s)/2 + s
		if (a[m_index] - a[s]) * (a[m_index] - a[e]) < 0: # a[m_index] is the median
			a[m_index], a[s] = a[s], a[m_index]
		elif (a[e] - a[s]) * (a[e] - a[m_index]) < 0: #a[e] is the median 
			a[e], a[s] = a[s], a[e]

def partition(a, s, e):
#partition the array around the pivot, which is at first position.
	first_large, first_unseen = s+1, s+1
	pivot = a[s]
	while first_unseen <= e:
		if a[first_unseen] < pivot:
			#swap first large with it
			a[first_large], a[first_unseen] = a[first_unseen], a[first_large]
			first_large += 1
		first_unseen += 1
	#swap pivot with the last small
	a[s], a[first_large-1] = a[first_large-1], a[s]
	return first_large-1

comparisons = quick_sort(nums, 0, len(nums) - 1, 'median')
print comparisons 
