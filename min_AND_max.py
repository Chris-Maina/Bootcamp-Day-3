def find_max_min(listOfNumbers):

	minimum_val = min(listOfNumbers)#gets the minimum value
	maximum_val = max(listOfNumbers)#gets the maximum value
    #creating an empty list and appending max and min values
	max_and_min=[]
	max_and_min.append(minimum_val)
	max_and_min.append(maximum_val)

    #Creating a set to get unique values incase max=min
	unique_max_min = set(max_and_min)
	#creating new list for unique values
	final_max_min = []
	for num in unique_max_min:
		final_max_min.append(num)


	return final_max_min

print(find_max_min([4,4,4]))