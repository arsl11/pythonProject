def sum_two_smallest_number(array):
    # m1 = 1000000
    # m2 = 1000000
    # for number in array:
    #     if number <= m1:
    #         m1, m2 = number, m1
    #     elif number < m2:
    #         m2 = number
    # return m1 + m2
    return sum(sorted(array)[:2])

array = [19, 5, 42, 2, 77]
print(sum_two_smallest_number(array))