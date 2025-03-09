def get_word_count(booktext):
    word_count = 0
    split_text = booktext.split()
    for text in split_text:
        word_count += 1
    return word_count

def character_count(booktext):
    alphas = {}

    for text in booktext:
        if text.lower() in alphas:
            alphas[text.lower()] += 1
        else:
            alphas[text.lower()]  = 1
    return alphas

