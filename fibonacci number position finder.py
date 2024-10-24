user_input = 6
if user_input > 0:
    int_to_list = list((1, 1))
for x in range(user_input):
    int_to_list.append(int_to_list[x] + int_to_list[x+1])

print(int_to_list[user_input-1])


