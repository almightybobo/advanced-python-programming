def even_numbers(a_list):
    return [a for a in a_list if a % 2 == 0]


if __name__ == '__main__':
    print(even_numbers([5, 4, 3, 2, 1])) # [4, 2]
