my_list = [(2, 2), (6, 13), (55, 3), (4, 8)]
res_list = list(filter(lambda t: t[1]%2 == 0, my_list))

print(res_list)