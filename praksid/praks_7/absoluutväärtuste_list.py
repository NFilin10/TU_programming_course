
def abs_list(abs_list):
    tulemus = []
    for i in range(len(abs_list)):
        if abs_list[i] > 0:
            tulemus.append(abs_list[i])
        else:
            tulemus.append(-abs_list[i])
    return tulemus
        

print(abs_list([1, -2, 3, -4, 5, -6]))