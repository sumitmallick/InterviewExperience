# Pattern:
# 4444444
# 4333334
# 4322234
# 4321234
# 4322234
# 4333334
# 4444444

def print_square_pattern(n):
    size = 2*n -1
    for i in range(size):
        for j in range(size):
            min_val = min(i, j, size-1-i, size-1-j)
            if min_val == 0:
                print(n, end = '')
            else:
                print(n - min_val, end = '')
        print()

print_square_pattern(4)