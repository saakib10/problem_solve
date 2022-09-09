def get_aspected_index(two_pair_values, target_value):
    result = []
    list_length = len(two_pair_values)
    for pair in range(list_length):
        if type(two_pair_values[pair]) == list:
            pair_sum = sum(two_pair_values[pair])
            if target_value == pair_sum:
                result.append(pair)
    return result

two_pair_values = [
[1, 5],
[9, -7],
[0, 8],
[6, 3],
[4, 11],
[14, 0],
[8, 1],
[4, 9]
]
target_value = 9
result = get_aspected_index(two_pair_values, target_value)
print(result)