def get_num_words(text):
    words = text.split()
    return len(words)

# returns a dictionary
# convert to lower case .lower() so no duplicates
# use dictionary String -> int 
# example: {'p': 6121, 'r': 20818, 'o': 25225, ...
def get_character_count(text):
    characters = {}
    for letter in text.lower():
        characters[letter] = characters.get(letter, 0) + 1  
    return characters