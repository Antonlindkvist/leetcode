def addDigits(num: int) -> int:
    if num == 0:
        return 0
    return 1 + (num - 1) % 9


print(addDigits(39))
