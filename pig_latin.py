def pig_latin():
    w = input('pig latin game start, please type a word. : ')
    if w[0] in 'aeiou':
        latin_word = w + 'way'
    else:
        w1 = w[1:] + w[0]
        latin_word = w1 + 'ay'
    print(latin_word)

pig_latin()