def toggle(word_in):
    alphabet_helper = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    word_out = ''
    for x in word_in:
        for pos in range(52):
            if alphabet_helper[pos] == x:
                i = pos
        if x not in alphabet_helper:
            word_out += x
        elif i >=26:
            word_out += alphabet_helper[i-26]
        else:
            word_out += alphabet_helper[i+26]
    return word_out


if __name__ == "__main__":
    word_in = input("Enter your word: ")
    print("Result : ", end = ' ')
    print(toggle(word_in))
