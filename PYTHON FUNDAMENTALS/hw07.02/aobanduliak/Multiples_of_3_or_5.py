def solution(number):
    if number < 0:
        return 0
    else:
        return sum(i for i in range(number) if i % 3 == 0 or i % 5 == 0)
