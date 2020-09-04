#!/usr/bin/env python3

# x = int(input('please enter an integer:'))

# if x < 10:
#     print('less than 10')
# elif x == 10:
#     print('equal 10 ')
# else:
#     print('more than 10')

# nums = [1, 2, 3, 4, 5, 6]

# for n in nums:
#     print(n)

# for i in range(5):
#     print(i)

# for i in range(10):
#     if i % 2 == 0: 
#         continue
#     elif i == 5:
#         break
#     else:
#         print(i, ' is odd number')


# n = 1
# if n == 1:
#     pass
# else:
#     print('complete')

# def fib(n):
#     a, b = 0, 1
#     while b < n:
#         a, b = b, a+b
#         print(a)

# fib(10)

def fib(n = 10):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
        print(a)

fib(5)
fib()