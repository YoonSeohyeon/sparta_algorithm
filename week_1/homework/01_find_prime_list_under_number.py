prime_num = 0
input = 20
num_count = []
def find_prime_list_under_number(number):
    for num_1 in range(2,number+1):
        for num_2 in range(2,num_1):                #이부분 이해를 잘못해서 오래걸림
            if num_1%num_2 == 0:
                break                               #break 응용 부족
        else:
            num_count.append(num_1)


    return num_count

result = find_prime_list_under_number(input)
print(result)
