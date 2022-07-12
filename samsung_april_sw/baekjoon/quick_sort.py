def quick_sort(my_array):
    if len(my_array) <= 1:
        return my_array
    pivot = len(my_array)//2
    left_array, equal_array, right_array = [], [], []
    for num in my_array:
        if num < my_array[pivot]:
            left_array.append(num)
        elif num > my_array[pivot]:
            right_array.append(num)
        else:
            equal_array.append(num)
    return quick_sort(left_array) + equal_array + quick_sort(right_array)

a = [1, 4, 6, 2, -3, 5,8,9,9,103,1]

print(quick_sort(a))