from stats import get_word_count

def get_book_text(filepath):
    with open(f"{filepath}") as f:
        file_contents = f.read()
    return file_contents


def main():
    book = get_book_text("books/frankenstein.txt")
    word_count = get_word_count()
    print(f"{word_count} words found in the document")
    
main()