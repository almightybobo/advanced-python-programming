def remove_duplicates_in_order(a_list):
    if a_list == []:
        return []

    result = [a_list[0]]
    for index in range(1, len(a_list)):
        elem = a_list[index]
        if elem not in result:
            result.append(elem)

    return result


if __name__ == '__main__':
    print(remove_duplicates_in_order([2, 1, 1, 3, 4])) # [2, 1, 3, 4]
    print(remove_duplicates_in_order([])) # []
