# 1. Дан список чисел. Создать список, в который попадают числа, описываемые возрастающую последовательность. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д. 
# Порядок элементов менять нельзя
# НЕ ПОНЯЛ ЗАДАЧУ. По какому принципу надо выводить последовательности?


# 1.1 Для тех, кто только сейчас видит этот файл, вместо 1 задачи:
# Дан список чисел. Создать список в который попадают числа, описывающие возрастающую последовательность 
# и содержащие максимальное количество элементов. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
#  [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
#  Порядок элементов менять нельзя

# X = [5, 2, 3, 4, 6, 1, 7]
 
# L = []
# M = []
# j = 1
 
# while j < len(X):
#   i = j
#   N = X[:]
#   while i < len(N)-1:
#     if N[i] < N[i+1]: 
#       M.append(N[i])
#       i += 1
#     else:
#       N.pop(i+1)
      
#   j+=1
#   if len(L) < len(M):
#     L = M
#   M=[]
 
# if X[-1] > L[-1]:
#   L.append(X[-1])
  
# if X[0] < L[0]:
#   L.insert(0, X[0])
  
# print(L)
 






# 2. Создать и заполнить файл случайными целыми значениями. Выполнить сортировку содержимого файла по возрастанию. 

# import random as rnd

# file = open('Example.txt', 'a+')
# rnd_list = []
# for i in range (0, 10):
#     file.write(str(rnd.randint(0, 9)))
# file.close()
# file = open('Example.txt', 'r')
# list_int = []
# list_str = str(file.read())
# for i in range(0, len(list_str)):
#     list_int.append(int(list_str[i]))
# file.close()
# print(list_int)
# list_int.sort()
# file = open('Example.txt', 'w+')
# file.write(str(list_int))
# print(list_int)


# 3. Вот вам файл с тысячей чисел. https://cloud.mail.ru/public/DQgN/LqoQzPEec
# Задача: найти триплеты и просто выводить их на экран. Триплетом называются три числа, 
# которые в сумме дают 0. (решение будет долгим, ибо является демонстрационным при теме многопоточного программирования)

# from itertools import combinations

# def find_triplet(some_list, key):
#     def valid(val):
#         return sum(val) == key
#     return list(filter(valid, list(combinations(some_list, 3))))

       

# with open('1Kints.txt', 'r') as file:
#     start_list = []
#     for line in file:
#         start_list.append(int(line))
# print(find_triplet(start_list, 0))    
