from stats import return_sorted_count, count_characters, count_words, get_book_text

def main():
    book = "books/frankenstein.txt"
    #text = get_book_text("books/frankenstein.txt")
    #num_words = count_words("books/frankenstein.txt")
    #print(f"{num_words} words found in the document")
    #print(count_characters(book))
    print(f"Found {count_words(book)} total words")
    return_sorted_count(book)

main()