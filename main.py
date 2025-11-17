def get_book_text(path_to_file):
    file_contents = ""
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    words = text.split()
    return len(words)

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = count_words(text)
    print(f"Found {num_words} total words")

main()