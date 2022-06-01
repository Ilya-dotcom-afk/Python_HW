#1. Найти сумму чисел списка стоящих на нечетной позиции Пример:[1,2,3,4] -> 4

# n = int(input ("Введите колличество элементов ряда"))
# numbers = list(range(1, n+1))
# print(numbers)
# sum = 0
# i=0
# while i<n:
#     if i == 0 or i%2 == 0:
#         sum+=numbers[i]
#     print(f"индекс: {i} значение {numbers[i]}")
#     i+=1
# print(sum)





# 2. Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
#    Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 

# import math
# n = int(input ("Введите колличество элементов ряда"))
# numbers = list(range(1, n+1))
# numbers_modify = [0]*math.ceil(n/2)
# print(numbers)
# min = 0
# max = n-1
# while min <= max:
#     print(numbers[min])
#     print(numbers[max])
#     numbers_modify[min] = numbers[min]*numbers[max]
#     print(numbers_modify[min])
#     min+=1
#     max-=1
# print(numbers_modify)



# 3. В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов. 
#    Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19 (здесь минимальное - 0, максимальное - 0,2?)

# from decimal import Decimal

# nums = [1.1, 1.2, 3.1, 5, 10.01]
# nums_modify = [0]*len(nums)
# a=0
# for i in nums:
#     nums_modify[a] = Decimal(i-i//1).quantize(Decimal("1.00"))
#     a+=1
# print(max(nums_modify) - (min(nums_modify)))







# 3.1 В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов
#  (отличное от нуля). 
#    Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19 

# from decimal import Decimal
# nums = [1.1, 1.2, 3.1, 5, 10.01]
# nums_modify = [0]*len(nums)
# a=0
# for i in nums:
#      nums_modify[a] = Decimal(i-i//1).quantize(Decimal("1.00"))
#      a+=1
# k = 0
# min = 1
# max = nums_modify[k]
# while k<len(nums_modify):
#     if nums_modify[k]<min and nums_modify[k] !=0:
#         min = nums_modify[k]
#     elif nums_modify[k]>max and nums_modify[k] !=0:
#         max = nums_modify[k]
#     k+=1
# print(min)
# print(max)
# print(max-min)




# 4. Написать программу преобразования десятичного числа в двоичное

# n = int(input("Введите десятичное число"))
# b = bin(n)
# print(b)
