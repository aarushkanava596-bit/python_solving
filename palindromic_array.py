def isPalinArray(arr):
    for x in arr:
        n, rev = x, 0
        while n > 0:
            rev = rev * 10 + n % 10
            n //= 10
        if rev != x:
            return False
    return True
