# def fn(n) :
#     if n == 1:
#         return 1
#     s = n + fn(n-1)
#     return s

# f1 = fn(3)
# print(f1)

def fn(n) :
    if n == 1:
        return 1
    s = n + fn(n-1) +n
    return s

f1 = fn(3)
print(f1)