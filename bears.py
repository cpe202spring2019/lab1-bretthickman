def bears(n):
    check = False
    if n == 42:
        return True
    if n < 42:
        return False
    if n % 2 == 0:
        if not check:
            check = bears(n / 2)
    if n % 3 == 0 or n % 4 == 0:
        if not check and ((n // 10**0 % 10) * (n // 10**1 % 10)) == 0:
            return False
        if not check:
            check = bears(n - ((n // 10**0 % 10) * (n // 10**1 % 10)))
    if n % 5 == 0:
        if not check:
            check = bears(n - 42)
    else:
        if check == True:
            return True
        else:
            return False
    return check
