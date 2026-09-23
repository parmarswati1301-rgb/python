#11.
def maximum(a, b, c):
    if a > b and a > c:
        print("Maximum =", a)
    elif b > a and b > c:
        print("Maximum =", b)
    else:
        print("Maximum =", c)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
maximum(a, b, c)

#12.
def count_vowels(string):
    count = 0
    for ch in string:
        if ch in "aeiouAEIOU":
            count = count + 1
    print("Number of vowels =", count)

string = input("Enter a string: ")
count_vowels(string)

#13.
def reverse_string(string):
    reverse = string[::-1]
    print("Reversed string =", reverse)
string = input("Enter a string: ")
reverse_string(string)

#14.
def check_palindrome(string):
    reverse = string[::-1]
    if string == reverse:
        print("Palindrome")
    else:
        print("Not Palindrome")

string = input("Enter a string: ")
check_palindrome(string)

#15.
def list_sum(numbers):
    total = 0
    for num in numbers:
        total = total + num
    print("Sum =", total)
numbers = [10, 20, 30, 40, 50]
list_sum(numbers)

#16.
def largest(numbers):
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    print("Largest element =", maximum)
numbers = [10, 25, 8, 40, 15]
largest(numbers)

#17.
def remove_duplicates(numbers):
    result = []
    for num in numbers:
        if num not in result:
            result.append(num)
    print("List without duplicates =", result)

numbers = [10, 20, 10, 30, 20, 40]
remove_duplicates(numbers)


#18.
def count_element(numbers, element):
    count = 0
    for num in numbers:
        if num == element:
            count = count + 1
    print("Element appears", count, "times")
numbers = [10, 20, 10, 30, 10, 40]
element = int(input("Enter element: "))
count_element(numbers, element)

#19.
def check_prime(num):
    if num < 2:
        print("Not Prime")
    else:
        for i in range(2, num):
            if num % i == 0:
                print("Not Prime")
                break
        else:
            print("Prime")
num = int(input("Enter a number: "))
check_prime(num)

#20.
def prime_numbers(start, end):
    primes = []
    for num in range(start, end + 1):
        if num >= 2:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print("Prime numbers =", prime_numbers(start, end))


#21.
def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
n = int(input("Enter number of terms: "))
fibonacci(n)

#22.
def second_largest(numbers):
    largest = numbers[0]
    second = numbers[0]
    for num in numbers:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    print("Second largest =", second)
numbers = [10, 25, 8, 40, 30]
second_largest(numbers)

#23.
def sort_list(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    print("Sorted list =", numbers)

numbers = [40, 10, 30, 20, 50]
sort_list(numbers)

#24.
def merge_lists(list1, list2):
    result = list1 + list2
    unique = []
    for num in result:
        if num not in unique:
            unique.append(num)

    print("Merged list without duplicates =", unique)
list1 = [10, 20, 30]
list2 = [20, 30, 40, 50]
merge_lists(list1, list2)


#25.
def are_ana(str1,str2):
    return sorted(str1)==sorted(str2)
print(are_ana("listen","silent"))
print(are_ana("hello","world"))
print()




