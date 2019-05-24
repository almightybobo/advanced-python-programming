def divisible_numbers(a_list, a_list_of_terms):
    return [a for a in a_list if all([a % term == 0 for term in a_list_of_terms])]
    # other answer
    # return [x for x in a_list if len([1 for term in terms if x % term == 0]) == len(terms)]

if __name__ == '__main__':
    print(divisible_numbers([12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [2, 3])) # [12, 6]
