from stats import get_num_words
from stats import get_num_char 

def get_book_text():
    with open("./books/frankenstein.txt", "r") as f:
        file_content = f.read()
    return file_content

def main():
    book_text = get_book_text()
    get_num_words(get_book_text)
    character_counts = get_num_char(book_text)
    print(character_counts)


if __name__ == "__main__":
    main()