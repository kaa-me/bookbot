import sys

from stats import get_num_char, get_num_words, sort_characters


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    with open(book_path, "r") as f:
        book_text = f.read()

    get_num_words(book_text)

    char_counts = get_num_char(book_text)
    sorted_chars = sort_characters(char_counts)

    for item in sorted_chars:
        print(f"'{item['char']}: {item['num']}'")


if __name__ == "__main__":
    main()
