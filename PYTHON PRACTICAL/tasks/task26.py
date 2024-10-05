class MyExceptions(Exception):
    pass


def sum_slice_array(arr, first, second):
    try:
        flag1 = False
        if (isinstance(first, int)) and (isinstance(second, int)):
            flag1 = True
        if flag1 and first >= 1 and second >= 1:
            flag1 = True
        else:
            flag1 = False

        flag2 = False
        if all(isinstance(item, int) for item in arr):
            flag2 = True

        flag3 = False
        if len(arr) > first-1 and len(arr) > second-1:
            flag3 = True
        res_list = [flag1, flag2, flag3]
        if not all(res_list):
            raise MyExceptions('MyExceptions')
    except MyExceptions as e:
        return e
    else:
        num1 = arr[first - 1]
        num2 = arr[second - 1]
        res = float(num1 + num2)
        return res
