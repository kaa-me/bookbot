def get_num_words(get_book_text):
    book_text = get_book_text()
    num_words = book_text.split()
    print(f'Found {len(num_words)} total words')

def get_num_char(text):
    char_counts = {}
    
    for char in text:
        lowered_char = char.lower()
        if lowered_char in char_counts:
            char_counts[lowered_char] += 1
        else:
            char_counts[lowered_char] = 1
    return char_counts

