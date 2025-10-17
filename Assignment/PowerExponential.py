def power_bruteforce (x, n) :
    result = 1
    for _ in range(n) :
        result *= x
    return result

def power_iterative (x,n) :
    result = 1
    power = abs(n)

    while power >0:
        if power % 2 == 1 :
            result *=x
        x *= x
        power //=2

    return result if n >=0 else 1/result

if __name__ == "__main__" :
    print(power_bruteforce(2, 10))  # 1024
    print(power_iterative(2, 10))   # 1024
    print(power_iterative(2, -3))   # 0.125
    print(power_iterative(3, 5))    # 243
