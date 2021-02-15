def duplicate_encode(word):
    iter_word = str(word)
    check_list = []
    formatted_list = []
    position = 0
    for i in iter_word:
        position += 1
        if i not in check_list and i not in (iter_word[position:]):
            check_list.append(i)
            i = '('
            formatted_list.append(i)
        else:
            check_list.append(i)
            i = ')'
            formatted_list.append(i)

    return ''.join(map(str, formatted_list))


word = 'recede'
print(duplicate_encode(word))