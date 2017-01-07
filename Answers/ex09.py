'''
Exercise 9
Objective: create funtion voter(num); this should return the resultant nominee from a dictionary with the following assignments:
			1: Clinton; 2:Cruz; 3:Sanders; 4: Trump; 5: Kasich; 6: Rubio
			For example: voter(3) should return "Sanders"

(triple apostrophes allow strings to span multiple lines)
'''

def voter(num):
	# Method 1: independently define elements of dictionary
	# candidates_dict = {}
	# candidates[1] = "Clinton"
	# candidates[2] = "Cruz"
	# candidates[3] = "Sanders"
	# candidates[4] = "Trump"
	# candidates[5] = "Kasich"
	# candidates[6] = "Rubio"

	# Method 2: use parallel lists and zip completion of dictionary
	candidate_nums = [1, 2, 3, 4, 5, 6]
	candidate_names = ["Clinton", "Cruz", "Sanders", "Trump", "Kasich", "Rubio"]
	candidates_dict = dict(zip(candidate_nums,candidate_names))

	return candidates_dict[num]

print voter(4)
