def fib(n):
    table = [0]*(n + 1)
    table[1] = 1
    for i in range(2, n+1):
        table[i] = table[i - 1] + table[i - 2]
    return table[n]


x = int(input('Enter the integer'))
print(fib(x))