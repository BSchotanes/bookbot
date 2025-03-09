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

def sort_dictonary(alpha_dictionary):
    list_of_dict = []

    for character in alpha_dictionary:
        char_dict = {"char": character, "count": alpha_dictionary[character]}
        list_of_dict.append(char_dict)

    list_of_dict.sort(reverse=True, key=sort_on)

    return list_of_dict

def sort_on(alpha_dictionary):
    return alpha_dictionary["count"]