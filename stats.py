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

def sort_on(items):
    return items["count"]

# I consulted Boots and Chat GPT to get this to work
# i guess I need more training on Dictionaries
def sort_characters(characters):
    char_list = []
    #char_list = [{"char":c,"count":n} for c,n in characters.items()]

    for c, n in characters.items():
        char_list.append({"char" : c, "count": n})

    char_list.sort(reverse=True, key=sort_on)
    return char_list