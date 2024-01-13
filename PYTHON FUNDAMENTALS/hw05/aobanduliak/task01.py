def create_float_list(integer_list):

    float_list = []
    for integer in integer_list:
        float_list.append(float(integer))
    return float_list

# E.g:


integer_list = [1, 2, 3, 4, 5]
float_list = create_float_list(integer_list)

print(float_list)
