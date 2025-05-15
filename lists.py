# Replace the "ANSWER HERE" with your answer

def remove_elements(list_to_remove_elements):
	largo = len(list_to_remove_elements) 
	if largo < 1:
		list_to_remove_elements = []
	elif largo < 5:
		del list_to_remove_elements[0]
	elif largo < 6:
		del list_to_remove_elements[4]
		del list_to_remove_elements[0]
	else:
		del list_to_remove_elements[5]
		del list_to_remove_elements[4]
		del list_to_remove_elements[0]
	return list_to_remove_elements

def add_elements(list_to_add_elements):
	if len(list_to_add_elements) == 0:
		list_to_add_elements = ['Pink', 'Yellow']
	else:
		list_to_add_elements.insert(0,"Pink")
		list_to_add_elements.append("Yellow")
	return list_to_add_elements

def is_empty(list_to_check):
	tamaño = len(list_to_check)
	return tamaño == 0
    
def check_lists(list_to_compare1, list_to_compare2):
	l1 = len(list_to_compare1)
	l2 = len(list_to_compare2)
	return (l1 >=3) and (l2 >= 3) and (list_to_compare1[2] == list_to_compare2[2])


def list_of_lists(list_of_lists_to_modify):
	list1 = list_of_lists_to_modify[0]
	list2 = list_of_lists_to_modify[1]
	list3 = list_of_lists_to_modify[2]
	new_list = []
	len1 = len(list1)
	len2 = len(list2)
	len3 = len(list3)
	if len1 == 0:
		new_list1 = []
	elif len1 == 1:
		new_list1 = [list1[0]]
	elif len1 > 1:
		new_list1 = [list1[0], list1[1]]
	
	if len2 < 2:
		new_list2 = []
	elif len2 == 2:
		new_list2 = [list2[1]]
	elif len2 == 3:
		new_list2 = [list2[1],list2[2]]
	elif len2 > 3:
		new_list2 = [list2[1],list2[2],list2[3]]

	if len3 == 0:
		new_list3 = []
	elif len3 == 1:
		new_list3 = [list3[-1]]
	elif len3 > 1:
		new_list3 = [list3[-2],list3[-1]]

	return [new_list1, new_list2, new_list3]
