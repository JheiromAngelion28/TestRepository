total = 0
for i in range(1, 6):
    total += i
print("Sum:", total)

n = int(input("Enter the number of Fibonacci terms: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()