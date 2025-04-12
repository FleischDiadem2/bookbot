def return_sorted_count(filepath):
    sorted_letters = dict(sorted(count_characters(filepath).items()))
    for letter in sorted_letters:
        if letter.isalpha():
            print(f"{letter}: {sorted_letters[letter]}")

def count_characters(filepath):
    dict_char_count = {}
    with open(filepath) as f:
        characters = list(f.read().lower())
    for char in characters:
        dict_char_count[char] = dict_char_count.get(char, 0) +1
    return dict_char_count

def count_words(filepath):
    word_count = len(get_book_text(filepath).split())
    return word_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents