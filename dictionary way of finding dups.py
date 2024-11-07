def CountCharInStr(string):
    dictionary = dict(())
    for character in string:
        if character not in dictionary:
            dictionary[character] = 1

        else:
            dictionary[character] += 1
    return dictionary


    
def TellUserNoOfDups(the_dict):
    list_of_dups = []
    for key in the_dict:
        if the_dict[key] > 1:
            list_of_dups.append(key)
    
    return list_of_dups



input_to_dictionary = CountCharInStr(input("What do you want to input:\n"))
list_of_duplicate_char = TellUserNoOfDups(input_to_dictionary)
print(list_of_duplicate_char)