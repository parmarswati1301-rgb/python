#1.
for i in range(1, 11):
    print(i)

#2.
i = 10
while i >= 1:
    print(i)
    i -= 1

#3.
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

#4.
n = int(input("Enter n: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Sum:", total)
