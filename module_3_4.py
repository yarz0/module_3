# def single_root_words(root_words, *other_words):
#     same_words = []
#     for word in other_words:
#         word.lower()
#         root_words.lower()
#         if word.count(word):
#             same_words.append(word)
#
#         return same_words
#
#
# print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
#
# print(single_root_words('Disablement', 'able', 'mable', 'disable', 'bagel'))

slovo = ['richiest', 'orichalcum', 'cheers', 'richies']
root = 'Rich'
result = []
for word in slovo:
    if word.lower().startswith(root.lower()) in slovo:
        result.append(word)

print(result)


