def to_fahrenheit(a_list):
    return [(lambda a: 9 * a / 5 + 32)(a) for a in a_list]


if __name__ == '__main__':
    print(to_fahrenheit([0, 10, 25, 30, 100])) # [32.0, 50.0, 77.0, 86.0, 212.0]
