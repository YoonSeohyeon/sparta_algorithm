numbers = [1, 1, 1, 1, 1]
target_number = 3


def dfs(array, target, cur):
    if len(array) == 0 and cur != target:
        return 0

    if len(array) == 0 and cur == target:
        return 1

    ret = 0

    plus, minus = cur, cur

    plus += array[0]
    minus -= array[0]

    ret += dfs(array[1:], target, plus)
    ret += dfs(array[1:], target, minus)

    return ret


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    answer = dfs(array, target, 0)
    return answer



print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!