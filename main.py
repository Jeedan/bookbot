from stats import get_num_words, get_character_count, sort_characters
import sys
def get_book_text(path_to_file):
    file_contents = ""
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def print_character_counts(characters):
    for chars in characters:
        print(f"'{chars["char"]}: {chars["count"]}'")  

def main():
    # if system argv is too short or empty, 
    # exit and show how to use the script
    if(len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)

    num_words = get_num_words(book_text)

    total_characters = get_character_count(book_text) 
    # we sort the characters from highest to lowest count
    sorted_characters = sort_characters(total_characters)

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"----------- Character Count ----------")
    #print our sorted_character list of dictionaries
    print_character_counts(sorted_characters)
    
    print(f"============ END ============")

main()