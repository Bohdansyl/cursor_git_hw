nt_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}
# 1
print(id(nt_a))
print(id(str_b))
print(id(set_c))
print(id(lst_d))
print(id(dict_e))


# 2
def my_func():
    lst_d.append(4)
    lst_d.append(5)


my_func()

print(lst_d)
print(id(lst_d))
# 3
print(type(nt_a))
print(type(str_b))
print(type(set_c))
print(type(lst_d))
print(type(dict_e))
# 4
print(isinstance(nt_a, int))
print(isinstance(str_b, str))
print(isinstance(set_c, set))
print(isinstance(lst_d, list))
print(isinstance(dict_e, dict))
# 5
a = 5
b = 6
print("Anna has {} apples and {} peaches.".format(a, b))
# 6
print("Anna has {1} apples and {0} peaches.".format(a, b))
# 7
print("Anna has {second} apples and {first} peaches.".format(first=a, second=b))
# 8
print("Anna has {second:5} apples and {first:3} peaches.".format(first=a, second=b))
# 9
print(f"Anna has {a} apples and {b} peaches.")
# 10
print("Anna has %d apples and %d peaches." % (a, b))
# 11
data_dict = {"apples": b, "peaches": a}
print("Anna has %(apples)d apples and %(peaches)d peaches." % data_dict)

# 12
list_comprehension = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(list_comprehension)
# [0, 1, 16, 9, 256, 25, 1296, 49, 4096, 81]
# 13
lst = []
for num in range(10):
    if num % 2 == 0:
        lst.append(num // 2)
    else:
        lst.append(num * 10)
print(lst)

# 14
dc_with_if = {num: num ** 2 for num in range(1, 11) if num % 2 == 1}
print(dc_with_if)

# 15
dc_with_elif = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print(dc_with_elif)
# 16
d = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        d[x] = x ** 3
print(d)

# 17
d = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        d[x] = x ** 3
    else:
        d[x] = x
print(d)

# 18

foo = lambda x, y: x if x < y else y


# 19
def foo(x, y, z):
    if y < x:
        return z
    if x > z:
        return y


# 20
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]

print(sorted(lst_to_sort))
# 21
print(sorted(lst_to_sort, reverse=True))
# 22
new_list = list(map(lambda x: x * 2, lst_to_sort))
print(new_list)
# 23
list_A = [2, 3, 4]
list_B = [5, 6, 7]
list_new = list(map(lambda x, y: x ** y, list_A, list_B))

# 24
import functools


def my_add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")
    return result


functools.reduce(my_add, lst_to_sort)
# 25
new_list = list(filter(lambda x: (x % 2 == 1), lst_to_sort))

print(new_list)

# 26
lst_neg = list(filter(lambda b: b < 0, range(-10, 10)))
print(lst_neg)

list_1 = [1, 2, 3, 5, 7, 9]
list_2 = [2, 3, 5, 6, 7, 8]
# 27
list_3 = list(filter(lambda x: x in list_1, list_2))
print(list_3)
