data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def count_data_structure_elements(structure):
    total_sum = 0
    for item in structure:
        if isinstance(item, int):
            total_sum += item
        elif isinstance(item, str):
            total_sum += len(item)
        elif isinstance(item, dict):
            if item:
                total_sum += count_data_structure_elements(item.values())
                total_sum += count_data_structure_elements(item.keys())
        elif isinstance(item, (list, tuple, set)):
            if item:
                total_sum += count_data_structure_elements(item)
    return total_sum


print(count_data_structure_elements(data_structure))
