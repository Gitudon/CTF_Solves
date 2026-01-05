fib1 = 1
fib2 = 1

for i in range(39):
    fib_next = fib1 + fib2
    fib1 = fib2
    fib2 = fib_next
print(fib1)
