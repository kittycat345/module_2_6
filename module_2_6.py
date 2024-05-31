def single_root_words(root_word, *other_words):
    same_word = []
    root_word_low = root_word.lower()
    other_words_low = []
    for k in range(len(other_words)):
        other_words_low.append(other_words[k].lower())
    if len(root_word) < len(other_words[0]):
        for i in range(len(other_words)):
            if other_words_low[i - 1].count(root_word_low) > 0:
                same_word.append(other_words[i - 1])
    if len(root_word) > len(other_words[0]):
        for i in range(len(other_words)):
            if root_word_low.count(other_words_low[i]) > 0:
                same_word.append(other_words[i])
    return same_word


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
