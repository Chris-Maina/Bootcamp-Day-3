#program to count the number of words in a string
def words(word_string):
	#initialize empty list
	word_list = [] 

	#remove tabs
	word_string = word_string.replace('\t','')
	#remove new lines
	word_string = word_string.replace('\n','')

	#coverts into a list
	word_list = word_string.split()

	#Taking care of extra spaces
	if(word_list.count('')>0):
		for item in range (0,word_list.count('')):
			word_list.remove('')

	
    #using comprehension to get a dictionary
	word_dict={word:word_list.count(word) for word in word_list}


	return word_dict

print(words('testing 1 2 testing'))



	  


