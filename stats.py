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

#this will count all the occurnaces of a word in the given book and returns the top 50 words used
def common_words(book):
    word_dict = {}
    words = book.lower().split()
    for word in words:
        word = word.strip('.,!?";:(){}[]')
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    word_list = list(word_dict.items())
    word_list.sort(key=lambda item: item[1], reverse=True)
    return word_list[:50]


