def get_num_words(text):
    words = text.split()
    print(f"Found {len(words)} total words")


def get_num_char(text):
    char_counts = {}

    for char in text:
        lowered_char = char.lower()
        if lowered_char in char_counts:
            char_counts[lowered_char] += 1
        else:
            char_counts[lowered_char] = 1

    return char_counts


def sort_characters(char_counts):
    chars_list = []

    for char, count in char_counts.items():
        if char.isalpha():
            chars_list.append({"char": char, "num": count})

    # sort from greatest to least
    chars_list.sort(key=get_num, reverse=True)

    return chars_list


def get_num(item):
    return item["num"]
