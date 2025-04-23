from stats import get_word_count
from stats import get_char_count
from stats import sort_dict
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(filepath):
    with open(f"{filepath}") as f:
        file_contents = f.read()
    return file_contents


def main(filepath):
    book = get_book_text(sys.argv[1])
    word_count = get_word_count(book)
    char_count = get_char_count(book)
    sorted_dict = sort_dict(char_count)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_dict:
        if item[0].isalpha():
            print(f"{item[0]}: {item[1]}")
        else:
            continue
    print("============= END ===============")
    
main(sys.argv[1])