calls = 0


def count_calls():
    global calls
    calls = calls + 1


def string_info(name):
    count_calls()
    info = (len(name), name.upper(), name.lower())
    return info


def is_contains(string, list_to_search):
    count_calls()
    string = string.upper()
    for word in list_to_search:
        if string == word.upper():
            return True
    return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
