def get_word_count(book):
    count = 0
    word_list = book.split()
    for word in word_list:
        count += 1
    return count

def get_char_count(book):
    char_dict = {}
    for char in book:
        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_dict(unsorted_char_dict):
    char_items = list(unsorted_char_dict.items())
    char_items.sort(key = lambda item: item[1], reverse = True)
    return char_items
