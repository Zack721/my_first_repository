def combinations(funtions_mini_set, functions_new_set):
    #number of combinations that can be made with an "n" number oof elements is n!
    for i in original_set:
        for t in original_set:
            if i == t:
                continue
            else:
                funtions_mini_set.add(i, t)
                functions_new_set.add(mini_set)
    



new_set = {}
mini_set = {}
print(type(mini_set))
continue_loop = True
while continue_loop == True:
    original_set = {1, 2, 3}
    append_to_set = input("What element would you like to add to the list")
    continue_loop = input("Would you like to add another element to the set(Answer True or False)")

combinations(mini_set, new_set)

