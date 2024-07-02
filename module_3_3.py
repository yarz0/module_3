def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

values_list = [1, 'stroka', False,]
values_dict = {'a': 1, 'b': 27, 'c': [1, 2, 3]}
print_params(b = 25)
print_params(c = [1, 2, 3])
print_params(*values_list)
print_params(**values_dict)
