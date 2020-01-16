fib = [1,2]
fib_even = [2]
last = 0
while last < 4000000:
    last = fib[-1] + fib[-2]
    fib.append(last)
    if last % 2 == 0 and last < 4000000:
        fib_even.append(last)

print(sum(fib_even))
