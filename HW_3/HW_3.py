# 1. Найти НОК двух чисел
# n1 = int (input("Введите первое число"))
# n2 = int (input("Введите второе число"))
# nok = n1*n2
# res = nok
# while n1<nok and n2<nok:
#     nok-=1
#     if nok%n1 == 0 and nok%n2 == 0:
#         res = nok
# print(res)

# 2. Вычислить число Пи c заданной точностью d
#    Пример: при d = 0.001,  c= 3.141. 


# import math
# from decimal import Decimal
# a = input("Введите точность вывода числа ПИ ")
# nums = list(range(1,10000000))
# summ = 0
# for i in nums:
#     summ = summ + 1/(i**2)
# n =Decimal(math.sqrt(6*summ)).quantize(Decimal(a))
# print(n)

#2.1 Вычислить число Пи c заданной точностью d
# import math
# from decimal import Decimal
# d = input("Введите точность вывода числа ПИ ")
# p = Decimal((math.pi)).quantize(Decimal(d))
# print(p)

# 3. Составить список простых множителей натурального числа N

# n = int(input("Введите натуральное число"))
# nums = []
# for i in range(1, n+1):
#     if n%i == 0:
#         k = 0
#         for j in range(2, i//2+1):
#             if i%j == 0:
#                 k+=1
#         if k<=0:
#             nums.append(i)
# print(nums)

# 4. Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
#    Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]
# nums = [1, 2, 3, 5, 1, 5, 3, 10]
# nums_modify = []
# for i in nums:
#     if i not in nums_modify:
#         nums_modify.append(i)
# print(nums_modify)

# 4.1 Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
#    Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

# nums = [1, 2, 3, 5, 1, 5, 3, 10]
# nums_modify = list(set(nums))
# print(nums_modify)



# + на тему файловой системы:
# 5.  Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа. 

# date = open('text.text', 'r+')
# n = str(date.read())
# n_res = ""
# for i in range(0, len(n)+1):
#     if int(i)%2 == 0:
#        n_res = n_res + n[i]
# date.truncate(0)
# date.close()
# date = open('text.text', 'r+')
# date.write(n_res)
# date.close()
