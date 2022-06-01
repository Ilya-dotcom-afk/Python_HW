# #Сформировать список из N членов последовательности. Для N = 5: 1, -3, 9, -27, 81 и т.д.
# N = int(input("Введите колличество элементов списка"))
# numbers = list(range(1, N+1))
# i = 1
# while i< N:
#     numbers[i] = numbers[i-1]*-3
#     i+=1
# print(numbers)


# #Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 
# #3n + 1. Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
# n = int(input("Введите количество элементов последовательности"))
# number = {}
# #k = 1
# for i in range(n):
#     number[i+1] = 3*(i+1)+1
# #    number[k] = 3*k+1
# #    k+=1
# print(number)



# #Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.
# from itertools import count


# str1 = input("Введите анализируемую строку ")
# subStr1 = input("Введите вхождение ")

# def CountStr (s, ss):
#     num = 0
#     i = -1
#     while True:
#         i = s.find(ss, i+1)
#         if i == -1:
#             return num
#         num +=1

# print(CountStr(str1, subStr1))




# #Подсчитать сумму цифр в вещественном числе.

# n = input("Введите вещественное число")
# s = 0
# N = int(n.replace(".", "0"))
# while N>=10:
#     s+=N%10
#     N = (N-N%10)/10
# s+=N
# print (s)


# #Написать программу получающую набор произведений чисел от 1 до N. Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]
# import math

# n = int (input("Введите количество элементов в списке"))
# numbers = list(range(1, n+1))
# for i in numbers:
#     numbers[i-1] = math.factorial(numbers[i-1])
# print(numbers)








