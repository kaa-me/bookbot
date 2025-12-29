from stats import get_num_char, get_num_words, sort_characters


def get_book_text():
    with open("./books/frankenstein.txt", "r") as f:
        return f.read()


def main():
    book_text = get_book_text()

    get_num_words(book_text)

    char_counts = get_num_char(book_text)
    sorted_chars = sort_characters(char_counts)

    for item in sorted_chars:
        print(f"'{item['char']}: {item['num']}'")


if __name__ == "__main__":
    main()
