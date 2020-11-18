def bubble_sort(sort_list):
	len_bubble_sort = len(sort_list)
	for i in range(len_bubble_sort-1):
		for j in range(len_bubble_sort-i-1):
			if sort_list[j] > sort_list[j+1]:
				sort_list[j],sort_list[j+1] = sort_list[j+1],sort_list[j]

				j-=1
	return sort_list

list1 = list(map(int,input().split()))
print(bubble_sort(list1))