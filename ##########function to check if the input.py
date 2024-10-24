##########function to check if the input is all alphabetical letters#########
def IsInputAlphaNumerical(user_input):                  #O(1)
    while user_input.isalnum() == False:               #O(n)
        user_input = input("What word would you like to input:")       #O(1)
        
#################is vowel in set function##########
def IsvowelInSet(vowel_to_find, the_set, the_list, not_present):       #O(1)
    if vowel_to_find in the_set:               #O(n)
        the_list.append(vowel_to_find)         #O(1)

    elif vowel_to_find not in the_set:         #O(n)
        not_present.append(vowel_to_find)      #O(1)
        #not sure if i can use "not" like that and i dont know why it wont append

#################output to the user of what vowels are in the users input####
def VowelIsInSet(present_vowels, original_input, not_present_vowels):     #O(1)
    for i in present_vowels:                                              #O(n)
        print(f"The vowel {i} is in {original_input}")                    #O(1)

    for x in not_present_vowels:                                          #O(n)
        print(f"The vowel {x} is not in {original_input}")                #O(1)



input_from_user = input("What word would you like to input:")             #O(1)
IsInputAlphaNumerical(input_from_user)                                    #O(1)
lowercase_input = input_from_user.lower()                                 #O(1)
set_of_the_values = set(())                                               #O(1)
list_of_present_vowels = []                                               #O(1)
not_in_input = []                                                         #O(1)

for i in lowercase_input:                                                 #O(n)
    set_of_the_values.add(i)                                              #O(1)

for vowels in ["a", "e", "i", "o", "u"]:                                  #O(n)
    IsvowelInSet(vowels, set_of_the_values, list_of_present_vowels, not_in_input)       #O(1)

VowelIsInSet(list_of_present_vowels, input_from_user, not_in_input)        #O(1)