first_list = [1, 2, 3, 4, 5]
second_list = [3, 5, 9, 12, 18]
flag = False
for i in first_list:
    for b in second_list:
        if i == b:
            flag = True
    if not flag:
        print(i)
    flag = False
