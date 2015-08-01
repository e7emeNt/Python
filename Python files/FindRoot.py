def findRoot(x, power, epsilon):
    if x < 0 and power % 2 == 0:
        return None
        #Can't find even powered root of negative number!!

    low = min(-1, x)
    high = max(1, x)
    ans = (high + low) / 2.0
    while abs(ans**power - x) > epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0
    return ans