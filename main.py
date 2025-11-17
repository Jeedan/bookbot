from stats import get_num_words
from stats import get_character_count

def get_book_text(path_to_file):
    file_contents = ""
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def print_character_counts(characters):
    for c in characters:
        print(f"'{c}': {characters[c]}")    

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(book_text)
    total_characters = get_character_count(book_text) 
    print(f"Found {num_words} total words")
    print_character_counts(total_characters)


main()