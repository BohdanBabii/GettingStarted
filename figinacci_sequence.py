
def compute_fibonacci(n: int) -> int:
    n0 = 0
    n1 = 1
    n_temp = 1
    for _ in range(1,n):
        n_temp = n1
        n1 += n0
        n0 = n_temp

    return n

n = int(input())
print(compute_fibonacci(n=n))





