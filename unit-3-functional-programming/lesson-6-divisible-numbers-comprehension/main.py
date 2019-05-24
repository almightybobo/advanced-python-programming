def divisible_numbers(a_list, term):
    return [a_list[i] for i in range(len(a_list)) if i % term ==  0]


if __name__ == '__main__':
    print(divisible_numbers([9, 8, 7, 6, 5, 4, 3, 2, 1], 3)) # [9, 6, 3]
