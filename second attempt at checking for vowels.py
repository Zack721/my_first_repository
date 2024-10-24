VOWELS = {"a", "e", "i", "o", "u"}    #O(1)
def StringToSet(str):                #O(1)
    unique_letters = set(())          #O(1)
    for i in str:             #O(n)
        unique_letters.add(i)         #O(1)
    
    return unique_letters             #O(1)

#################is vowel in set function##########
def ParseInputVowels(input_letters):         #O(1)
    input_vowels = set(())             #O(1)
    for i in VOWELS:                 #O(n)
        if i in input_letters:       #O(n)
            input_vowels.add(i)      #O(1)
    return input_vowels              #O(1)

##############output to the user of what vowels are in the users input####
def PrintResults(present_vowels, original_input):    #O(1)
    print(f"The vowel {present_vowels} is in {original_input}")    #O(1)

    if len(present_vowels)  != len(VOWELS):      #O(1)
        print(f"The vowel {VOWELS.difference(present_vowels)} is not in {original_input}")   #O(1)

input_from_user = input("What word would you like to input:")   #O(1)
unique_letters = StringToSet(input_from_user.lower())     #O(1)
list_of_present_vowels = ParseInputVowels(unique_letters)   #O(1)




PrintResults(list_of_present_vowels, input_from_user)        #O(1)
