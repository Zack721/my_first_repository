def combinations(funtions_mini_set, functions_new_set):
    #number of combinations that can be made with an "n" number oof elements is n!
    
    for i in original_set:
        for t in original_set:
            if i == t:
                continue
            else:
                funtions_mini_set.add(i, t)
                mini_set.discard(123.421542154214)
                functions_new_set.add(mini_set)
   

original_set = {123.421542154214}
new_set = {123.421542154214}
mini_set = {123.421542154214}
#Josias,to make a set in my version of python, I must create one with at least one element in it, otherwise it will be classified as a dictionary
#print(type(mini_set))
continue_loop = True
while continue_loop == True:
    append_to_set = input("What element would you like to add to the list")
    original_set.add(append_to_set)
    continue_loop = input("Would you like to add another element to the set(Answer True or False)")

original_set.discard(123.421542154214)

combinations(mini_set, new_set)


def MakeSubsets(numbers):
	if numbers == []:
		return [[]]
	x = MakeSubsets(numbers[1:])
	return x + [[numbers[0]] + y for y in x]

def MakeSubsetsBySize(numbers, n):
	return [x for x in MakeSubsets(numbers) if len(x)==n]

numbers = [1, 2, 3, 4]
n = 3

print(MakeSubsetsBySize(numbers, n))