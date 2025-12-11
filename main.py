from stats import get_num_words

def get_book_text():
    with open("/Volumes/Samsung_SSD/OrbStack/dev/home/dev/bookbot/bookbot/books/frankenstein.txt", "r") as f:
        file_content = f.read()
    return file_content

def main():
    get_num_words(get_book_text)


main()
    
