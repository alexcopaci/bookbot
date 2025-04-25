def word_count(text):
    sep_word = text.split()
    word_numb = len(sep_word)
    return word_numb


def char_count(text):
    char_number = {}
    text = text.lower()
    for c in text:
        if c in char_number:
            char_number[c] += 1
        else:
            char_number[c] = 1
    return char_number

def chars_dict_to_sorted_list(char_dict):
    chars_list = [] 
    for char, count in char_dict.items(): 
        chars_list.append({"char": char , "num": count})

    # define a function that tells sort what value to use
    def sort_on(dict):
        return dict["num"]
    
    # sort the list from greatest to least 
    chars_list.sort(reverse=True, key=sort_on)

    return chars_list
    
