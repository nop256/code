def letters_up_to_char(long_word, char):
    result = ""
    i = 0
    while i < len(long_word) and long_word[i] != char:
        result += long_word[i]
        i += 1

    return result


print(letters_up_to_char('coderoxthesox', 'x'))
print(letters_up_to_char('abcdefghijklmnop', 'f'))
