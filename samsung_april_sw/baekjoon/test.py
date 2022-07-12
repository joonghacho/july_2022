# def rotate_90(my_array):
#     temp = zip(*my_array[::-1])
#     new_array = [list(ele) for ele in temp]
#     return new_array
# def ruota_antiorario(matrix):
#    ruota=list(zip(*reversed(matrix)))
#    return[list(elemento) for elemento in ruota]
# def ruota_orario(matrix):
#    ruota=list(zip(*reversed(matrix)))
#    return[list(elemento)[::-1] for elemento in ruota][::-1]

# my_array = [[1,2,3],[4,5,6],[7,8,9]]

# for i in my_array:
#     print(i)
# my_array = ruota_orario(my_array)
# for j in my_array:
#     print(j)
# import sys

# one_gear = (sys.stdin.readline())
# # print(one_gear)
# import itertools

# iterables = [ [1,2,3,4], [88,99], ['a','b'] ]

# answer = []
# candidate = list(itertools.product(*iterables))

# # print(candidate)

# def rotate(box):
#     element = box.pop()
#     new_box = list(element) + box
#     return new_box

# def rotate(box):
#     element = box.pop()
#     k = [element]
#     return k + box
a = ["a","b","c"]
a = a[-1] + a[:-1]
print(a)