

def get_num_words(get_book_text):
    book_text = get_book_text()
    num_words = book_text.split()
    print(f'Found {len(num_words)} total words')

