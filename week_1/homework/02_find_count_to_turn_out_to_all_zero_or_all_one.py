input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    turn_zero_num = 0
    turn_one_num = 0

    if string[0] == '0':
        turn_one_num += 1
    elif string[0] == '1':
        turn_zero_num +=1

    for i in range(len(string)-1):
        if string[i] != string[i+1]:
            if string[i + 1] == '0':
                turn_one_num +=1
            if string[i + 1] == '1':
                turn_zero_num +=1
    return min(turn_one_num,turn_zero_num)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)