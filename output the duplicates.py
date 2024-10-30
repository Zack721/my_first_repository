def AppendCharToList():
    list_of_characters = []
    user_input = input("What is your input?")
    for character in user_input:
        list_of_characters.append(character)
    
    list_of_characters = IsThereDuplicate(list_of_characters)
    return list_of_characters

def IsThereDuplicate(list):
    which_have_dups = []
    for i in list:
        if list.count(i)>= 2 and i not in which_have_dups:
            which_have_dups.append(i)
    return which_have_dups
        


dictionary_of_dups = dict(duplicates = AppendCharToList())
print(dictionary_of_dups)




