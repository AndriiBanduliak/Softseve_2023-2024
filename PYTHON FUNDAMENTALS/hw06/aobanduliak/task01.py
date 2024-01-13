
div_by_2 = []
div_by_3 = []
not_div_by_both = []


for num in range(1, 11):

    if num % 2 == 0:

        div_by_2.append(num)

    if num % 3 == 0:

        div_by_3.append(num)

    if num % 2 != 0 and num % 3 != 0:

        not_div_by_both.append(num)


print("Числа, которые делятся на 2:", div_by_2)
print("Числа, которые делятся на 3:", div_by_3)
print("Числа, которые не делятся на 2 и 3:", not_div_by_both)
