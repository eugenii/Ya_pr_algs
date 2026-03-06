# K Сортировка слиянием.

def merge(arr, lf, mid, rg):
	# Your code
	# “ヽ(´▽｀)ノ”
    result = merge_sort(arr[:mid], lf, mid) + merge_sort(arr[mid:], mid, rg)
    return result


def merge_sort(arr, lf, rg):
	# Your code
	# “ヽ(´▽｀)ノ”
	if len(arr) != 1:
		mid = len(arr) // 2
		left = merge_sort(arr[:mid], lf, mid)
		right = merge_sort(arr[mid:], mid, rg)
		merge(arr, left, mid, right)

def test():
	a = [1, 4, 9, 2, 10, 11]
	b = merge(a, 0, 3, 6)
	expected = [1, 2, 4, 9, 10, 11]
	assert b == expected
	c = [1, 4, 2, 10, 1, 2]
	merge_sort(c, 0, 6)
	expected = [1, 1, 2, 2, 4, 10]
	assert c == expected

if __name__ == '__main__':
    test()