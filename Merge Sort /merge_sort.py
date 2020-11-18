def merge_list(list1):

	if len(list1)==1:

		return list1
	else:
		# length of list1 dividing by 2 for a create two list and putted same number of elements  from list1
		mid=len(list1)//2
		# using recursive and assigning list in  a left_list and right_list variable by slicing list1 .

		left__list,right_list = merge_list(list1[:mid]),merge_list(list1[mid:])

	# Taking sorted_list as empty list after comparing value between left_list and right_list,lowest values added in sorted_list
	sorted_list = []

	i,j=0,0
	# it will exuated  lenght of left_list and right_list.
	while i<len(left__list) and j<len(right_list):
		# Here comparing value between left_list and right_list
		if left__list[i] > right_list[j]:
			# Lowest value added in sorted_list
			sorted_list.append(right_list[j])
			j+=1
			# j increments for comparing the next value of right_list
		else:
			sorted_list.append(left__list[i])
			i += 1
			# i increments for comparing the next value of left_list

	# added some elemnts in sorted_list who left in list1
	sorted_list+= left__list[i:]
	sorted_list+= right_list[j:]

	return sorted_list                   
list1 = list(map(int,input().split()))
print(merge_list(list1))

