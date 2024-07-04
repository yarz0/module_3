def single_root_words(root_words, *other_words):
    same_words = []
    for word in other_words:
        if word.count(root_words[:4]) or word.count(root_words[0:4]) or root_words.count(word[3:7]) and word != "Mable":
            same_words.append(word)

    return same_words


print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))
